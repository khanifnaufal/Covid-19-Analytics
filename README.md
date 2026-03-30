# 🌍 Global COVID-19 Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3f4f75?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas)

Selamat datang di repositori **Global COVID-19 Analytics Dashboard**. Proyek ini merupakan portofolio *End-to-End Data Analytics* yang dibangun untuk menggali, membersihkan, dan memvisualisasikan data penyebaran pandemi COVID-19 dalam skala global (hingga pertengahan 2020) lintas benua, beserta pelacakan episentrum spesifik hingga level negara bagian (State) di Amerika Serikat. 

Proyek ini menggunakan **Jupyter Notebook** untuk *Exploratory Data Analysis (EDA)* dan **Streamlit** untuk disajikan secara premium menjadi aplikasi *Web Dashboard* interaktif.

## ✨ Fitur Utama (Interactive Features)

Aplikasi web telah dibagi ke dalam 5 bagian analisis utama (Tabs) yang mencakup:

1. 📈 **Tren Global (Time-Series)**: Mempertontokan pergerakan kurva akumulasi penyebaran dan kematian pasien dari hari ke hari di seluruh dunia secara agregat.
2. 🗺️ **Peta Dunia Terkini (Choropleth Map)**: Peta sensosori spasial interaktif. *Hover* pada negara manapun untuk menampilkan detail kasus penyebaran maupun persentase *testing*.
3. 📊 **Komparasi Antar-Negara**: Pembanding data laju infeksi dua/tiga negara pilihan secara langsung secara *head-to-head* pada satu layar.
4. 🏆 **Papan Klasemen Performa Penanganan**: Grafik analisis batang murni (Bar Chart) untuk menampilkan deretan profil performa mitigasi, seperti Rasio Kesembuhan hingga rasio *Fatalities* tertinggi.
5. 🇺🇸 **Eksplorasi Episentrum USA**: Penetrasi *Data Drilling* spesifik pada set data regional (*County/Province*) untuk mencari kawasan utama penularan di Amerika Serikat tanpa mengorbankan fungsionalitas memori perangkat (*Memory-Efficient Agregation*).

## 📂 Struktur Repositori

- `COVID19_Global_Analysis.ipynb` — Eksplorasi Analisis Data (*Clean Data & Storytelling*) yang mencakup kesimpulan analitis berbasis bisnis.
- `app.py` — *Source Code* utama yang merender logika Streamlit dengan UI/UX Plotly yang sudah dikustomisasi.
- `dataset/` — Memuat kumpulan 6 file CSV skala besar (seperti `day_wise.csv`, `worldometer_data.csv`, `usa_county_wise.csv`, dll). *Catatan: Beberapa file sangat besar, mungkin butuh Git LFS.*

## 🚀 Instalasi & Cara Menjalankan Aplikasi Secara Lokal

Anda bisa memainkan grafik di dasbor ini dengan mengakses localhost lokal mesin Anda. Berikut ini adalah langkah-langkahnya:

1. **Unduh Repositori**:
   ```bash
   git clone https://github.com/USERNAME_ANDA/Covid19-Data-Analytics.git
   cd Covid19-Data-Analytics
   ```

2. **(Opsional) Buat Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install Dependencies (*Libraries*)**:
   Pastikan pustaka analitik ini terinstal (sudah tersedia opsinya melalui *pip*):
   ```bash
   pip install streamlit pandas plotly numpy
   ```

4. **Luncurkan Aplikasi Streamlit**:
   Ketik dan *Enter* perintah pemanggilan berikut di Terminal Anda:
   ```bash
   streamlit run app.py
   ```
   Aplikasi akan secara otomatis meluncur di browser default Anda (umumnya di alamat web `http://localhost:8501`).

## ✍️ Konklusi Eksekutif (*Brief Insights*)

1. **Volume Tes Realistis**: Kami berhasil melihat tingginya kolerasi positif antara total uji (*Total Tests*) dengan Konfirmasi Kasus Baru. Negara pelapor sepi infeksi bukan berarti mereka kebal, namun fasilitas penunjang tes mereka lemah dalam pelacakan (kasus tak terlihat tinggi).
2. **Lonjakan Skala Harian**: AS, Brazil, dan India mendongkrak kurva infeksi di setengah kuartal periode pada rentang bulan Maret secara agresif, dan episentrum spesifik terbesar mencuat dari titik *New York, USA*.

---
⭐ *Dibuat oleh **[Nama/Github Anda]**. Silakan beri Star jika portofolio analisis data ini bermanfaat bagi inspirasi proyek Anda selanjutnya!*
