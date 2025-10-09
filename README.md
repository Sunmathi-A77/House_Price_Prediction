# 🏠 House Price Prediction Project

## Project Overview

TThis project predicts house prices based on features such as area, bedrooms, bathrooms, stories, parking, and other amenities. A Multiple Linear Regression model is trained on the dataset after preprocessing, handling skewness, outliers, and encoding categorical variables.

## Dataset

Source: Kaggle Housing Prices Dataset (Link - https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

## Features:

price: House price (target)

area: Area of the house (sq.ft)

bedrooms: Number of bedrooms

bathrooms: Number of bathrooms

stories: Number of stories

mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea: Categorical yes/no features

parking: Number of parking spots

furnishingstatus: Furnishing status (furnished, semi-furnished, unfurnished)

## Steps Performed

## 1. Data Loading and Exploration

Loaded the dataset and checked the first few rows.

Reviewed data types and summary statistics to understand feature distributions and missing values.

## 2. Exploratory Data Analysis (EDA)

Numeric Columns Analysis:

Checked numeric features: price, area, bedrooms, bathrooms, stories, parking.

Detected outliers using the IQR method before log transformation.

Visualized distributions using boxplots.

Insert boxplot image of numeric columns before log transformation here

Skewness Analysis:

Price, area, bathrooms, stories, and parking were moderately right-skewed.

Bedrooms were nearly symmetric.

Visualized distributions using histograms.

Insert histograms of numeric columns before log transformation here

Correlation Analysis:

Computed correlations between numeric features and price.

Top features correlated with price: area, bathrooms, stories, parking, airconditioning.

Visualized correlations using a heatmap.

Insert correlation heatmap here

Categorical Columns Analysis:

Reviewed distributions of features like mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus.

Insert bar charts for categorical columns here

## 3. Data Preprocessing

Converted categorical features to numeric: yes/no → 1/0.

One-hot encoded furnishingstatus.

Log-transformed skewed numeric features: price, area, bathrooms, stories, parking to reduce skewness.

Checked skewness after transformation to confirm normalization.

Visualized distributions using histograms.

Insert histograms of numeric columns after log transformation here

Detected outliers after log transformation.

Visualized numeric columns with boxplots post log-transform.

Insert boxplots of numeric columns after log transformation here

## 4. Feature Selection

Selected features for modeling: area, bedrooms, bathrooms, stories, parking, and encoded categorical columns.

Target variable: price

## 5. Data Splitting

Split dataset into training (80%) and testing (20%) sets.

## 6. Model Training

Trained a Multiple Linear Regression model using all numeric and encoded categorical features.

Evaluated model coefficients to understand feature impact on house price.

Insert table or image of feature coefficients here

## 7. Model Evaluation

Predicted house prices on the test set.

Calculated metrics:

R² Score: Indicates how well the model explains variance in the target.

Mean Squared Error (MSE): Measures average prediction error.

Root Mean Squared Error (RMSE): Square root of MSE for interpretation in original units.

Residual Analysis:

Plotted histogram of residuals to check distribution.

Scatter plot of residuals vs predicted values to confirm randomness.

Insert residual plots here

Base Price (Intercept): Represents the theoretical price when all features are zero.

## 8. Prediction

Predicted price for a new house with:

Area: 2500 sq.ft

Bedrooms: 3

Bathrooms: 2

Stories: 2

Parking: 1

Main Road: Yes

Guest Room: No

Basement: No

Hot Water Heating: No

Air Conditioning: Yes

Preferred Area: Yes

Furnishing: Furnished

Converted the predicted log-price back to the original scale to get the final price.

Predicted House Price: ₹X,XXX,XXX.XX

Insert prediction visualization or highlight image here

## 9. Visualizations

Histograms: Show distributions of numeric features before and after log transformation.

Boxplots: Highlight outliers in numeric features.

Correlation Heatmap: Shows relationships between features and target.

Residual Plots: Ensure model assumptions are satisfied.

Scatter Plot of Actual vs Predicted Prices: Highlights prediction accuracy.

Insert respective images in this section

## 10. Results

Base Price (Intercept): ₹11.91

Predicted Price for 2500 sq.ft, 3 bed, 2 bath: ₹5,435,800.86

R² Score: 0.682

MSE: 0.061

RMSE: 0.248

## 11. Conclusion

The linear regression model effectively predicts house prices based on area, bedrooms, bathrooms, and other features.

Log transformation reduced skewness and minimized outliers, improving model stability.

Residual and scatter plots confirm good prediction accuracy.

Base price (intercept) provides a theoretical starting value for houses with minimal features.

## 12. Technologies & Libraries Used

Python – Programming Language

Pandas – Data manipulation and analysis

NumPy – Numerical computations

Scikit-learn – Machine Learning (Linear Regression, train/test split, metrics)

Matplotlib – Data visualization (histograms, scatter plots)

Seaborn – Data visualization (heatmaps, distribution plots)