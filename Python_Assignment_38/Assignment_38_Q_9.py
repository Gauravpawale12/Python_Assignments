import pandas as pd
import matplotlib.pyplot as plt



# Load dataset

df = pd.read_csv("student_performance_ml.csv")

# AssignmentsCompleted vs FinalResult
df.groupby("FinalResult")["AssignmentsCompleted"].mean().plot(kind="bar")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Average Assignments Completed")
plt.title("Assignments Completed vs Result")
plt.show()