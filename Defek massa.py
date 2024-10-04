import streamlit as st

def hitung_defek_massa(jumlah_proton, jumlah_neutron, massa_nuklida):
    massa_proton = 1.007276  # Massa proton dalam u
    massa_neutron = 1.008665  # Massa neutron dalam u

    total_massa_proton = jumlah_proton * massa_proton
    total_massa_neutron = jumlah_neutron * massa_neutron

    defek_massa = (total_massa_proton + total_massa_neutron) - massa_nuklida
    return defek_massa

# Judul aplikasi
st.title("Penghitungan Defek Massa")

# Input dari pengguna
jumlah_proton = st.number_input("Masukkan jumlah proton (Z):", min_value=0)
jumlah_neutron = st.number_input("Masukkan jumlah neutron (N):", min_value=0)
massa_nuklida = st.number_input("Masukkan massa nuklida (dalam u):", min_value=0.0)

if st.button("Hitung Defek Massa"):
    defek = hitung_defek_massa(jumlah_proton, jumlah_neutron, massa_nuklida)
    st.write(f"Defek massa (Δm) adalah: {defek:.6f} u")
