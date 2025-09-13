import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("saved_models/gb_best_pipe_final.joblib")

st.title("Employee Churn Prediction App")

st.sidebar.header("Input Employee Features")

# Sidebar inputs
satisfaction_level = st.sidebar.slider("Satisfaction Level", 0.0, 1.0, 0.5, 0.01)
last_evaluation = st.sidebar.slider("Last Evaluation", 0.0, 1.0, 0.5, 0.01)
number_project = st.sidebar.slider("Number of Projects", 1, 10, 3)
average_montly_hours = st.sidebar.slider("Average Monthly Hours", 80, 320, 160)
time_spend_company = st.sidebar.slider("Years at Company", 1, 10, 3)
work_accident = st.sidebar.selectbox("Work Accident", [0, 1])
promotion_last_5years = st.sidebar.selectbox("Promotion in Last 5 Years", [0, 1])
departments = st.sidebar.selectbox(
    "Department",
    ['Sales', 'Technical', 'Support', 'IT', 'RandD', 'Accounting', 'HR', 'Management', 'Marketing', 'Product_mng']
)
salary = st.sidebar.selectbox("Salary Level", ['low', 'medium', 'high'])

# Prepare input as DataFrame for pipeline
import pandas as pd
input_df = pd.DataFrame([{
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,
    "time_spend_company": time_spend_company,
    "work_accident": work_accident,
    "promotion_last_5years": promotion_last_5years,
    "departments": departments,
    "salary": salary
}])

if st.sidebar.button("Predict Churn"):
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    st.subheader("Prediction Result")
    st.write(f"Churn Prediction: {'Left' if pred == 1 else 'Stayed'}")
    st.write(f"Churn Probability: {proba:.2%}")
