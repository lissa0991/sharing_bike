# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os 

# Nama : Rahmalia Nurhalissa
# Submission Data Analyst ML-61

# LOAD DATA

# @st.cache
# def load_data():
#     # Mendapatkan direktori tempat skrip Python berjalan
#     current_directory = os.getcwd()
#     # Menggabungkan direktori saat ini dengan nama file
#     relative_path = os.path.join(current_directory, "C:\\Users\\User\\Documents\\bangkit\\submission\\day.xlsx")
#     data = pd.read_excel(relative_path)
#     return data

# # Memanggil fungsi untuk memuat data
# data = load_data()
@st.cache_resource
def load_data():
    data = pd.read_csv("./day.csv")
    return data


data = load_data()

# TITLE DASHBOARD
# Set page title
st.title("Bike Share Dashboard Day")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/code)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian')
st.sidebar.markdown('2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut')
st.sidebar.markdown('3: Salju Ringan, Hujan Ringan + Badai Petir + Awan Tersebar, Hujan Ringan + Awan Tersebar')
st.sidebar.markdown('4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut')


# VISUALIZATION

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    # st.subheader("Season-wise Bike Share Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Hujan", 4: "Musim Dingin"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Jumlah Penyewa berdasarkan Musim")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Jumlah Penyewa berdasar Cuaca")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)


# weekday vs. Bike Share Count
# st.subheader("Humidity vs. Bike Share Count")
fig_weekday_chart = px.scatter(
    data, x="weekday", y="cnt", title="hari kerja vs. Jumlah Penyewa")
st.plotly_chart(fig_weekday_chart)

# holiday vs. Bike Share Count
# st.subheader("holiday vs. Bike Share Count")
fig_holiday_chart = px.scatter(
    data, x="holiday", y="cnt", title="holiday vs. Jumlah Penyewa")
st.plotly_chart(fig_holiday_chart)

# Temperature vs. Bike Share Count
# st.subheader("Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Jumlah Penyewa")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")
