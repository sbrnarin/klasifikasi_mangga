import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Klasifikasi Kualitas Mangga",
    page_icon="🥭",
    layout="centered"
)

model = joblib.load("model_klasifikasi_mangga.joblib")

st.title("🥭 Klasifikasi Kualitas Mangga")
st.markdown("Aplikasi machine learning untuk memprediksi **kualitas mangga** berdasarkan ciri-ciri fisik dan asal daerah.")

# Input fitur
diameter = st.slider("Diameter (cm)", 5.0, 10.0, 7.5)
berat = st.slider("Berat (gram)", 150.0, 300.0, 220.0)
tebal_kulit = st.slider("Tebal Kulit (cm)", 0.2, 1.0, 0.5)
kadar_gula = st.slider("Kadar Gula (°Brix)", 8.0, 14.0, 11.0)
asal_daerah = st.radio("Asal Daerah", ["Kalimantan", "Jawa Tengah", "Jawa Barat", "Sulawesi", "Bali"], index=0)
warna = st.radio("Warna", ["hijau", "kuning", "jingga", "kemerahan"], index=1)
musim_panen = st.radio("Musim Panen", ["kemarau", "hujan"], index=0)

# Tombol prediksi
if st.button("Prediksi Kualitas", type="primary"):
    data_baru = pd.DataFrame([{
        "diameter": diameter,
        "berat": berat,
        "tebal_kulit": tebal_kulit,
        "kadar_gula": kadar_gula,
        "asal_daerah": asal_daerah,
        "warna": warna,
        "musim_panen": musim_panen
    }])

    prediksi = model.predict(data_baru)
    hasil = prediksi[0]

    if hasil.lower() == "bagus":
        st.success(f"🌟 Prediksi kualitas mangga: **{hasil}** — Mangga ini tergolong berkualitas tinggi!")
    elif hasil.lower() == "sedang":
        st.warning(f"🍃 Prediksi kualitas mangga: **{hasil}** — Mangga ini tergolong kualitas sedang.")
    else:
        st.error(f"🍂 Prediksi kualitas mangga: **{hasil}** — Mangga ini tergolong kualitas rendah.")

    st.markdown("### Data yang Dimasukkan")
    st.dataframe(data_baru)

st.divider()
st.caption("dibuat dengan 🥭 oleh **sabrina azmi**")
