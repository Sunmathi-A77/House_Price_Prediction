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

Skewness Analysis:

Price, area, bathrooms, stories, and parking were moderately right-skewed.

Bedrooms were nearly symmetric.

Visualized distributions using histograms.

<img width="831" height="682" alt="image" src="https://github.com/user-attachments/assets/6bc174f4-7940-45c5-bdc6-6890e84395a9" />

Correlation Analysis:

Computed correlations between numeric features and price.

Top features correlated with price: area, bathrooms, stories, parking, airconditioning.

Visualized correlations using a heatmap.

<img width="546" height="434" alt="image" src="https://github.com/user-attachments/assets/58e3e128-802c-40d2-a41b-e8c82570d957" />

Categorical Columns Analysis:

Reviewed count of features like mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus.

## 3. Data Preprocessing

Converted categorical features to numeric: yes/no → 1/0.

One-hot encoded furnishingstatus.

Log-transformed skewed numeric features: price, area, bathrooms, stories, parking to reduce skewness.

Checked skewness after transformation to confirm normalization.

Visualized distributions using histograms.

<img width="1189" height="789" alt="image" src="https://github.com/user-attachments/assets/494a7875-6244-468a-aa73-8943e13ce1a5" />

Detected outliers using IQR method.

Visualized numeric columns with boxplots post log-transform.

<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/4e9913dd-ed45-4ea5-9670-53cb8ce8785a" />

Removed outliers using IQR and Check how many outliers remain

## 4. Feature Selection

Selected features for modeling: area, bedrooms, bathrooms, stories, parking, and encoded categorical columns.

Target variable: price

## 5. Data Splitting

Split dataset into training (80%) and testing (20%) sets.

## 6. Model Training

Trained a Multiple Linear Regression model using all numeric and encoded categorical features.

Evaluated model coefficients to understand feature impact on house price.

## 7. Model Evaluation

Predicted house prices on the test set.

Calculated metrics:

R² Score: Indicates how well the model explains variance in the target.

Mean Squared Error (MSE): Measures average prediction error.

Root Mean Squared Error (RMSE): Square root of MSE for interpretation in original units.

Residual Analysis:

Plotted histogram of residuals to check distribution.

<img width="576" height="455" alt="image" src="https://github.com/user-attachments/assets/010a0193-d18f-4493-9cee-c4d8f4be73f1" />

Scatter plot of residuals vs predicted values to confirm randomness.

<img width="580" height="432" alt="image" src="https://github.com/user-attachments/assets/83205c30-9549-421f-9169-4782637b5cb0" />

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

Predicted House Price: ₹5,256,840.70

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/cae89314-53e3-4bd7-b628-6c0b4e887c4a" />

## 9. Visualizations

Histograms: Show distributions of numeric features before and after log transformation.

Boxplots: Highlight outliers in numeric features.

Correlation Heatmap: Shows relationships between features and target.

Residual Plots: Ensure model assumptions are satisfied.

Scatter Plot of Actual vs Predicted Prices: Highlights prediction accuracy.

## 10. Results

Base Price (Intercept): ₹11.80

Predicted Price for 2500 sq.ft, 3 bedrooms, 2 bathrooms: ₹5,256,840.70

R² Score: 0.725

MSE: 0.046

RMSE: 0.215

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
