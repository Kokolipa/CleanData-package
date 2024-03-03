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
        Args:
            data (pd.DataFrame): pd.DataFrame
            subset (list | pd.Series): A list of features OR a singular searies. Default = None (return duplicates for the intire dataset).
            identify_all (bool, optional): If 'first' specified, then return only the first instances of the duplicated values. Defaults to False (identify all duplicated values). If 'last' return only the last instances of the duplicated values. Defaults to False (identify all duplicated values)
        """
        return data[data.duplicated(subset=subset, keep=identify_all)]            
    
    
    #* (2) Method 
    @classmethod
    def drop_duplicates(cls, data: pd.DataFrame, subset=None, identify_all='first') -> pd.DataFrame:
        """Drop duplicated values in DataFrame. 
        Args:
            data (pd.DataFrame): pd.DataFrame
            subset (list | pd.Series): A list of features OR a singular searies. Default = None (applies to all features).
            identify_all (bool, optional): Defaults to 'first' (drop all duplicated values but keep the 'first' instances); If 'last' return only the last instances of the duplicated values; If False = drop all duplicates.
        """
        return data.drop_duplicates(subset=subset, keep=identify_all, inplace=True)       
