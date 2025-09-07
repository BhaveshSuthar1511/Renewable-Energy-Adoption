import streamlit as st
import pandas as pd
import pickle

# Load trained ML model
with open("Renewable_Energy_Adoption_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit page setup
st.set_page_config(page_title="Renewable Energy Adoption Predictor", layout="centered")
st.title("⚡ Renewable Energy Adoption Prediction")
st.write("Enter the feature values below to predict whether adoption is likely or not.")

# --- Input fields ---
carbon_emissions = st.number_input("Carbon Emissions", min_value=0.0, step=0.1)
energy_output = st.number_input("Energy Output", min_value=0.0, step=0.1)
renewability_index = st.slider("Renewability Index", 0.0, 1.0, 0.5, step=0.01)
cost_efficiency = st.slider("Cost Efficiency", 0.0, 1.0, 0.5, step=0.01)

# --- Prepare input ---
input_data = pd.DataFrame([{
    "carbon_emissions": carbon_emissions,
    "energy_output": energy_output,
    "renewability_index": renewability_index,
    "cost_efficiency": cost_efficiency
}])

# --- Prediction ---
if st.button("🔮 Predict"):
    try:
        prediction = model.predict(input_data)[0]

        # Show result
        if prediction == 1:
            st.success("✅ Likely to Adopt Renewable Energy")
        else:
            st.error("❌ Not Likely to Adopt Renewable Energy")

        # Optional: show confidence score (if model supports predict_proba)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0][1] * 100
            st.info(f"🔎 Confidence: {proba:.2f}%")

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
