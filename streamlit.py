import streamlit as st

# Input suhu dan satuan awal
x = st.number_input("Masukkan suhu:")
sx = st.selectbox("Satuan asal", ["C", "F", "K"])

# Input satuan tujuan konversi
sy = st.selectbox("Konversi ke", ["C", "F", "K"])

# Fungsi untuk konversi suhu
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Konversi dari Celsius
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    
    # Konversi dari Fahrenheit
    if from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    
    # Konversi dari Kelvin
    if from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32

# Lakukan konversi
result = convert_temperature(x, sx, sy)

# Output hasil konversi
st.write(f"Hasil konversi dari {x}°{sx} ke {sy} adalah {result}°{sy}.")

