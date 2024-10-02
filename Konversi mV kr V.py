import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Konversi mV ke V")

# Input data dari pengguna
data_input = st.text_area("Masukkan data (mV), pisahkan dengan koma:", "1000, 2000, 3000")

# Konversi data input ke dalam list
try:
    # Memisahkan input dan mengubah menjadi list float
    data_list = [float(i.strip()) for i in data_input.split(",")]
    
    # Mengonversi mV ke V
    data_in_volts = [x / 1000 for x in data_list]

    # Menampilkan hasil konversi
    st.write("Data dalam mV:", data_list)
    st.write("Data dalam V:", data_in_volts)

except ValueError:
    st.error("Tolong masukkan angka yang valid, pisahkan dengan koma.")
