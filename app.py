import streamlit as st
import requests
API_ENDPOINT = 'http://localhost:8000/predict'

st.set_page_config(page_title="Customer Health Predictor", layout="centered")

st.title("🧍 Customer Data Form")

# Input fields
age = st.number_input("Age", value=30)
weight = st.number_input("Weight (kg)" , value=70.0, step=0.1)
height = st.number_input("Height (m)", value=1.75, step=0.01)
income_lpa = st.number_input("Annual Income (in LPA)",  value=5.0, step=0.1)

smoker = st.radio("Smoker", options=[True, False], format_func=lambda x: "Yes" if x else "No")

city = st.text_input("City", value="Mumbai")

occupation = st.selectbox(
    "Occupation",
    options=[
        'retired', 'freelancer', 'student', 'government_job',
        'business_owner', 'unemployed', 'private_job'
    ]
)

# Prepare data
customer_data = {
    "age": age,
    "weight": weight,
    "height": height,
    "income_lpa": income_lpa,
    "smoker": smoker,
    "city": city,
    "occupation": occupation
}

# Submit button
if st.button("Submit"):
    # st.write("✅ Input Data:")
    # st.json(customer_data)

    # Optional: send to FastAPI
    try:
        response = requests.post(API_ENDPOINT, json=customer_data)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Predicted Insurance Premium category:{prediction['y_pred']}")
        else :
            st.error(f"Problem with the api end point, with error code {response.status_code}")

    except Exception as e:
        st.error(f"❌ Failed to connect to API: {e}")
