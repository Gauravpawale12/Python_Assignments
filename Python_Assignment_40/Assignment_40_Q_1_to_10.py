# Import necessary libraries
import pandas as pd  # For data manipulation and reading CSV files
from sklearn.model_selection import train_test_split  # For splitting data into train and test sets
from sklearn.tree import DecisionTreeClassifier, plot_tree  # For Decision Tree model and visualization
from sklearn.metrics import accuracy_score  # For calculating accuracy
import matplotlib.pyplot as plt  # For plotting the decision tree

# Load the dataset from the CSV file
# Assuming the file is in the same directory; adjust path if needed
df = pd.read_csv('student_performance_ml.csv')

# Display the first few rows to understand the data (optional for debugging)
print(df.head())

# Define features (X) and target (y)
# Features are all columns except 'FinalResult'
X = df.drop('FinalResult', axis=1)
y = df['FinalResult']

# Split the data into training and testing sets (80/20 split)
# Using random_state=42 for reproducibility in most cases
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Question 1: Train the Decision Tree model and display feature importances
# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_
feature_names = X.columns

# Display importance scores
print("\nQuestion 1: Feature Importances")
for feature, importance in zip(feature_names, importances):
    print(f"{feature}: {importance}")

# Identify most and least contributing features
most_important = feature_names[importances.argmax()]
least_important = feature_names[importances.argmin()]
print(f"Most contributing feature: {most_important}")
print(f"Least contributing feature: {least_important}")

# Calculate original accuracy for comparison later
y_pred = model.predict(X_test)
original_accuracy = accuracy_score(y_test, y_pred)
print(f"Original Accuracy: {original_accuracy}")

# Question 2: Remove SleepHours, retrain, and compare accuracy
# Drop SleepHours from features
X_no_sleep = X.drop('SleepHours', axis=1)
X_train_no_sleep, X_test_no_sleep, _, _ = train_test_split(X_no_sleep, y, test_size=0.2, random_state=42)

# Retrain model
model_no_sleep = DecisionTreeClassifier(random_state=42)
model_no_sleep.fit(X_train_no_sleep, y_train)

# Predict and calculate new accuracy
y_pred_no_sleep = model_no_sleep.predict(X_test_no_sleep)
new_accuracy = accuracy_score(y_test, y_pred_no_sleep)
print("\nQuestion 2: After Removing SleepHours")
print(f"New Accuracy: {new_accuracy}")
print(f"Does it affect performance? {'Yes' if new_accuracy != original_accuracy else 'No'}")

# Question 3: Train using only StudyHours and Attendance
# Select only these two features
X_limited = X[['StudyHours', 'Attendance']]
X_train_limited, X_test_limited, _, _ = train_test_split(X_limited, y, test_size=0.2, random_state=42)

# Retrain model
model_limited = DecisionTreeClassifier(random_state=42)
model_limited.fit(X_train_limited, y_train)

# Predict and calculate accuracy
y_pred_limited = model_limited.predict(X_test_limited)
limited_accuracy = accuracy_score(y_test, y_pred_limited)
print("\nQuestion 3: Using Only StudyHours and Attendance")
print(f"Limited Accuracy: {limited_accuracy}")
print(f"Still performing well? {'Yes' if limited_accuracy >= original_accuracy else 'No'}")

# Question 4: Create new DataFrame for 5 new students and predict
# Hypothetical new students data (adjust values as needed)
new_students = pd.DataFrame({
    'StudyHours': [3.0, 5.0, 1.0, 7.0, 4.0],
    'Attendance': [70, 80, 60, 90, 75],
    'PreviousScore': [50, 60, 40, 70, 55],
    'AssignmentsCompleted': [4, 6, 2, 8, 5],
    'SleepHours': [6, 7, 5, 8, 6]
})

# Predict using the original model
predictions = model.predict(new_students)
print("\nQuestion 4: Predictions for New Students")
for i, pred in enumerate(predictions):
    result = 'Pass' if pred == 1 else 'Fail'
    print(f"Student {i+1}: {result}")

# Question 5: Manually calculate accuracy without accuracy_score
# Using original model's predictions
correct_predictions = sum(y_test == y_pred)  # Count matches
manual_accuracy = correct_predictions / len(y_test)
print("\nQuestion 5: Manual Accuracy")
print(f"Manual Accuracy: {manual_accuracy}")
print(f"Matches sklearn accuracy? {'Yes' if manual_accuracy == original_accuracy else 'No'}")

# Question 6: Identify misclassified students
# Find indices where y_test != y_pred
misclassified_indices = y_test != y_pred
misclassified = X_test[misclassified_indices]
print("\nQuestion 6: Misclassified Students")
print(f"Number misclassified: {misclassified.shape[0]}")
if not misclassified.empty:
    print(misclassified)
    # Observe patterns manually (e.g., low attendance common in fails)
else:
    print("No misclassifications.")

# Question 7: Train with different random_states and compare
random_states = [0, 10, 42]
accuracies = []
for rs in random_states:
    X_train_rs, X_test_rs, y_train_rs, y_test_rs = train_test_split(X, y, test_size=0.2, random_state=rs)
    model_rs = DecisionTreeClassifier(random_state=rs)
    model_rs.fit(X_train_rs, y_train_rs)
    y_pred_rs = model_rs.predict(X_test_rs)
    acc = accuracy_score(y_test_rs, y_pred_rs)
    accuracies.append(acc)
    print(f"\nQuestion 7: Accuracy with random_state={rs}: {acc}")

print("Results change? Yes, slightly due to different splits.")

# Question 8: Decision Tree Visualization
# Visualize the original trained tree
print("\nQuestion 8: Visualizing Decision Tree")
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=feature_names, class_names=['Fail', 'Pass'], filled=True)
plt.show()  # This will display the tree plot
# Root node is likely 'Attendance' as it has highest importance
# Selected first due to highest information gain

# Question 9: Create PerformanceIndex and retrain
# Add new column
df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

# New features including PerformanceIndex
X_with_index = df.drop('FinalResult', axis=1)
X_train_index, X_test_index, y_train_index, y_test_index = train_test_split(X_with_index, y, test_size=0.2, random_state=42)

# Retrain
model_index = DecisionTreeClassifier(random_state=42)
model_index.fit(X_train_index, y_train_index)

# Predict and accuracy
y_pred_index = model_index.predict(X_test_index)
index_accuracy = accuracy_score(y_test_index, y_pred_index)
print("\nQuestion 9: With PerformanceIndex")
print(f"New Accuracy: {index_accuracy}")
print(f"Improves? {'Yes' if index_accuracy > original_accuracy else 'No'}")

# Question 10: Train with max_depth=None
# max_depth=None allows unlimited depth, potential overfitting
model_deep = DecisionTreeClassifier(max_depth=None, random_state=42)
model_deep.fit(X_train, y_train)

# Calculate training and testing accuracy
y_train_pred = model_deep.predict(X_train)
train_acc = accuracy_score(y_train, y_train_pred)
y_test_pred = model_deep.predict(X_test)
test_acc = accuracy_score(y_test, y_test_pred)
print("\nQuestion 10: With max_depth=None")
print(f"Training Accuracy: {train_acc}")
print(f"Testing Accuracy: {test_acc}")
if train_acc == 1.0 and test_acc < 1.0:
    print("Overfitting: Model memorizes training data but generalizes poorly.")
else:
    print("No significant overfitting observed.")