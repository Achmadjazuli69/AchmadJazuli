import streamlit as st

# Fungsi untuk menghitung defek massa
def hitung_defek_massa(jumlah_proton, jumlah_neutron, massa_nuklida):
    massa_proton = 1.007276  # Massa proton dalam u
    massa_neutron = 1.008665  # Massa neutron dalam u

    total_massa_proton = jumlah_proton * massa_proton
    total_massa_neutron = jumlah_neutron * massa_neutron

    defek_massa = (total_massa_proton + total_massa_neutron) - massa_nuklida
    return defek_massa

# Judul aplikasi
st.set_page_config(page_title="Penghitungan Defek Massa", layout="wide")
st.title("Penghitungan Defek Massa")

# Sidebar untuk input
st.sidebar.header("Input Data")
jumlah_proton = st.sidebar.number_input("Masukkan jumlah proton (Z):", min_value=0)
jumlah_neutron = st.sidebar.number_input("Masukkan jumlah neutron (N):", min_value=0)
massa_nuklida = st.sidebar.number_input("Masukkan massa nuklida (dalam u):", min_value=0.0)

# Tombol hitung
if st.sidebar.button("Hitung Defek Massa"):
    defek = hitung_defek_massa(jumlah_proton, jumlah_neutron, massa_nuklida)
    st.success(f"Defek massa (Δm) adalah: **{defek:.6f} u**")

# Menampilkan informasi tambahan
st.markdown("""
## Penjelasan
Defek massa adalah perbedaan antara massa total proton dan neutron dengan massa nuklida. 
Ini menunjukkan stabilitas nuklida dan energi yang terlibat dalam pembentukannya.
""")
