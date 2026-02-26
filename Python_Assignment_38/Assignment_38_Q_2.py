import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")


# Count Pass & Fail Students
total_students = df.shape[0]
passed = df[df["FinalResult"] == 1].shape[0]
failed = df[df["FinalResult"] == 0].shape[0]

print("Total Students:", total_students)
print("Passed Students:", passed)
print("Failed Students:", failed)