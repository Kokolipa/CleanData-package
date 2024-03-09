from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="CleanData",
    version="0.0.10",
    description="A comprehensive and scalable Python Library for daily cleansing operations.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kokolipa/CleanData-package/tree/CleanData_main", 
    author="Kokolipa",
    author_email="galbeeri1@gmail.com",
    license="MIT", 
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10.13",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy>=1.23.5",
        "scikit-learn==1.2.2",
        "pyod==1.1.2",
        "pyspellchecker >= 0.8.1",
        "transformers >= 4.38.2"],  
    python_requires=">=3.10",
)
