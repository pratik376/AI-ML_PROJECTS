import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Bangalore House Price Predictions")

model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
columns = pickle.load(open('columns.pickle', 'rb'))
columns = list(columns)
locations = columns[3:]

st.title("🏠 Bangalore House Price Prediction App")
st.markdown("Enter the details below to estimate the house price in **Lakhs INR**.")

sqft = st.selectbox("Total Square Feet", ["Select Total Square Feet"] + [str(i) for i in range(300, 10001, 50)])
bhk = st.selectbox("BHK (Bedrooms)", ["Select BHK"] + [str(i) for i in range(1, 11)])
bath = st.selectbox("Bathrooms", ["Select Bathrooms"] + [str(i) for i in range(1, 11)])
location = st.selectbox("Location", ["Select a location"] + list(locations))

def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location in columns:
        loc_index = columns.index(location)
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)

if st.button("Predict Price"):
    if sqft != "Select Total Square Feet" and bhk != "Select BHK" and bath != "Select Bathrooms" and location != "Select a location":
        try:
            sqft_val = float(sqft)
            bhk_val = int(bhk)
            bath_val = int(bath)
            price = predict_price(location, sqft_val, bath_val, bhk_val)
            st.success(f"💰 Estimated Price: {price} Lakhs INR")
        except Exception:
            st.error("Please enter valid inputs.")
    else:
        st.warning("⚠️ Please select Total Square Feet, BHK, Bathrooms and Location before predicting.")
