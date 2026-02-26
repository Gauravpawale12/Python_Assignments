import pandas as pd
import matplotlib.pyplot as plt



# Load dataset

df = pd.read_csv("student_performance_ml.csv")

# SleepHours vs FinalResult

df.groupby("FinalResult")["SleepHours"].mean().plot(kind="bar")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Average Sleep Hours")
plt.title("Sleep Hours vs Final Result")
plt.show()