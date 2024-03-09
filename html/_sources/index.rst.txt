.. CleanData Documentation documentation master file, created by
   sphinx-quickstart on Mon Mar  4 22:18:12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CleanData Documentation! 
===================================================

**Cleandata** is an easy to use Python library for data cleansing operations 
with the main focus on reducing the steps required on each sub-process included in the data pre-processing step:

- Reducing memory consumption for dataset with decreased byte sizes.
- Considering MAR, MCAR, and MNAR cases to treat case-specific NA values.
- Treating and dropping duplicated values.
- Using scientific methods to treat anomalies.
- Treating text typos.
- Using AI state-of-the-art models for Table Question Answering purposes.

Visit the `GitHub reponsitory <https://github.com/Kokolipa/CleanData-package/tree/CleanData_main>`_ for more information.

Library Requirements:
----------------
=================  =====================
**Library**            **Version**
=================  =====================
NumPy                   >=1.23.5
scikit-learn            ==1.2.2
pyod                    ==1.1.2
pyspellchecker          >=0.8.1
transformers            >=4.38.2
=================  =====================



Installation
------------
To use CleanData, first install it using pip:

.. code-block:: console

   (.venv) $ pip install CleanData


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
