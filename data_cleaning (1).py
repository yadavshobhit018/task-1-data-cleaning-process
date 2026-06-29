
import pandas as pd

# Load the raw dataset
df = pd.read_excel("Customer_Personality_Raw_Dataset.xlsx")

# -------------------------------
# 1. Check missing values
# -------------------------------
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values in Income with the column mean
df["Income"] = df["Income"].fillna(df["Income"].mean())

# -------------------------------
# 2. Remove duplicate rows
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# 3. Standardize text values
# -------------------------------

# Education
df["Education"] = df["Education"].replace({
    "graduation": "Graduation"
})

# Country
df["Country"] = df["Country"].replace({
    "USA": "United States",
    "U.S.A": "United States",
    "United states": "United States",
    "india": "India",
    "canada": "Canada",
    "UK": "United Kingdom"
})

# -------------------------------
# 4. Convert date format
# -------------------------------
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    dayfirst=True,
    errors="coerce"
)

df["Dt_Customer"] = df["Dt_Customer"].dt.strftime("%d-%m-%Y")

# -------------------------------
# 5. Rename column headers
# -------------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# -------------------------------
# 6. Fix data types
# -------------------------------
int_columns = [
    "id",
    "year_birth",
    "kidhome",
    "teenhome",
    "recency",
    "mntwines",
    "mntfruits"
]

for col in int_columns:
    df[col] = df[col].astype(int)

df["income"] = df["income"].astype(float)

# -------------------------------
# Save cleaned dataset
# -------------------------------
df.to_excel("Customer_Personality_Cleaned_Dataset.xlsx", index=False)

print("\nData cleaning completed successfully.")
print("Cleaned dataset saved as Customer_Personality_Cleaned_Dataset.xlsx")
