# NumPy-data-integrity-engine
A high-performance data validation and transformation engine built with NumPy to clean and standardize  datasets.

Build a data validation & transformation engine that uses Numpy as the core processor for large tabular datasets. It will check for:

missing values,
outliers,
inconsistent types,
duplicate rows,
normalization,
transformations,
and provide a secure cleaned output.

Think of it like a mini data pipeline — but entirely powered by Numpy arrays, not just Pandas.

project1/               
│
├── numpy_data_integrity_engine/      
│   ├── data/
│   └── sample_data.csv                ← Your input data
|   |── eng_venv/                      ← Your virtual environment
│   └── engine/
│       ├── __init__.py                ← Makes it a package
|       ├── main.py                    ← Your main entry point
│       ├── loader.py
│       ├── validator.py
│       ├── transformer.py
│       └── utils.py
│
├── tests/                             ← Unit test files
│   ├── test_validator.py
│   ├── test_transformer.py
│
│
├── requirements.txt                   ← List of dependencies
├── README.md                          ← Project overview
├── only_for_my_ref.txt                ← (Optional personal notes)

# 🧼 NumPy Data Integrity Engine (NPDIE)

A blazing-fast, Numpy-centric engine for validating and transforming tabular datasets. Designed to showcase deep Numpy skills while providing practical utility in data science and engineering workflows.

## Features
- Missing value detection and handling
- Outlier detection using Z-score
- Min-Max normalization
- Type-safe operations
- Built with a modular, testable architecture

  File	                Purpose
loader.py	          Loads data (e.g. reads CSV into NumPy arrays).
validator.py	      Checks data integrity (missing values, ranges, etc.).
transformer.py	    Applies data transformations.
test_validator.py	  Tests the validator code.
