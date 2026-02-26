import pandas as pd
import matplotlib.pyplot as plt



# Load dataset

df = pd.read_csv("student_performance_ml.csv")

# Histogram of StudyHours
plt.hist(df["StudyHours"])
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")
plt.show()
