# CleanData
-----------------

##  CleanData: Powerful Python data preprocessing library with scientific approach
Insert clickable quick links here 


## What is it?

Cleandata is an easy to use Python library for data cleansing operations with the main focus on reducing the steps required on each sub-process included in the data pre-processing step with scientific approach:
1. Reducing memory consumption for dataset with decreased byte sizes.
2. Considering MAR, MCAR, and MNAR cases to treat case-specific NA values.
3. Treating and dropping duplicated values.
4. Using scientific methods to treat anomalies.
5. Treating text typos.
6. Using AI state-of-the-art models (**TAPAS**) for Table Question Answering purposes to enhance the workflow and reduce the overall time consumption for data exploration.


## The IDEA
Enabling users to improve code readability and efficiency by leveraging a distinctive module that allows for the creation of pipelines. These pipelines encapsulate the sub-steps of the cleaning process, including best practices, and map each step to its corresponding action within a single code block. 
``` python
import CleanData
data = (
    data.pipe(CleanData.Memory.optimise_mem),
    data.pipe(CleanData.TreatNA.drop_complete_case_na),
    data.pipe(CleanData.FindTreatDuplicates.drop_duplicates),
    # ... additional steps to be included in the funnel 
    )
```


## Table of Contents

- [Modules & Functions Included](#modules--functions-included)
- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [Installation from sources](#installation-from-sources)
- [License](#license)
- [Documentation](#documentation)


## Modules & Functions Included
- Memory module: Significantly reduce memory consumption to the smallest corresponding byte size of dataset with one simple function. 
- Treat_NA mudole:
    - **IdentifyNAs**:  Identify rows containing missing values in a DataFrame not taking into account MAR, MNAR, and MCAR (additional information what those are can be found [HERE](https://www.kaggle.com/code/prashant111/a-reference-guide-to-feature-engineering-methods), [and HERE](https://www.bookdown.org/rwnahhas/RMPH/mi-mechanisms.html). 
    - **complete_case_na**: Filter DataFrame to retain rows with complete case or edge case missing values.
    - **drop_complete_case_na**:  Drop rows with complete case missing values from a DataFrame.
    - **DataImpute**: Apply univariate data imputation for numerical & categorical strategies (suitable for MCAR cases).
    - **MNAR**: Missing of values is not at random (MNAR) if their being missing depends on information not recorded in the dataset (This function will drop all corresponsing NA values from the dependent variables based on the Independent variable/s). 
    - **logistic_regression_MAR_identifier**: Identify Missing at Random (MAR) cases using Logistic Regression.

- find_treat_duplicates module:
    - **find_duplicates**: Idenfify duplicated values in DataFrame
    - **drop_duplicates**: Drop duplicated values in DataFrame. 

- TextTypos module:
    - **strip_and_lower_strings**: Strip whitespace and convert strings to lowercase in DataFrame.
    - **object_to_numeric**: Convert specified columns from object type to numeric type.
    - **correct_word**: Correct spelling of a word (singular words in the `DataFrame`) using SpellChecker (this function consider special characters as well).
    - **correct_sentence**: Correct spelling in a sentence using SpellChecker (this function should be consider `for cases where a feature in the DataFrame contain more the singular word`).

- Anomalies module:
    - **find_date_anomalies**: Find anomalies in date data (when `month` contain less then 28 days / when `year` contain less then 365 days).
    - **nonlinear_outliers_influencers_knn**: Detects outliers in a dataset based on nonlinear methods and KNN.
    - **linear_outliers_influencers**: This function align for linear datasets to explore outliers using Cook's D (distance based evaluation).

- QA module 
    - **Ask**: Asks a natural language question about a given pandas DataFrame and prints the answer.



## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/Kokolipa/CleanData-package

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/pandas) and on [Conda](https://docs.conda.io/en/latest/).
TODO: Fix the links after deployment

```sh
# conda
conda install -c conda-forge CleanData
```

```sh
# or PyPI
pip install CleanData
```


## Dependencies

| Package           | Version   |
|-------------------|-----------|
| numpy             | >=1.23.5  |
| scikit-learn      | ==1.2.2   |
| pyod              | ==1.1.2   |
| pyspellchecker    | >=0.8.1   |
| transformers      | >=4.38.2  |


## License
[MIT](https://github.com/Kokolipa/CleanData-package/blob/CleanData_main/LICENSE)

## Documentation
TODO: Include the link to the documentation using GitHub Pages.
<!-- The official documentation is hosted on [GitHub Pages](). -->




