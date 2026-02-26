import pandas as pd
import matplotlib.pyplot as plt



# Load dataset

df = pd.read_csv("student_performance_ml.csv")

# Boxplot for Attendance
plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.ylabel("Attendance Percentage")
plt.show()