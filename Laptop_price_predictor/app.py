import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Laptop Price Prediction", layout="wide")

st.title("💻 Laptop Price Prediction")

# Load your data and pipeline
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.sidebar.header("Select Laptop Specifications")

company = st.sidebar.selectbox("Select Company", df['Company'].unique())
type_name = st.sidebar.selectbox("Select TypeName", df['TypeName'].unique())
ram = st.sidebar.selectbox("Select RAM (GB)", sorted(df['Ram'].unique()))
weight = st.sidebar.number_input("Enter Weight (kg)", min_value=0.5, max_value=5.0, step=0.1, value=2.0)
gpu = st.sidebar.selectbox("Select GPU", df['Gpu'].unique())
os_input = st.sidebar.selectbox("Select Operating System", df['OS'].unique())
cpu_brand = st.sidebar.selectbox("Select CPU Brand", df['Cpu brand'].unique())
hdd = st.sidebar.number_input("HDD (GB)", min_value=0, max_value=2000, step=128, value=0)
ssd = st.sidebar.number_input("SSD (GB)", min_value=0, max_value=2000, step=128, value=256)
touchscreen = st.sidebar.selectbox("Touchscreen", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
ips = st.sidebar.selectbox("IPS Panel", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
inches = st.sidebar.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1, value=15.6)
screen_res = st.sidebar.text_input("Screen Resolution (e.g., 1920x1080)", value="1920x1080")

# Calculate PPI
try:
    X_res, Y_res = map(int, screen_res.split('x'))
    ppi = ((X_res**2 + Y_res**2)**0.5) / inches
except:
    ppi = 0

# Prepare input DataFrame
input_df = pd.DataFrame({
    'Company': [company],
    'TypeName': [type_name],
    'Ram': [ram],
    'Gpu': [gpu],
    'OS': [os_input],
    'Weight': [weight],
    'Touchscreen': [touchscreen],
    'IPS': [ips],
    'ppi': [ppi],
    'Cpu brand': [cpu_brand],
    'HDD': [hdd],
    'SSD': [ssd],
})


if st.button("Predict Price"):
    prediction = pipe.predict(input_df)[0]
    price = np.exp(prediction)  # if your target y was log-transformed
    st.success(f"💰 Estimated Laptop Price: ₹ {round(price, 2)}")
