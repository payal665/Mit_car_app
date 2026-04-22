import streamlit as st
import pickle
import numpy as np

# Load models
price_model = pickle.load(open('final_model.pkl', 'rb'))
mileage_model = pickle.load(open('mileage_model.pkl', 'rb'))

# Sidebar selection
option = st.sidebar.selectbox("Select Prediction", ["Price Prediction", "Mileage Prediction"])

# ================= PRICE =================
if option == "Price Prediction":

    d1 = {'Comprehensive': 0, 'Third Party insurance': 1, 'Zero Dep': 2, 'Not Available': 3}
    d2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
    d3 = {'Manual': 0, 'Automatic': 1}
    d4 = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth Owner': 4}

    st.title("Car Price and Mileage Prediction")

    insurance_validity = st.selectbox("Insurance Validity", list(d1.keys()))
    fuel_type = st.selectbox("Fuel Type", list(d2.keys()))
    kms_driven = st.number_input("KMs Driven", min_value=0)
    ownership = st.selectbox("Ownership", list(d4.keys()))
    transmission = st.selectbox("Transmission Type", list(d3.keys()))

    if st.button("Predict Price"):
        insurance = d1[insurance_validity]
        fuel = d2[fuel_type]
        owner = d4[ownership]
        trans = d3[transmission]

        test = np.array([[insurance, fuel, kms_driven, owner, trans]])
        prediction = price_model.predict(test)[0]

        st.success(f"Predicted Price: {round(prediction, 2)} Lakhs")

# ================= MILEAGE =================
elif option == "Mileage Prediction":

    fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3}
    trans_dict = {'Manual': 0, 'Automatic': 1}

    st.title("Car Mileage Prediction")

    fuel = st.selectbox("Fuel Type", list(fuel_dict.keys()))
    engine = st.slider("Engine (CC)", 800, 3000)
    kms = st.slider("KMs Driven", 0, 200000)
    trans = st.selectbox("Transmission", list(trans_dict.keys()))

    if st.button("Predict Mileage"):
        test = np.array([[fuel_dict[fuel], engine, kms, trans_dict[trans]]])
        prediction = mileage_model.predict(test)[0]

        st.success(f"Predicted Mileage: {round(prediction, 2)} km/l")