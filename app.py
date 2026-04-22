import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('final_model.pkl', 'rb'))

# Encoding dictionaries
d1 = {'Comprehensive': 0, 'Third Party insurance': 1, 'Zero Dep': 2, 'Not Available': 3}
d2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3 = {'Manual': 0, 'Automatic': 1}
d4 = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth Owner': 4}

# Title
st.title("Car Price Prediction 🚗")

# Inputs (IMPORTANT: use selectbox instead of text_input)
insurance_validity = st.selectbox("Insurance Validity", list(d1.keys()))
fuel_type = st.selectbox("Fuel Type", list(d2.keys()))
kms_driven = st.number_input("KMs Driven", min_value=0)
ownership = st.selectbox("Ownership", list(d4.keys()))
transmission = st.selectbox("Transmission Type", list(d3.keys()))

# Predict button
if st.button("Predict"):

    try:
        # Convert input into numbers
        insurance = d1[insurance_validity]
        fuel = d2[fuel_type]
        owner = d4[ownership]
        trans = d3[transmission]

        # Final input
        test = np.array([[insurance, fuel, kms_driven, owner, trans]])

        # Prediction
        prediction = model.predict(test)[0]

        st.success(f"Predicted Car Price is ₹ {round(prediction, 2)} Lakhs")

    except Exception as e:
        st.error(f"Error: {e}")