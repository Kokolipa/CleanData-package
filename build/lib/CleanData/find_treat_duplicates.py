# Import Dependencies
import pandas as pd

#!############################# # Treat Duplicated Values Class # ##############################

class FindTreatDuplicates:
    def __init__(self, data):
        self.data = data
    
    
    #* (1) Method 
    @classmethod
    def find_duplicates(cls, data: pd.DataFrame, subset=None, identify_all=False) -> pd.DataFrame:
        """Idenfify duplicated values in DataFrame. 

        Parameters:
            - data (pd.DataFrame): pd.DataFrame
            - subset (list | pd.Series): A list of features OR a singular searies. Default = None (return duplicates for the intire dataset).
            - identify_all (bool, optional): If 'first' specified, then return only the first instances of the duplicated values. Defaults to False (identify all duplicated values). If 'last' return only the last instances of the duplicated values. Defaults to False (identify all duplicated values)
        
        Example usage:
        --------------
        .. code-block:: python

            # Seed for reproducibility
            np.random.seed(0)

            # Sample data generation
            data = {
                'id': np.arange(1, 51),
                'name': np.random.choice(['John', 'Jane', 'Doe', 'Emily', 'Michael'], 50),
                'age': np.random.randint(18, 60, size=50),
                'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 50)
            }

            df = pd.DataFrame(data)

            # Introducing duplicates
            duplicates = pd.DataFrame({
                'id': [51, 52, 53, 54, 55],  # New IDs to avoid confusion with the unique identifier intention
                'name': ['John', 'Jane', 'Doe', 'Emily', 'Michael'],
                'age': [25, 30, 45, 22, 35],
                'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
            })

            # Adding duplicates to the original dataframe
            df = pd.concat([df, duplicates, duplicates])  # Adding twice for multiple duplicates

            # Shuffling the dataframe to mix duplicates
            df = df.sample(frac=1).reset_index(drop=True)

            # Return all the duplicated values
            CleanData.find_treat_duplicates.FindTreatDuplicates.find_duplicates(df, subset='id')

        """
        return data[data.duplicated(subset=subset, keep=identify_all)]            
    
    
    #* (2) Method 
    @classmethod
    def drop_duplicates(cls, data: pd.DataFrame, subset=None, identify_all='first') -> pd.DataFrame:
        """Drop duplicated values in DataFrame. 

        Parameters:
            - data (pd.DataFrame): pd.DataFrame
            - subset (list | pd.Series): A list of features OR a singular searies. Default = None (applies to all features).
            - identify_all (bool, optional): Defaults to 'first' (drop all duplicated values but keep the 'first' instances); If 'last' return only the last instances of the duplicated values; If False = drop all duplicates.
        
        Example usage:
        --------------
        .. code-block:: python

            # Seed for reproducibility
            np.random.seed(0)

            # Sample data generation
            data = {
                'id': np.arange(1, 51),
                'name': np.random.choice(['John', 'Jane', 'Doe', 'Emily', 'Michael'], 50),
                'age': np.random.randint(18, 60, size=50),
                'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 50)
            }

            df = pd.DataFrame(data)

            # Introducing duplicates
            duplicates = pd.DataFrame({
                'id': [51, 52, 53, 54, 55],  # New IDs to avoid confusion with the unique identifier intention
                'name': ['John', 'Jane', 'Doe', 'Emily', 'Michael'],
                'age': [25, 30, 45, 22, 35],
                'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
            })

            # Adding duplicates to the original dataframe
            df = pd.concat([df, duplicates, duplicates])  # Adding twice for multiple duplicates

            # Shuffling the dataframe to mix duplicates
            df = df.sample(frac=1).reset_index(drop=True)

            # Return all the duplicated values
            CleanData.find_treat_duplicates.FindTreatDuplicates.drop_duplicates(df, subset='id')
        """
        return data.drop_duplicates(subset=subset, keep=identify_all, inplace=True)       
