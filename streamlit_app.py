import streamlit as st
import pandas as pd
import numpy as np

# 1. Title
st.title("Dashboard Reza")

# 2. Header
st.header("Analisis Performa By Reza")

# 3. Subheader
st.subheader("Ringkasan Statistik Mingguan")

# 4. Text (Paragraf)
st.text("""
contoh teks menggunakan streamlit yang dibuat dengan VS Code dan diupload digithub
""")

# 5. Caption
st.caption("Data diperbarui secara otomatis setiap jam.")

# 6. Code (Potongan Kode)
st.subheader("Snippet Kode")
code_example = '''
def hitung_total(data):
    return data.sum()

# Memanggil fungsi
total = hitung_total(df['sales'])
'''
st.code(code_example, language='python')

# 7. Data Display (Dataframe & Table)
st.subheader("Visualisasi Data")

# Membuat data dummy
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Produk A', 'Produk B', 'Produk C']
)

st.write("Menampilkan Data dalam bentuk DataFrame (Interaktif):")
st.dataframe(df)

st.write("Menampilkan Data dalam bentuk Table (Statis):")
st.table(df.iloc[0:3]) # Hanya menampilkan 3 baris pertama agar ringkas

# 8. Chart
st.subheader("Grafik Tren Penjualan")
st.line_chart(df)

st.write("Grafik Area:")
st.area_chart(df)