# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hg4w1rO2AyFcyLY4oOGSu9nKtljoEcd0
"""

# STEP 1: Upload the CSV
from google.colab import files
uploaded = files.upload()

# Task 3: Linear Regression – House Price Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("Housing.csv")  # Check your file name
df = pd.get_dummies(df, drop_first=True)
print("Missing values:\n", df.isnull().sum())
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
print("Intercept:", model.intercept_)
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test, y=y_pred, color='darkorange')
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='blue')
plt.grid(True)
plt.show()
