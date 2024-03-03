
# Import Dependencies
import numpy as np
import pandas as pd

#!############################# # Memory Optimisation # ##############################

class Memory:
    def __init__(self, data):
        self.data = data
    
    
    #* (1) Method 
    @classmethod
    def optimise_mem(cls, data: pd.DataFrame, verbose=True) -> pd.DataFrame:
        # Create a function to optimise the memory
        start_mem = data.memory_usage().sum() / 1024 ** 2
        numerics = ["int8", "int16", "int32", "int64", "float16", "float32", "float64"]
        for col in data.columns:
            col_type = data[col].dtypes
            if col_type in numerics:
                # Retrieve the min and max values of a column
                c_min = data[col].min()
                c_max = data[col].max()
                # ? Treating integer columns
                if str(col_type)[:3] == "int":
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        data[col] = data[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        data[col] = data[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        data[col] = data[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        data[col] = data[col].astype(np.int64)
                # ? Treating float columns 
                else:
                    if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                        data[col] = data[col].astype(np.float32)
                    elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        data[col] = data[col].astype(np.float32)
                    else:
                        data[col] = data[col].astype(np.float64)
        # Returning the end megabytes calculation (reduction)
        end_mem = data.memory_usage().sum() / 1024 ** 2

        if verbose:
            print("Mem. usage decreased to {:.2f} Mb ({:.1}% reduction)".format(end_mem, 100 * ((start_mem - end_mem) / start_mem)))
        
        return data 