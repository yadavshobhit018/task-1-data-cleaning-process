Task 1: Data Cleaning and Preprocessing

Objective

The objective of this task was to clean and preprocess a raw dataset by handling missing values, removing duplicate records, standardizing text values, converting date formats, renaming column headers, and correcting data types.

Dataset

* Customer Personality Analysis (Sample Dataset)

Tools Used

* Python
* Pandas
* Microsoft Excel

Data Cleaning Steps

* Identified missing values using isnull().
* Filled missing values in the Income column with the mean value.
* Removed duplicate records using drop_duplicates().
* Standardized country names (e.g., USA, U.S.A → United States).
* Standardized education values (e.g., graduation → Graduation).
* Converted all dates to DD-MM-YYYY format.
* Renamed column headers to lowercase with underscores.
* Corrected data types for numeric columns.

Files Included

Task-1-Data-Cleaning-Preprocessing/
│
├── data/
│   ├── Customer_Personality_Raw_Dataset.xlsx
│   └── Customer_Personality_Cleaned_Dataset.xlsx
│
├── code/
│   └── data_cleaning.py

├── README.md


Outcome

The dataset was cleaned and prepared for analysis by handling missing values, removing duplicates, standardizing text values, converting dates, and correcting data types.

Author

Shobhit Yadav