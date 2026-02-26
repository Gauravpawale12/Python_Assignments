import pandas as pd
import matplotlib.pyplot as plt



# Load dataset

df = pd.read_csv("student_performance_ml.csv")

# Scatter Plot: StudyHours vs PreviousScore

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"])
plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"])
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.show()