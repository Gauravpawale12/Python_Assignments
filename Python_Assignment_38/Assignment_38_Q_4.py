import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")


# Distribution of FinalResult (Pass / Fail)

result_counts = df["FinalResult"].value_counts()
result_percent = df["FinalResult"].value_counts(normalize=True) * 100

print("Result Count:\n", result_counts)
print("\nResult Percentage:\n", result_percent)

if abs(result_percent[1] - result_percent[0]) < 10:
    print("\nDataset is Balanced")
else:
    print("\nDataset is Imbalanced")