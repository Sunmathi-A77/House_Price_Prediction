import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction App")

# --- User Inputs ---
area = st.number_input("Enter area (in sq.ft)", min_value=1.0, value=1000.0)
bedrooms = st.number_input("Number of bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Number of bathrooms", min_value=1, value=2)
stories = st.number_input("Number of stories", min_value=1, value=1)
parking = st.number_input("Number of parking spaces", min_value=0, value=1)

# Binary features with Yes/No dropdowns
mainroad = st.selectbox("Is the house on the main road?", ["No", "Yes"])
guestroom = st.selectbox("Has guest room?", ["No", "Yes"])
basement = st.selectbox("Has basement?", ["No", "Yes"])
hotwaterheating = st.selectbox("Has hot water heating?", ["No", "Yes"])
airconditioning = st.selectbox("Has air conditioning?", ["No", "Yes"])
prefarea = st.selectbox("Preferred area?", ["No", "Yes"])

# Furnishing status dropdown
furnishingstatus = st.selectbox("Furnishing status", ["furnished", "semi-furnished", "unfurnished"])

# --- Predict Button ---
if st.button("Predict House Price"):
    # Log transform numeric features safely
    area_log = np.log(area if area > 0 else 1)
    bathrooms_log = np.log(bathrooms if bathrooms > 0 else 1)
    stories_log = np.log(stories if stories > 0 else 1)
    parking_log = np.log(parking if parking > 0 else 1)

    # Convert Yes/No to 1/0
    mainroad_val = 1 if mainroad == "Yes" else 0
    guestroom_val = 1 if guestroom == "Yes" else 0
    basement_val = 1 if basement == "Yes" else 0
    hotwaterheating_val = 1 if hotwaterheating == "Yes" else 0
    airconditioning_val = 1 if airconditioning == "Yes" else 0
    prefarea_val = 1 if prefarea == "Yes" else 0

    # One-hot encode furnishing status
    furnishing_furnished = 1 if furnishingstatus == "furnished" else 0
    furnishing_semi = 1 if furnishingstatus == "semi-furnished" else 0
    furnishing_unfurnished = 1 if furnishingstatus == "unfurnished" else 0

    # Prepare feature array
    features = np.array([[area_log, bedrooms, bathrooms_log, stories_log,
                          mainroad_val, guestroom_val, basement_val,
                          hotwaterheating_val, airconditioning_val,
                          parking_log, prefarea_val,
                          furnishing_furnished, furnishing_semi, furnishing_unfurnished]])

    # Predict log(price) and convert back
    log_price = model.predict(features)
    predicted_price = np.exp(log_price)

    st.success(f"🏠 Estimated House Price: ₹{predicted_price[0]:,.2f}")
