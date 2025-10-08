# House Price Prediction

## Project Overview

The goal of this project is to predict house prices based on features such as area, number of bedrooms, and number of bathrooms. We use Multiple Linear Regression to model the relationship between these features and the house price.

## Dataset

Source: Kaggle Housing Prices Dataset (Link - https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

## Features:

area: Size of the house in square feet

bedrooms: Number of bedrooms

bathrooms: Number of bathrooms

price: Target variable (house price)

## Steps Performed

## Data Loading and Exploration

Loaded dataset using Pandas

Checked the first few rows

## Exploratory Data Analysis (EDA)

Checked data types, summary statistics, and missing values.

Converted categorical features to numeric (yes/no → 1/0, furnishingstatus → 1/2/3).

Analyzed correlations:

Top features correlated with price: area, bathrooms, stories, parking, airconditioning.

Visualized using heatmap.

Examined skewness:

price, area, bathrooms, stories, parking → moderately right-skewed.

bedrooms → slightly skewed (Symmetric)

Applied log transformation to reduce skewness (price_log, area_log, etc.).

Histograms used to visualize distributions.

Detect outliers using IQR method - Only minor outliers detected in price_log and area_log.

## Feature Selection

Selected features: area, bedrooms, bathrooms

Target: price

## Data Splitting

Split the dataset into training (80%) and testing (20%) sets

## Modeling

Trained a Multiple Linear Regression model using sklearn.linear_model.LinearRegression

## Evaluation

Predicted prices on the test set

## Calculated:

R² Score: Measures how well the model explains variance

Mean Squared Error (MSE): Measures prediction error

## Prediction

Predicted price for a new house with:

Area = 2500 sq.ft

Bedrooms = 3

Bathrooms = 2

## Base Price

The intercept of the model represents the base price when all features are zero.

## Visualization

Actual vs Predicted Prices Scatter Plot - Shows how close predicted prices are to actual prices.

<img width="536" height="470" alt="image" src="https://github.com/user-attachments/assets/700ea4a0-1afd-46ff-9370-499953a46f43" />

Blue points represent actual vs predicted house prices.

Red line represents perfect predictions (predicted = actual).

## Results

Base Price (Intercept):  ₹59485.38

Predicted Price for 2500 sq.ft, 3 bed, 2 bath: ₹₹4848384.07

R² Score: 0.456

MSE: 2750040479309.052

## Conclusion

The linear regression model predicts house prices based on area, bedrooms, and bathrooms.

The scatter plot helps visualize how close predictions are to actual prices.

Base price (intercept) represents the theoretical price when all features are zero.

## Technologies & Libraries Used

Python – Programming language

Pandas – Data manipulation and analysis

Scikit-learn – Machine learning (Linear Regression, train/test split, metrics)

Matplotlib – Data visualization (scatter plot)

Numpy - Numerical computations and array operations
