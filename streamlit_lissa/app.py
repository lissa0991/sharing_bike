import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# Pengaturan awal
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)
import datetime
st.set_page_config(page_title="Air Quality Dashboard", layout="wide", initial_sidebar_state="auto")


# Judul dashboard
st.title('Dashboard Bike Sharing')


with st.sidebar:
    # Menambahkan logo perusahaan 
    name = st.text_input(label='Nama lengkap', value='')
    st.write('Nama: ', name)
  
    number = st.number_input(label='Umur')
    st.write('Umur: ', int(number), ' tahun')

    date = st.date_input(label='Tanggal lahir', min_value= datetime.date(1900, 1, 1))
    st.write('Tanggal lahir:', date)
    # Mengambil start_date & end_date dari date_input


col1, col2 = st.columns(2)

with col1:
    # Baca dataset
    dataset_day = pd.read_csv("day.csv")

    # Plot scatter plot untuk hubungan antara suhu (temp) dan jumlah pengguna terdaftar (registered)
    fig, ax = plt.subplots(figsize=(8, 6))  # Reduce the figure size
    ax.scatter(dataset_day['temp'], dataset_day['registered'], color='skyblue', alpha=0.6)
    ax.set_title('Hubungan antara Suhu dan Jumlah Pengguna Terdaftar')
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Pengguna Terdaftar')
    ax.grid(True, linestyle='--', alpha=0.6)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)
    st.write('Semakin tinggi kenaikan suhu maka semakin tinggi juga jumlah pengguna yang terdaftar, dapat dilihat pada grafik jumlah pendaftar tertinggi diantara 0.6 - 0.7 celcius, sebanyak 7000 pendaftar ')

    # Memfilter data untuk hari kerja
    weekday_data = dataset_day[(dataset_day['holiday'] == 0) & (dataset_day['workingday'] == 1)]

    # Menghitung jumlah total pengguna terdaftar dan pengguna sewaan pada hari kerja
    total_registered_users = weekday_data['registered'].sum()
    total_casual_users = weekday_data['casual'].sum()

    # Visualisasi jumlah pengguna terdaftar dan pengguna sewaan pada hari kerja dalam bentuk grafik batang
    fig, ax = plt.subplots(figsize=(10, 6))
    categories = ['Pengguna Terdaftar', 'Pengguna Sewaan']
    values = [total_registered_users, total_casual_users]
    ax.bar(categories, values, color=['blue', 'orange'])
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_title('Jumlah Pengguna Terdaftar dan Pengguna Sewaan pada Hari Kerja')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Menambahkan label nilai di atas bar
    for i, v in enumerate(values):
        ax.text(i, v + 10, str(v), ha='center', va='bottom', fontsize=10)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

    # Menampilkan data hari kerja dan jumlah pengguna menggunakan Streamlit
    st.write("Total pengguna terdaftar pada hari kerja:", total_registered_users)
    st.write("Total pengguna sewaan pada hari kerja:", total_casual_users)

with col2: 
    # Membuat mapping untuk musim
    season_mapping = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
                    7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'}
    dataset_day['season'] = dataset_day['mnth'].map(season_mapping)

    # Menghitung rata-rata sepeda yang disewa per musim
    average_bikes_rented_per_season = dataset_day.groupby('season')['cnt'].mean()

    # Menentukan musim dengan jumlah sepeda yang paling banyak disewa
    most_rented_season = average_bikes_rented_per_season.idxmax()
    total_rented_bikes_in_most_rented_season = average_bikes_rented_per_season.max()

    # Membuat plot menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Menampilkan data dalam bentuk bar plot
    average_bikes_rented_per_season.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewa')
    ax.set_title('Rata-rata Jumlah Sepeda Disewa per Musim')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    # Menambahkan label nilai di atas bar
    for i, v in enumerate(average_bikes_rented_per_season):
        ax.text(i, v + 10, str(round(v, 2)), ha='center', va='bottom', fontsize=10)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)
    # Menampilkan hasil menggunakan Streamlit
    st.write("Musim dengan jumlah sepeda yang banyak disewa:", most_rented_season)
    st.write("Jumlah sepeda yang disewa pada musim tersebut:", total_rented_bikes_in_most_rented_season)

    # Memfilter data untuk hari libur
    holiday_data = dataset_day[dataset_day['holiday'] == 1]

    # Menghitung total jumlah pengguna terdaftar dan pengguna sewaan pada hari libur
    total_registered_users_holiday = holiday_data['registered'].sum()
    total_casual_users_holiday = holiday_data['casual'].sum()

    # Visualisasi hubungan antara jumlah penyewa dan pendaftar dengan hari libur dalam bentuk bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    categories = ['Pengguna Terdaftar', 'Pengguna Sewaan']
    values = [total_registered_users_holiday, total_casual_users_holiday]
    ax.bar(categories, values, color=['blue', 'orange'])
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_title('Hubungan Antara Jumlah Pengguna Terdaftar dan Pengguna Sewaan dengan Hari Libur')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Menambahkan label nilai di atas bar
    for i, v in enumerate(values):
        ax.text(i, v + 10, str(v), ha='center', va='bottom', fontsize=10)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)
    st.write("Total pengguna terdaftar pada hari libur:", total_registered_users_holiday)
    st.write("Total pengguna sewaan pada hari libur:", total_casual_users_holiday)
