
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
        for col in data.select_dtypes(exclude="number").columns:
            data[col] = data[col].str.lower()
            if data[col].str.startswith(" ").any() or data[col].str.endswith(" ").any():
                data[col] = data[col].str.strip()
        return data

    
    #* (2) Method 
    @classmethod
    def object_to_numeric(cls,df:pd.DataFrame, features: list) -> pd.DataFrame:
        for col in df[features].columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df[col]
    
    
    #* (3) Method 
    @classmethod
    def correct_word(cls, word: str) -> str:
        spell = SpellChecker()
        return spell.correction(word)
    
    
    #* (4) Method 
    @classmethod
    def correct_sentence(cls, strings:str) -> str:
        words = strings.split(' ')  # Split the string into words
        corrected_words = [cls.correct_word(word) for word in words]  # Apply correction to each word
        return ' '.join(corrected_words)  