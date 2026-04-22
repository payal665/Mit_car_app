import streamlit as st
import pickle
import numpy as np

import os

model_path = os.path.join(os.getcwd(), "mileage_model.pkl")
model = pickle.load(open(model_path, 'rb'))

fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3}
trans_dict = {'Manual': 0, 'Automatic': 1}

st.title("Car Mileage Prediction 🚗")
st.image("https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg")

fuel = st.selectbox("Fuel Type", list(fuel_dict.keys()))
engine = st.slider("Engine (CC)", 800, 3000)
kms = st.slider("KMs Driven", 0, 200000)
trans = st.selectbox("Transmission", list(trans_dict.keys()))

if st.button("Predict"):
    test = np.array([[fuel_dict[fuel], engine, kms, trans_dict[trans]]])
    prediction = model.predict(test)[0]
    st.success(f"🚗 Estimated Mileage: {round(prediction,2)} km/l")