import pandas as pd  # noqa: F401
from transformers import (AutoModelForTableQuestionAnswering,  # noqa: F401
                          AutoTokenizer, pipeline)

from ._utils import get_time


class QA:
    # Load model & tokenizer

    model = 'google/tapas-base-finetuned-wtq'
    tapas_model = AutoModelForTableQuestionAnswering.from_pretrained(model)
    tapas_tokenizer = AutoTokenizer.from_pretrained(model)
    
    # Initializing pipeline
    nlp = pipeline('table-question-answering', model=tapas_model, tokenizer=tapas_tokenizer)

    def __init__(self, data):
        self.data = data

    @classmethod
    @get_time
    def Ask(cls, query: str, data: pd.DataFrame):
        """
            Asks a natural language question about a given pandas DataFrame and prints the answer.

            This method utilizes a pre-trained TAPAS model for table-based question answering to interpret the data
            in the DataFrame and provide answers to questions posed in natural language. It's designed to work with
            data that can be represented in tabular form and can handle a wide range of question types, including
            aggregations, comparisons, and single-row lookups.

            Example usage:
                Ask('Which city has the highest download speed?', data)

            Parameters:
                - query (str): The natural language question to be asked about the data.
                - data (pd.DataFrame): The pandas DataFrame containing the data to be queried. 
                
            Returns:
                None. The answer is printed out. 
            
            Example usage: 
            --------------
            .. code-block:: python

                # Import Depenencies
                import CleanData
                import pandas as pd


                # Create a query
                query = "What is the highest in the hoursperweek feature in my data?"

                # Apply the Ask method on your DataFrame
                CleanData.QA.Ask(query, income)

            Note: **I am currently working to scale this method, currently can be applied on max 256 records at a time**
        """

        # Applying a string type for data
        data = data.astype(str)
        
        print(query)
        print('>>>>>')
        result = cls.nlp({'table': data, 'query': query})
        answer = result['cells']
        print(answer)

        
