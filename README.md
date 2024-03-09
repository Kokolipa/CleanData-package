# CleanData
-----------------

# pandas: powerful Python data analysis toolkit
Insert clickable quick links here 


## What is it?

Cleandata is an easy to use Python library for data cleansing operations with the main focus on reducing the steps required on each sub-process included in the data pre-processing step with scientific approach:
1. Reducing memory consumption for dataset with decreased byte sizes.
2. Considering MAR, MCAR, and MNAR cases to treat case-specific NA values.
3. Treating and dropping duplicated values.
4. Using scientific methods to treat anomalies.
5. Treating text typos.
6. Using AI state-of-the-art models for Table Question Answering purposes.



## Table of Contents

- [Main Features](#main-features)
- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [Installation from sources](#installation-from-sources)
- [License](#license)
- [Documentation](#documentation)


## Main Features
Here are just a few of the things that pandas does well:

  - Easy handling of [**missing data**][missing-data] (represented as
    `NaN`, `NA`, or `NaT`) in floating point as well as non-floating point data
  - Size mutability: columns can be [**inserted and
    deleted**][insertion-deletion] from DataFrame and higher dimensional
    objects
  - Automatic and explicit [**data alignment**][alignment]: objects can
    be explicitly aligned to a set of labels, or the user can simply
    ignore the labels and let `Series`, `DataFrame`, etc. automatically
    align the data for you in computations
  - Powerful, flexible [**group by**][groupby] functionality to perform
    split-apply-combine operations on data sets, for both aggregating
    and transforming data
  - Make it [**easy to convert**][conversion] ragged,
    differently-indexed data in other Python and NumPy data structures
    into DataFrame objects
  - Intelligent label-based [**slicing**][slicing], [**fancy
    indexing**][fancy-indexing], and [**subsetting**][subsetting] of
    large data sets
  - Intuitive [**merging**][merging] and [**joining**][joining] data
    sets
  - Flexible [**reshaping**][reshape] and [**pivoting**][pivot-table] of
    data sets
  - [**Hierarchical**][mi] labeling of axes (possible to have multiple
    labels per tick)
  - Robust IO tools for loading data from [**flat files**][flat-files]
    (CSV and delimited), [**Excel files**][excel], [**databases**][db],
    and saving/loading data from the ultrafast [**HDF5 format**][hdfstore]
  - [**Time series**][timeseries]-specific functionality: date range
    generation and frequency conversion, moving window statistics,
    date shifting and lagging


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




