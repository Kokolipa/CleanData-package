
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

        Parameters:
            - data (pd.DataFrame): Input DataFrame containing string columns.

        Returns:
            pd.DataFrame: DataFrame with strings stripped of leading/trailing whitespace and converted to lowercase.
        
        Example usage:
        --------------
        .. code-block:: python

            # Import dependencies
            import pandas as pd
            import CleanData

            # sample data
            data = {
                'Text': [
                    "    The quck brown fox jumps over the lazy dog.",
                    "She is an engeneer and work in a tech company.",
                    "I'm goign to the beech this weekend.",
                    "    His favorit! color is purpel.",
                    "The concert was amazig, I reccomend it to everyone.",
                    "    The resturant was ful of delicius food.",
                    "I have an appoitment with the docter tomorrow.",
                    "The weathr is nice today, let's go for a picnick.",
                    "   I'm intersted in biologgy and study it at the univeristy.",
                    "He's a talanted musitian and plays the gitar very well."
                ]
            }

            # Create DataFrame
            occupation_df_eval = pd.DataFrame(data)

            # Lower case the data & strip whitespaces
            CleanData.text_typos.TextTypos.strip_and_lower_strings(occupation_df_eval).values
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

        Parameters:
            - df (pd.DataFrame): Input DataFrame containing columns to be converted.
            - features (list): List of column names to be converted to numeric type.

        Returns:
            pd.DataFrame: DataFrame with specified columns converted to numeric type.
        
        Example usage: 
        --------------
        .. code-block:: python

            # Import dependencies
            import numpy as np
            import pandas as pd
            import CleanData

            # Create a DataFrame
            s1 = pd.DataFrame(np.arange(1, 20, 1))

            # Enforce string values in the DataFrame columns 
            s1.iloc[15] = 'test'
            s1[1] = s1

            # Trasform the DataFrame columns back to numerical values
            CleanData.TextTypos.object_to_numeric(s1, [0, 1])

            s1
        """       

        for col in df[features].columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df[col]
    
    
    
    
    #* (3) Method 
    @classmethod
    def correct_word(cls, word: str) -> str:
        """Correct spelling of a word using SpellChecker.

        Parameters:
            - word (str): Input word to be corrected.

        Returns:
            str: Corrected version of the input word.
        
        Example usage:
        ---------------
        .. code-block:: python
        
            # Import dependencies
            import pandas as pd
            import random

            # List of occupations with intentional typos
            occupations_with_typos = [
                "Docter",
                "Engeneer",
                "Progrmmer",
                "Teahcer",
                "Dentest",
                "Writter",
                "Nurse",
                "Actrress",
                "Pilot",
                "Surgeon"
            ]

            # List of correct occupations
            correct_occupations = [
                "Doctor",
                "Engineer",
                "Programmer",
                "Teacher",
                "Dentist",
                "Writer",
                "Nurse",
                "Actress",
                "Pilot",
                "Surgeon"
            ]

            # Generate a dataframe with 100 records
            occupation_df_typos = pd.DataFrame({'Occupation': [random.choice(occupations_with_typos) for _ in range(100)]})
            occupation_df_correct = pd.DataFrame({'Occupation': [random.choice(correct_occupations) for _ in range(100)]})

            # Concatenate the dataframes
            occupation_df = pd.concat([occupation_df_typos, occupation_df_correct], ignore_index=True)

            # Display the dataframe
            occupation_df = occupation_df.sample(frac=1)

            # Apply correction to the entire dataframe
            corrected_df = occupation_df.applymap(CleanData.text_typos.TextTypos.correct_word)

            corrected_df

        """    
        spell = SpellChecker()
        return spell.correction(word)
    
    
    #* (4) Method 
    @classmethod
    def correct_sentence(cls, strings:str) -> str:
        """Correct spelling in a sentence using SpellChecker.

        Parameters:
            - strings (str): Input sentence to be corrected.

        Returns:
            str: Corrected version of the input sentence.
        
        Example usage:
        ---------------
        ..  code-block:: python

            # Import dependencies
            import pandas as pd
            import CleanData

            # sample data
            data = {
                'Text': [
                    "The brown fox jumps over the lazy dog.",
                    "She is an engeneer and work in a tech company.",
                    "I'm goign to the beech this weekend.",
                    "His favorit! color is purpel.",
                    "The concert was amazig, I reccomend it to everyone.",
                    "The resturant was ful of delicius food.",
                    "I have an appoitment with the docter tomorrow.",
                    "The weathr is nice today, let's go for a picnick.",
                    "I'm intersted in biologgy and study it at the univeristy.",
                    "He's a talanted musitian and plays the gitar very well."
                ]
            }

            # Create DataFrame
            occupation_df_eval = pd.DataFrame(data)

            # Correct the text typos
            occupation_df_eval['Text'] = occupation_df_eval['Text'].apply(CleanData.text_typos.TextTypos.correct_sentence)

            occupation_df_eval
        """     
        words = strings.split(' ')  # Split the string into words
        corrected_words = [cls.correct_word(word) for word in words]  # Apply correction to each word
        return ' '.join(corrected_words)  