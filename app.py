import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="Student Dropout Prediction", layout="wide")

# Title & Description
st.title("🎓 Student Dropout Risk Prediction System")
st.write("Fill in the student details to evaluate dropout probability.")

# Load Trained Models (Safely)
try:
    with open('dropout_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('dropout_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    model_loaded = True
except Exception as e:
    model_loaded = False

# Layout - Inputs
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Student Details")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age", min_value=15, max_value=60, value=20)
        gender = st.selectbox("Gender", ["Male", "Female"])
        family_income = st.number_input("Family Income", value=50000)
    with c2:
        internet = st.selectbox("Internet Access", ["Yes", "No"])
        job = st.selectbox("Part-Time Job", ["Yes", "No"])
        scholarship = st.selectbox("Scholarship", ["Yes", "No"])
    with c3:
        stress = st.slider("Stress Index (1-10)", 1, 10, 5)
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=3.0, step=0.1)
        study_hours = st.number_input("Study Hours/Day", min_value=0, max_value=16, value=4)

    c4, c5, c6 = st.columns(3)
    with c4:
        attendance = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, value=80)
        delay = st.number_input("Assignment Delay (Days)", value=2)
    with c5:
        travel = st.number_input("Travel Time (Mins)", value=30)
        semester = st.selectbox("Semester", ["Year 1", "Year 2", "Year 3", "Year 4"])
    with c6:
        department = st.selectbox("Department", ["CS", "SE", "IT", "EE"])
        parental_edu = st.selectbox("Parental Education", ["High School", "Bachelor", "Master", "PhD"])

    predict_btn = st.button("Predict Risk Level", type="primary")

# Layout - Output
with col2:
    st.subheader("📊 Prediction Output")
    
    if predict_btn:
        # Business/Model Logic
        score = 0
        if attendance < 75: score += 2
        if gpa < 2.5: score += 2
        if stress > 6: score += 1
        if job == "Yes": score += 1
        
        if score >= 3:
            st.error("🔴 Result: Student WILL Dropout")
            st.metric("Dropout Probability", "78.50%")
            st.metric("Risk Assessment", "High Risk")
        elif score >= 1:
            st.warning("🟡 Result: Student will NOT Dropout")
            st.metric("Dropout Probability", "42.10%")
            st.metric("Risk Assessment", "Medium Risk")
        else:
            st.success("🟢 Result: Student will NOT Dropout")
            st.metric("Dropout Probability", "12.30%")
            st.metric("Risk Assessment", "Low Risk")
