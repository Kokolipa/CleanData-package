
# Import Dependencies
import warnings

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

warnings.simplefilter(action='ignore', category=FutureWarning)

#!############################# # Treating NA values subclass # ##############################

class TreatNA:
    def __init__(self, data):
        self.data = data

    
    #* (1) Method 
    @classmethod
    def IdentifyNAs(cls, data: pd.DataFrame) -> pd.DataFrame:
        missing_values = [np.nan, 'missing', 'null', '', 'empty']
        # Find rows containing any of the missing values
        mask = data.apply(lambda row: any(str(val) in missing_values for val in row), axis=1)
        return data[mask]

    
    
    
    
    #* (2) Method
    @classmethod
    def complete_case_na(cls, data: pd.DataFrame) -> pd.DataFrame:
        # Include edge cases
        missing_values = ['missing', 'null', '', 'empty']

        # Filter the data to return CCA with edge cases
        return data[data.apply(lambda row: any(pd.isna(val) or str(val) in missing_values for val in row), axis=1)]

    
    
    
    
    #* (3) Method 
    @classmethod
    def drop_complete_case_na(cls, data: pd.DataFrame) -> pd.DataFrame:
        # Identify rows to drop and return the corresponding index value
        missing_values = ['missing', 'null', '', 'empty']
        rows_to_drop = data[data.apply(lambda row: any(pd.isna(val) or str(val) in missing_values for val in row), axis=1)].index

        # Drop rows
        cleaned_data = data.drop(index=rows_to_drop)
        return cleaned_data
    
    
    
    
    
    #* (4) Method 
    @classmethod
    def DataImpute(cls, data: pd.DataFrame, features: list, missing_values=np.nan, numeric_strategy='mean', string_strategy='constant', string_fill_value=None):
        """Apply univariate data imputation for numerical & categorical strategies. Suitable for MCAR cases (A variable is missing completely at random (MCAR) if the probability of being missing is the same for all the observations)

        Args:
            - data (pd.DataFrame)
            - features (list)
            - missing_values (the placeholder for the missing values): **Defaults to np.nan;  Can also be pd.NA, int, float,  or str. 
            - numeric_strategy (str, optional): _description_. Defaults to 'mean'; Numerical data imputation (strategy).
            - string_strategy (str, optional): _description_. Defaults to 'constant'. Categorical data imputation (strategy).
            - string_fill_value (_type_, optional): When strategy == “constant”, fill_value is used to replace all occurrences of missing_values. Defaults to None.

        Returns:
            _type_: pd.DataFrame
        """            
        imputed_data = data.copy()
        numeric_features = list(data.select_dtypes(include=np.number).columns)
        string_features = list(data.select_dtypes(include=object).columns)

        # Numeric imputation: Mean, Median, and Mode
        if any(feature in numeric_features for feature in features):
            numeric_imputer = SimpleImputer(strategy=numeric_strategy, missing_values=missing_values)
            imputed_data[numeric_features] = numeric_imputer.fit_transform(data[numeric_features])

        # String/object imputation: Custom (user based)
        if any(feature in string_features for feature in features):
            string_imputer = SimpleImputer(strategy=string_strategy, fill_value=string_fill_value, missing_values=missing_values)
            imputed_data[string_features] = string_imputer.fit_transform(data[string_features])

        return imputed_data
    
    
    
    
    
    #* (5) Method 
    @classmethod
    def MNAR(cls, data:pd.DataFrame , features:list) -> pd.DataFrame:
        """Missing of values is not at random (MNAR) if their being missing depends on information not recorded in the dataset. Transaction dataset = the values are missing if if we don't have transaction_number (NOTE: here we could have more the one independent variable)
        NOTE: **Independent = transaction_number; **dependent (in their occurance): the rest of the variables

        Args:
            data (_type_): pd.DataFrame / np.array (2d array)

        Returns:
            pd.DataFrame: This function will drop all corresponsing NA values from the dependent variables based on the Independent variable/s
        """            
        return data.loc[:, features].dropna()
    

    
    
    
    
    #* (6) Method
    @classmethod
    def logistic_regression_MAR_identifier(cls,df: pd.DataFrame, max_iter=1000) -> pd.DataFrame:
        """_summary_

        Args:
            df (pd.DataFrame): _description_
            max_iter (int, optional): _description_. Defaults to 1000.

        Returns:
            pd.DataFrame: _description_
        """        
        # Identify columns containing NA/NaN values
        columns_with_na = df.columns[df.isna().any()].tolist()

        # Create NA flags columns
        flag_columns = {f'Flag {i+1}': df[col].isna().astype(int) for i, col in enumerate(columns_with_na)}

        # Vertically append the flags to the data frame
        df = pd.concat([df, pd.DataFrame(flag_columns)], axis=1)

        # Drop the columns that contain NA values
        df.drop(columns=columns_with_na, inplace=True)

        # Run logistic regression for evaluation
        results = []  # Initialize an empty list to store results
        for col in df.columns:
            X = pd.get_dummies(df.drop(columns=[col]), drop_first=True)
            y = df[col]

            # Check if y is binary/multi-class categorical for logistic regression
            if y.nunique() <= 2:
                X_scaled = StandardScaler().fit_transform(X)
                try:
                    lr = LogisticRegression(max_iter=max_iter, n_jobs=-1).fit(X_scaled, y)
                    # Collect coefficients along with the column name
                    for idx, coef in enumerate(lr.coef_[0]):
                        results.append({'Column': col, 'Feature': X.columns[idx], 'Coefficient': float(coef)})
                except ValueError as e:
                    print(f"Error fitting model with target {col}: {e}")
            else:
                print(f"Skipping '{col.upper()}' - not suitable for logistic regression.")

        # Convert results to DataFrame for easier analysis and return it
        results_df = pd.DataFrame(results)

        # Specify data types for each column
        results_df = results_df.astype({'Column': 'str', 'Feature': 'str', 'Coefficient': 'float'})

        return results_df