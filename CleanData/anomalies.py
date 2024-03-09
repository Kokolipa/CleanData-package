# Import Dependencies
import time
import warnings

import numpy as np
import pandas as pd
from pyod.models.cd import CD
from pyod.utils.data import get_outliers_inliers
from sklearn.neighbors import LocalOutlierFactor

warnings.simplefilter(action='ignore', category=FutureWarning)



#!############################# # Find & Treat Anomalies # ##############################
    #FIXME: finalise Anomalies class -> Create a function to find categorical Anomalies with value_counts(normalise=True). 

class Anomalies:
    def __init__(self, data):
        self.data = data

    
    #* (1) Method
    @classmethod # class method for date anomalies
    def find_date_anomalies(cls, data:pd.DataFrame, date_column: str, identify_by='month'):
        """Find anomalies in date data.

        Parameters:
            - data (pd.DataFrame): DataFrame containing date information.
            - date_column (str): Name of the column containing date data.
            - identify_by (str, optional): Identifier for type of anomaly to find ('month' or 'year'). Defaults to 'month'.

        Returns:
            pd.DataFrame: DataFrame containing anomalies based on specified identification criteria.
        
        Example usage:
        --------------
        .. code-block:: python
            
            # Import dependencies
            import pandas as pd
            import numpy as np
            from datetime import timedelta, date
            import CleanData

            # Function to generate daily dates except for anomalies
            def create_date_dataset(start_date, end_date, anomaly_month_year, missing_months_year):
                current_date = start_date
                dates = []

                while current_date <= end_date:
                    current_month_year = (current_date.month, current_date.year)

                    # Skip dates for the anomaly month (less than 28 days)
                    if current_month_year == anomaly_month_year:
                        if len(dates) % 29 != 0:  # Ensuring this month has fewer than 28 records
                            dates.append(current_date)
                        current_date += timedelta(days=2)  # Skipping days to ensure less than 28 records
                    # Skip entire months for the missing months in the specified year
                    elif current_month_year[1] == missing_months_year and current_month_year[0] in [2, 3]:
                        current_date += timedelta(days=1)  # Move to the next day to check for month increment
                        if current_date.month in [2, 3]:  # If still in the missing month, skip to next month
                            continue
                    else:
                        dates.append(current_date)
                        current_date += timedelta(days=1)

                return dates

                # Define the start and end dates for the dataset
                start_date = date(2022, 1, 1)
                end_date = date(2023, 12, 31)

                # Specify the anomaly month/year and the year with missing months
                anomaly_month_year = (4, 2022)  # April 2022 will have less than 28 records
                missing_months_year = 2023  # February and March 2023 will be missing

                # Generate the dataset
                dates = create_date_dataset(start_date, end_date, anomaly_month_year, missing_months_year)

                # Create a DataFrame
                df = pd.DataFrame(dates, columns=['Date'])

                # Display the first few rows of the DataFrame to confirm
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)

                df['month'] = df['Date'].dt.month
                df['year'] = df['Date'].dt.year
                test = df.groupby(['year','month']).size().reset_index(name="days_count")

                year_count = test.groupby('year')["days_count"].sum()

                CleanData.anomalies.Anomalies.find_date_anomalies(df, date_column='Date', identify_by='month')

        """   

        if identify_by == 'month':
            data['year'] = data[date_column].dt.year
            data['month'] = data[date_column].dt.month
            eval_data = data.groupby(['year', 'month']).size().reset_index(name="days_count")
            return eval_data.loc[eval_data['days_count'] < 28]
        
        elif identify_by == 'year':
            # Create year & month features
            data['month'] = data[date_column].dt.month
            data['year'] = data[date_column].dt.year
            eval_data = data.groupby(['year', 'month']).size().reset_index(name="days_count")
            year_count = eval_data.groupby('year')['days_count'].sum().reset_index()
            year_missing = year_count[year_count['days_count'] < 365]

            # Print statements for missing days in each year
            for index, row in year_missing.iterrows():
                missing_days = 365 - row['days_count']
                print(f"Year {row['year']} is missing {missing_days} days ({round(missing_days/30, 2)} month/s)")
    
    
    
    
    
    
    
    #* (2) Method
    @classmethod
    def nonlinear_outliers_influencers_knn(cls, data: pd.DataFrame, features: list, neighbors_fraction: float = 0.1, contamination='auto', center_measure='mean'):
        """Detects outliers in a dataset based on nonlinear methods and KNN.

        Parameters:
            - data (pd.DataFrame): The dataset to analyze.
            - features (list): List of features to consider for outlier detection.
            - neighbors_fraction (float, optional): Fraction of dataset size to use as neighbors. Defaults to 0.1.
            - contamination (str, optional): Method for calculating contamination ('auto', '3std'). Defaults to 'auto'.
            - center_measure (str, optional): Central distribution measure to use ('mean' or 'median'). Defaults to 'mean'.

        Returns:
            pd.DataFrame: DataFrame of outliers.
        
        Example usage:
        --------------
        .. code-block:: python
        
            # Note: The application of this function is similar to the linear outliers function

            # Import dependencies
            import numpy as np
            import pandas as pd
            import CleanData


            # Set random seed for reproducibility
            np.random.seed(42)

            # Generate a fake dataset with 100 samples and 3 features
            n_samples = 1000
            n_features = 5

            # Generate random data for the features
            X = np.random.rand(n_samples, n_features)

            # Generate random outliers by adding noise to the data
            outliers_indices = np.random.choice(n_samples, 5, replace=False)  # Select 5 random indices as outliers
            X[outliers_indices] += 10  # Add noise to create outliers

            # Create Dataframe
            df = pd.DataFrame(X, columns=['Column' + ' ' + str(i) for i in range(1, n_features+1, 1)])

            # Identify outliers influencers from your dataset
            CleanData.anomalies.Anomalies.nonlinear_outliers_influencers_knn(df, df.columns.to_list())
        """    
        
        if contamination == 'auto': 
            # Start the timer
            start_time = time.time()
            
            # Calculate the number of neighbors based on a fraction of the dataset size
            n_neighbors = max(1, int(len(data) * neighbors_fraction))

            # Use Local Outlier Factor for outlier detection (contamination auto = 0.1)
            clf = LocalOutlierFactor(n_neighbors=n_neighbors, contamination='auto')
            X = data[features]
            # Fit the model and predict outliers (-1 for outliers, 1 for inliers)
            y_pred = clf.fit_predict(X)
            
            # Filter outliers
            X['outlier'] = y_pred
            outliers = X[X['outlier'] == -1]
            
            # End the timer
            end_time = time.time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            
            # Convert elapsed time to milliseconds
            elapsed_time_ms = elapsed_time * 1000

            # Print the elapsed time in milliseconds
            print("Elapsed time:", elapsed_time_ms, "milliseconds")
            print("n_nighbors:", n_neighbors)
            return outliers.drop('outlier', axis=1)
        
        elif contamination == '3std':
            # Start the timer
            start_time = time.time()
            
            # Calculate the mean and standard deviation of features
            if center_measure == 'mean':
                centers = data[features].mean().values
                spreads = data[features].std().values
            elif center_measure == 'median':
                centers = data[features].median().values
                spreads = data[features].std().values  
                    
            # Calculate contamination -> return 3 STD from the mean +/-
            contamination_values = []
            for i, spread in enumerate(spreads):
                if center_measure == 'mean':
                    outlier_mask = (data.iloc[:, i] < centers[i] - 3 * spread) | (data.iloc[:, i] > centers[i] + 3 * spread)
                elif center_measure == 'median':
                    outlier_mask = (data.iloc[:, i] < centers[i] - 3 * spread) | (data.iloc[:, i] > centers[i] + 3 * spread)
                contamination_values.append(data[outlier_mask].shape[0] / data.shape[0])
                    
            # Return contamination
            contamination = np.median(contamination_values)
            
            # Calculate the number of neighbors based on a fraction of the dataset size
            n_neighbors = max(1, int(len(data) * neighbors_fraction))

            # Use Local Outlier Factor for outlier detection (contamination auto = 3 STD away from the mean +/-) 
            clf = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
            X = data[features]
            # Fit the model and predict outliers (-1 for outliers, 1 for inliers)
            y_pred = clf.fit_predict(X)
            
            # Filter outliers
            X['outlier'] = y_pred
            outliers = X[X['outlier'] == -1]
            
            # End the timer
            end_time = time.time()
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            
            # Convert elapsed time to milliseconds
            elapsed_time_ms = elapsed_time * 1000

            # Print the elapsed time in milliseconds
            print("Elapsed time:", elapsed_time_ms, "milliseconds")
            print("n_nighbors:", n_neighbors)
            return outliers.drop('outlier', axis=1)
        else:
            raise ValueError("Invalid value for contamination. Please provide 'auto' or '3std'.")

    
    
    
    
    
    
    
    #* (3) Method
    @classmethod
    def linear_outliers_influencers(cls,data:pd.DataFrame ,features:list, center_measure='mean'):
        """This function align for linear datasets to explore outliers using Cook's D (distance based evaluation). A Cook’s result > 1 = Significant influence, while Cook’s D > 0.5 is worth investigating. 

        Parameters:
            - data (pd.DataFrame): The dataset to analyze.
            - features (list): List of features to consider for outlier detection.
            - center_measure (str, optional): Central distribution measure to use ('mean' or 'median'). Defaults to 'mean'.

        Returns:
            pd.DataFrame: DataFrame of outliers.
        
        Example usage:
        --------------
        .. code-block:: python

            # Import dependencies
            import numpy as np
            import pandas as pd
            import CleanData


            # Set random seed for reproducibility
            np.random.seed(42)

            # Generate a fake dataset with 100 samples and 3 features
            n_samples = 1000
            n_features = 5

            # Generate random data for the features
            X = np.random.rand(n_samples, n_features)

            # Generate random outliers by adding noise to the data
            outliers_indices = np.random.choice(n_samples, 5, replace=False)  # Select 5 random indices as outliers
            X[outliers_indices] += 10  # Add noise to create outliers

            # Create Dataframe
            df = pd.DataFrame(X, columns=['Column' + ' ' + str(i) for i in range(1, n_features+1, 1)])

            # Identify outliers influencers from your dataset
            CleanData.anomalies.Anomalies.linear_outliers_influencers(df, df.columns.to_list())
        """            
        
        # Calculate the mean and standard deviation of features
        if center_measure == 'mean':
            centers = data[features].mean().values
            spreads = data[features].std().values
        elif center_measure == 'median':
            centers = data[features].median().values
            spreads = data[features].std().values  
                    
        # Calculate contamination -> return 3 STD from the mean +/-
        contamination_values = []
        for i, spread in enumerate(spreads):
            if center_measure == 'mean':
                outlier_mask = (data.iloc[:, i] < centers[i] - 3 * spread) | (data.iloc[:, i] > centers[i] + 3 * spread)
            elif center_measure == 'median':
                outlier_mask = (data.iloc[:, i] < centers[i] - 3 * spread) | (data.iloc[:, i] > centers[i] + 3 * spread)
            contamination_values.append(data[outlier_mask].shape[0] / data.shape[0])
                    
        # Return contamination
        contamination = np.median(contamination_values)

        # Splitting to X & Y columns
        X = data[features]

        # Instantiate the Cook's D evaluator
        cooks_D = CD(contamination=contamination)
        # predict outliers
        cooks_D.fit(X)

        # predict outliers & inliners (bool array = 1/0)
        pred = cooks_D.predict(X, return_confidence=True)
        # We have to transpose the dataset to match the dataset
        df = pd.DataFrame(pred).T
        df = df.rename(columns={0: "predictions", 1: "confidence"})

        X_array = X.to_numpy() # Transforming to numpy array to leverage get_outliers_inliers
        y_array = df["predictions"]   
            
        # Extracting inliners and outliers
        X_outliers, X_inliners = get_outliers_inliers(X_array, y_array)

        # Result outliers
        return pd.DataFrame(X_outliers, columns=X.columns)