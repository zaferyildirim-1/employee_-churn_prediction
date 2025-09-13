import streamlit as st
import joblib
import pandas as pd
from pathlib import Path
import numpy as np

st.set_page_config(page_title="Employee Churn Prediction", page_icon="📉", layout="wide")
st.title("Employee Churn Prediction App")
st.sidebar.header("Input Employee Features")

@st.cache_resource
def load_model():
    here = Path(__file__).parent
    candidates = [
        here / "gb_best_pipe_final.joblib",                   # repo root (your current layout)
        here / "saved_models" / "gb_best_pipe_final.joblib",  # fallback
    ]
    for p in candidates:
        if p.exists():
            return joblib.load(p)
    raise FileNotFoundError(f"Model file not found. Tried: {', '.join(map(str, candidates))}")

model = load_model()

# Sidebar inputs
satisfaction_level = st.sidebar.slider("Satisfaction Level", 0.0, 1.0, 0.5, 0.01)
last_evaluation = st.sidebar.slider("Last Evaluation", 0.0, 1.0, 0.5, 0.01)
number_project = st.sidebar.slider("Number of Projects", 1, 10, 3)
average_montly_hours = st.sidebar.slider("Average Monthly Hours", 80, 320, 160)
time_spend_company = st.sidebar.slider("Years at Company", 1, 10, 3)
work_accident = st.sidebar.selectbox("Work Accident", [0, 1])
promotion_last_5years = st.sidebar.selectbox("Promotion in Last 5 Years", [0, 1])
dept_ui = st.sidebar.selectbox(
    "Department",
    ['Sales','Technical','Support','IT','RandD','Accounting','HR','Management','Marketing','Product_mng']
)
# Map UI -> training labels (case-sensitive for encoders)
DEPT_MAP = {
    'Sales':'sales','Technical':'technical','Support':'support','IT':'IT','RandD':'RandD',
    'Accounting':'accounting','HR':'hr','Management':'management','Marketing':'marketing',
    'Product_mng':'product_mng'
}
departments = DEPT_MAP[dept_ui]
salary = st.sidebar.selectbox("Salary Level", ['low', 'medium', 'high'])

input_df = pd.DataFrame([{
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,  # keep dataset’s original spelling
    "time_spend_company": time_spend_company,
    "work_accident": work_accident,
    "promotion_last_5years": promotion_last_5years,
    "departments": departments,
    "salary": salary
}])

st.write("### Preview")
st.dataframe(input_df, use_container_width=True)

if st.sidebar.button("Predict Churn"):
    pred = model.predict(input_df)[0]
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0][1]
    else:
        proba = None

    st.subheader("Prediction Result")
    if pred == 1:
        st.success("Churn Prediction: **Left**")
        if proba is not None:
            st.write(f"Churn Probability: **{proba:.2%}**")
        st.image("left.png", caption="Employee likely to leave", use_container_width=True)
    else:
        st.success("Churn Prediction: **Stayed**")
        if proba is not None:
            st.write(f"Churn Probability: **{proba:.2%}**")
        st.image("stayed.png", caption="Employee likely to stay", use_container_width=True)


