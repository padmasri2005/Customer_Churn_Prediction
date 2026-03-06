import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Customer Churn Prediction")

col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=220)

with col2:
    st.markdown(
        "<h1 style='white-space:nowrap;'>Customer Churn Prediction</h1>",
        unsafe_allow_html=True
    )
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0,1])
    partner = st.selectbox("Partner", ["Yes","No"])
    dependents = st.selectbox("Dependents", ["Yes","No"])
    tenure = st.number_input("Tenure (months)",0,100)
    payment = st.selectbox("Payment Method",["Electronic check","Mailed check","Bank transfer","Credit card"])

with col2:
    phone = st.selectbox("Phone Service",["Yes","No"])
    multiple = st.selectbox("Multiple Lines",["Yes","No","No phone service"])
    internet = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
    online_security = st.selectbox("Online Security",["Yes","No","No internet service"])
    online_backup = st.selectbox("Online Backup",["Yes","No","No internet service"])
    paperless = st.selectbox("Paperless Billing",["Yes","No"])

with col3:
    device_protection = st.selectbox("Device Protection",["Yes","No","No internet service"])
    tech_support = st.selectbox("Tech Support",["Yes","No","No internet service"])
    streaming_tv = st.selectbox("Streaming TV",["Yes","No","No internet service"])
    streaming_movies = st.selectbox("Streaming Movies",["Yes","No","No internet service"])
    contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
    monthly = st.number_input("Monthly Charges",0.0,200.0)
    
total = st.number_input("Total Charges",0.0,10000.0)


# ---- Encoding (same as label encoding logic) ----

def encode(value, options):
    return options.index(value)

gender = encode(gender,["Male","Female"])
partner = encode(partner,["Yes","No"])
dependents = encode(dependents,["Yes","No"])
phone = encode(phone,["Yes","No"])
multiple = encode(multiple,["Yes","No","No phone service"])
internet = encode(internet,["DSL","Fiber optic","No"])
online_security = encode(online_security,["Yes","No","No internet service"])
online_backup = encode(online_backup,["Yes","No","No internet service"])
device_protection = encode(device_protection,["Yes","No","No internet service"])
tech_support = encode(tech_support,["Yes","No","No internet service"])
streaming_tv = encode(streaming_tv,["Yes","No","No internet service"])
streaming_movies = encode(streaming_movies,["Yes","No","No internet service"])
contract = encode(contract,["Month-to-month","One year","Two year"])
payment = encode(payment,["Electronic check","Mailed check","Bank transfer","Credit card"])
paperless = encode(paperless,["Yes","No"])


new_data = np.array([[gender, senior, partner, dependents, tenure,
                      phone, multiple, internet, online_security,
                      online_backup, device_protection, tech_support,
                      streaming_tv, streaming_movies, contract,
                      paperless, payment, monthly, total]])


# Centering the Predict Button
c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])

with c3:
    predict = st.button("Predict Churn")

# Prediction
if predict:

    prediction = model.predict(new_data)

    if prediction[0] == 1:
        st.markdown(
            "<h3 style='text-align:center; color:red;'>⚠️ Customer is likely to CHURN</h3>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h3 style='text-align:center; color:green;'>✅ Customer is NOT likely to churn</h3>",
            unsafe_allow_html=True
        )