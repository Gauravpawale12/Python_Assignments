import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Display first 5 records
print("First 5 Records:\n", df.head())

# Display last 5 records
print("\nLast 5 Records:\n", df.tail())

# Total rows and columns
print("\nShape of Dataset:", df.shape)

# Column names
print("\nColumn Names:", df.columns.tolist())

# Data types
print("\nData Types:\n", df.dtypes)