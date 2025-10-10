import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

# Load dataset
data = pd.read_csv("House_Price.csv")

# Convert yes/no columns to 1/0
binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for col in binary_cols:
    data[col] = data[col].map({'yes': 1, 'no': 0})

# Apply log transformation to skewed numeric columns safely
skewed_cols = ['price', 'area', 'bathrooms', 'stories', 'parking']
for col in skewed_cols:
    data[col] = data[col].replace(0, 1)  # avoid log(0)
    data[col] = np.log(data[col])

# One-hot encode furnishingstatus column
furnishing_dummies = pd.get_dummies(data['furnishingstatus'], prefix='furnishingstatus')
data = pd.concat([data, furnishing_dummies], axis=1)

# Define features and target
X = data[['area','bedrooms','bathrooms','stories','mainroad','guestroom','basement',
          'hotwaterheating','airconditioning','parking','prefarea'] + list(furnishing_dummies.columns)]
y = data['price']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved successfully as house_price_model.pkl")
