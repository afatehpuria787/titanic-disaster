print("Importing relevant packages")

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Importing the training dataset")
train_df = pd.read_csv('src/data/train.csv')

print("Reviewing the dataset")
train_df.head()

print("Reviewing descriptive stats")
train_df.describe()
print("Understanding how many NULL values we have")
train_df.isna().sum()

print("Removing rows where Age is NULL")
train_df = train_df.dropna(subset=['Age']) #Dropping all rows where Age is NULL

print("Creating a dummy variable for sex")
train_df['Sex_dummy'] = np.where(train_df['Sex'] == 'male', 0, 1) #Creating a dummy variable for sex

print("Defining Sex_dummy, Age, and Pclass as independent and Survived as our dependent variables")
X_train = train_df[['Sex_dummy', 'Age','Pclass']]  # independent variables are sex, age, and ticket class
y_train = train_df['Survived']             # dependent variable

print("Making model")
model = LogisticRegression()
model.fit(X_train, y_train)

print("Retrieving and printing training accuracy of training data")
train_accuracy = model.score(X_train, y_train)
print("Training Accuracy:", train_accuracy)

print("Repeat cleaning, defining independent variables step for test data")
test_df = pd.read_csv('src/data/test.csv') #Importing the test dataset
#Data Cleaning
test_df = test_df.dropna(subset=['Age']) #Dropping all rows where Age is NULL
test_df['Sex_dummy'] = np.where(test_df['Sex'] == 'male', 0, 1) #Creating a dummy variable for sex
#Define independent variables
X_test = test_df[['Sex_dummy', 'Age','Pclass']]  # independent variables are sex, age, and ticket class

print("Applying the logistic regression model created above to test data")
y_pred = model.predict(X_test) #Applying the logistic regression model to our test data

print("Saving predicted Passenger ID and Survived (predictions made on test data) to an external dataframe called output_python")
output_python = pd.DataFrame({
    'PassengerId': test_df['PassengerId'],
    'Survived': y_pred
})
output_python.to_csv('output_python.csv', index=False)