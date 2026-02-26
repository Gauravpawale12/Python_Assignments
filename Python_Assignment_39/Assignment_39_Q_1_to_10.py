# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------
df = pd.read_csv("student_performance_ml.csv")

# Split features and target
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

# --------------------------------------------------
# 2. Train-Test Split
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --------------------------------------------------
# 3. Train Decision Tree Model
# --------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# --------------------------------------------------
# 4. Prediction on Test Data
# --------------------------------------------------
y_pred = model.predict(X_test)

print("Actual Values:\n", y_test.values)
print("Predicted Values:\n", y_pred)

# --------------------------------------------------
# 5. Accuracy Calculation
# --------------------------------------------------
accuracy = accuracy_score(y_test, y_pred) * 100
print("\nModel Accuracy:", accuracy, "%")

# --------------------------------------------------
# 6. Confusion Matrix
# --------------------------------------------------
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

"""
Confusion Matrix Terms:
True Positive  : Correctly predicted Pass
True Negative  : Correctly predicted Fail
False Positive : Predicted Pass but actually Fail
False Negative : Predicted Fail but actually Pass
"""

# --------------------------------------------------
# 7. Training vs Testing Accuracy (Overfitting Check)
# --------------------------------------------------
train_accuracy = accuracy_score(y_train, model.predict(X_train)) * 100
test_accuracy = accuracy_score(y_test, y_pred) * 100

print("\nTraining Accuracy:", train_accuracy, "%")
print("Testing Accuracy:", test_accuracy, "%")

if train_accuracy > test_accuracy:
    print("Model may be overfitting")
elif train_accuracy < test_accuracy:
    print("Model may be underfitting")
else:
    print("Model is well balanced")

# --------------------------------------------------
# 8. Decision Tree with Different max_depth
# --------------------------------------------------
for depth in [1, 3, None]:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    pred = dt.predict(X_test)
    acc = accuracy_score(y_test, pred) * 100
    print(f"Testing Accuracy with max_depth={depth} : {acc}%")

# --------------------------------------------------
# 9. Prediction for New Student
# --------------------------------------------------
new_student = [[6, 85, 66, 7, 7]]

result = model.predict(new_student)

if result[0] == 1:
    print("\nPrediction: Student will PASS")
else:
    print("\nPrediction: Student will FAIL")

# --------------------------------------------------
# Final Conclusion
# --------------------------------------------------
print("\nConclusion:")
print("Decision Tree model can effectively predict student performance.")
print("Proper tuning of max_depth helps avoid overfitting.")