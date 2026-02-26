import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")


# Average StudyHours for Pass and Fail students
study_analysis = df.groupby("FinalResult")["StudyHours"].mean()
print("Average Study Hours based on Result:\n", study_analysis)

# Average Attendance for Pass and Fail students
attendance_analysis = df.groupby("FinalResult")["Attendance"].mean()
print("\nAverage Attendance based on Result:\n", attendance_analysis)