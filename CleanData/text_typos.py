
# Import Dependencies
import pandas as pd
from spellchecker import SpellChecker

#!############################# # Find & Treat Text Typos # ##############################

class TextTypos:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    #* (1) Method
    @classmethod
    def strip_and_lower_strings(cls, data: pd.DataFrame) -> pd.DataFrame: 
        """
        Strip whitespace and convert strings to lowercase in DataFrame.

        Args:
            data (pd.DataFrame): Input DataFrame containing string columns.

        Returns:
            pd.DataFrame: DataFrame with strings stripped of leading/trailing whitespace and converted to lowercase.
        """   
        for col in data.select_dtypes(exclude="number").columns:
            data[col] = data[col].str.lower()
            if data[col].str.startswith(" ").any() or data[col].str.endswith(" ").any():
                data[col] = data[col].str.strip()
        return data

    
    #* (2) Method 
    @classmethod
    def object_to_numeric(cls,df:pd.DataFrame, features: list) -> pd.DataFrame:
        """
        Convert specified columns from object type to numeric type.

        Args:
            df (pd.DataFrame): Input DataFrame containing columns to be converted.
            features (list): List of column names to be converted to numeric type.

        Returns:
            pd.DataFrame: DataFrame with specified columns converted to numeric type.
        """       

        for col in df[features].columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df[col]
    
    
    #* (3) Method 
    @classmethod
    def correct_word(cls, word: str) -> str:
        """Correct spelling of a word using SpellChecker.

        Args:
            word (str): Input word to be corrected.

        Returns:
            str: Corrected version of the input word.
        """    
        spell = SpellChecker()
        return spell.correction(word)
    
    
    #* (4) Method 
    @classmethod
    def correct_sentence(cls, strings:str) -> str:
        """Correct spelling in a sentence using SpellChecker.

        Args:
            strings (str): Input sentence to be corrected.

        Returns:
            str: Corrected version of the input sentence.
        """     
        words = strings.split(' ')  # Split the string into words
        corrected_words = [cls.correct_word(word) for word in words]  # Apply correction to each word
        return ' '.join(corrected_words)  