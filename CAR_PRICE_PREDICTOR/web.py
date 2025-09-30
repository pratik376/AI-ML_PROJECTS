import streamlit as st
import pickle
import pandas as pd

# Load the trained model
pipe = pickle.load(open('LinearRegressionModel.pkl','rb'))

# Load dataset to get unique values for dropdowns
df = pd.read_csv('quikr_car.csv')

# Clean dataset for dropdowns
df = df[df['year'].str.isnumeric()]
df['year'] = df['year'].astype(int)
df = df[df['Price'] != 'Ask For Price']
df['Price'] = df['Price'].str.replace(",", "").astype(int)
df['kms_driven'] = df['kms_driven'].str.replace("kms","").str.replace(",","")
df = df[~df['kms_driven'].isin(['Petrol','NAN'])]
df['kms_driven'] = df['kms_driven'].astype(int)
df = df[~df['fuel_type'].isna()]
df['name'] = df['name'].str.split(" ").str.slice(0,3).str.join(" ")

# Sidebar inputs
st.sidebar.header("Car Details")

car_name = st.sidebar.selectbox("Select Car Name", sorted(df['name'].unique()))
company = st.sidebar.selectbox("Select Company", sorted(df['company'].unique()))
fuel_type = st.sidebar.selectbox("Select Fuel Type", sorted(df['fuel_type'].unique()))
year = st.sidebar.number_input("Year of Manufacture", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=2015, step=1)
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=int(df['kms_driven'].max()), value=50000, step=1000)

# Title
st.title("🚗 Car Price Prediction")
st.write("Predict the approximate price of your car based on selected details.")

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'name':[car_name],
        'company':[company],
        'year':[year],
        'kms_driven':[kms_driven],
        'fuel_type':[fuel_type]
    })
    
    prediction = pipe.predict(input_df)[0]
    
    st.success(f"💰 Estimated Price: ₹ {round(prediction):,}")
    st.info("Note: This is an approximate price based on historical data.")

# Optional: Show dataset preview
if st.checkbox("Show Sample Data"):
    st.subheader("Sample Car Data")
    st.dataframe(df[['name','company','year','kms_driven','fuel_type','Price']].head(10))
