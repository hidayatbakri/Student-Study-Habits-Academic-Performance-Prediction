import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('models/model_lasso.pkl')

st.title("🎓 Prediksi Nilai Akhir Mahasiswa (Input 0–100)")

st.write("Masukkan data kebiasaan belajar mahasiswa (0–100):")

# Form input semua skala 0–100
with st.form("input_form"):
    study_hours = st.number_input("Jam belajar per minggu (168)", min_value=0, max_value=168, value=0)
    sleep_hours = st.number_input("Jam tidur per hari (24)", min_value=0, max_value=24, value=0)
    attendance = st.number_input("Persentase kehadiran (0–100)", min_value=0, max_value=100, value=0)
    assignments = st.number_input("Presentase tugas selesai (0–100)", min_value=0, max_value=100, value=0)

    submitted = st.form_submit_button("Prediksi Nilai")

# Jika form disubmit
if submitted:
    # Normalisasi manual: bagi 100
    input_data = pd.DataFrame([{
        'study_hours_per_week': study_hours / 100,
        'sleep_hours_per_day': sleep_hours / 100,
        'attendance_percentage': attendance / 100,
        'assignments_completed': assignments / 100
    }])

    # Prediksi nilai
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Prediksi nilai akhir mahasiswa: **{prediction:.2f}**")
