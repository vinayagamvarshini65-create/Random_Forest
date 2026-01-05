import streamlit as st
import pandas as pd
import joblib

# Set page title
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Title and description
st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to estimate the price.")

# Load the model
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

model = load_model()

# Create columns for organized input
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Location", ["Downtown", "Hills", "Rural", "Suburb", "Waterfront"])
    house_type = st.selectbox("House Type", ["Apartment", "Condo", "House", "Townhouse", "Villa"])
    sqft = st.number_input("Square Footage", min_value=100, max_value=10000, value=2000)
    lot_size = st.number_input("Lot Size", min_value=0, max_value=50000, value=5000)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
    garage = st.number_input("Garage Spaces", min_value=0, max_value=5, value=2)

with col2:
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 10, 2)
    age = st.number_input("Age of House", min_value=0, max_value=200, value=25)
    condition = st.slider("Condition Rating", 1, 5, 3)
    school_rating = st.slider("School Rating", 1, 10, 7)
    
    # Checkbox features
    has_pool = st.checkbox("Has Pool")
    has_fireplace = st.checkbox("Has Fireplace")
    has_basement = st.checkbox("Has Basement")

# Map checkboxes to 1/0 as expected by the model
data = {
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "sqft": [sqft],
    "lot_size": [lot_size],
    "age": [age],
    "year_built": [year_built],
    "garage": [garage],
    "location": [location],
    "house_type": [house_type],
    "condition": [condition],
    "has_pool": [1 if has_pool else 0],
    "has_fireplace": [1 if has_fireplace else 0],
    "has_basement": [1 if has_basement else 0],
    "school_rating": [school_rating]
}

# Create a DataFrame for prediction
input_df = pd.DataFrame(data)

# Predict Button
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"### Estimated Price: ${prediction[0]:,.2f}")