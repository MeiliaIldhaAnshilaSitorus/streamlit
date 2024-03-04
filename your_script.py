#######################streamlit run your_script.py
# Import libraries
import streamlit as st
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#######################
# Page configuration
st.set_page_config(
    page_title="Bike Riding",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")
#######################
# Load data
df_day = pd.read_csv("C:/Users/asus/Downloads/Pengumpulan tugas/data/data1_day.csv")
df_hour = pd.read_csv("C:/Users/asus/Downloads/Pengumpulan tugas/data/data 2_hour.csv")
st.title("Projek Analisis Data Bike Riding")
st.caption("Ini adalah dashboard menggunakan dataset Bike Sharing.")
st.header("Pengembangan Dashboard")
if st.button('Hello everyone'):
    st.write("Berikut berbagai visualisasi data yang tersaji:")

#Data day
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_day['season'] = df_day.season.astype('category')
df_day['mnth'] = df_day.mnth.astype('category')
df_day['holiday'] = df_day.holiday.astype('category')
df_day['weekday'] = df_day.weekday.astype('category')
df_day['workingday'] = df_day.workingday.astype('category')
df_day['weathersit'] = df_day.weathersit.astype('category')
#Data hour
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
df_hour['season'] = df_hour.season.astype('category')
df_hour['mnth'] = df_hour.mnth.astype('category')
df_hour['holiday'] = df_hour.holiday.astype('category')
df_hour['weekday'] = df_hour.weekday.astype('category')
df_hour['workingday'] = df_hour.workingday.astype('category')
df_hour['weathersit'] = df_hour.weathersit.astype('category')

df_BikeSharing = df_hour.merge(df_day, on='dteday', how='inner', suffixes=('_hour', '_day'))
#Konversi Nilai
# Season: 1:Winter, 2:Spring, 3:Summer, 4:Fall
df_day.season.replace((1,2,3,4), ('Winter','Spring','Summer','Fall'), inplace=True)

# Year: 0:2011, 1:2012
df_day.yr.replace((0,1), (2011,2012), inplace=True)

# Month:  1:Jan, 2:Feb, 3:Mar, 4:Apr, 5:May, 6:Jun, 7:Jul, 8:Aug, 9:Sep, 10:Oct, 11:Nov, 12:Dec
df_day.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'), inplace=True)

# Weathersit: 1:Clear, 2:Misty, 3:Light_RainSnow 4:Heavy_RainSnow
df_day.weathersit.replace((1,2,3,4), ('Clear','Misty','Light_RainSnow','Heavy_RainSnow'), inplace=True)

# Weekday: 0:Sun, 1:Mon, 2:Tue, 3:Wed, 4:Thu, 5:Fri, 6:Sat
df_day.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)

# Workingday: 0:No, 1:Yes
df_day.workingday.replace((0,1), ('No', 'Yes'), inplace=True)
# Semua tipe data tidak ada yang bermasalah
#Drop kolom yang tidak digunakan dalam data
df_day1 = df_day.drop("instant", axis=1)
df_day1.head()
df_day1.rename(columns={
    "dteday" : "Date",
    "yr" : "Year",
    "mnth" : "Month",
    "weathersit" : "Weather",
    "hum" : "Humiidity",
    "temp" : "Temperature",
    "atemp" : "Atemp",
    "windspeed" : "Windspeed",
    "season" : "Season",
    "holiday" : "Holiday",
    "weekday" : "Weekday",
    "casual" : "Casual",
    "registered" : "Registered",
    "cnt" : "Sum_count"}, inplace=True
)
df_day1['Temperature'] = df_day1['Temperature']*41
df_day1['Atemp'] = df_day1['Atemp']*50
df_day1['Humiidity'] = df_day1['Humiidity']*100
df_day1['Windspeed'] = df_day1['Windspeed']*67

st.header('Visualisasi Data:')
#________________________________________________________________________________________________________________________________________

 #Histogram
columns = ['Casual', 'Registered', 'Sum_count']

fig, ax = plt.subplots(1, 3, figsize=(10,5))

for i, ax in enumerate(ax):
    sns.histplot(x=df_day1[columns[i]], ax=ax, bins=10, color='green')
    ax.set_title(columns[i])
    ax.set_xlabel("")
    ax.set_ylabel("")

plt.tight_layout()
plt.show()
st.pyplot(fig)
#________________________________________________________________________________________________________________________________________

#Boxplot 1
fig, ax = plt.subplots(1, 3, figsize=(10,5))

for i, ax in enumerate(ax):
    sns.boxplot(y=df_day1[columns[i]], ax=ax, color='green')
    ax.set_title(columns[i])
    ax.set_xlabel("")
    ax.set_ylabel("")

plt.tight_layout()
plt.show()
st.pyplot(fig)
#________________________________________________________________________________________________________________________________________

#Boxplot 2
plt.figure(figsize=(16,6))
sns.boxplot(
    x="Season",
    y="Sum_count",
    data=df_day1,
    palette=["green", "blue"]
)
plt.xlabel("Season (Musim)")
plt.ylabel("Total Rides(Total Perjalanan)")
plt.title("Total dari Bikeshare Bides by Season (Total dari Bikeshare Bides berdasarkan Musim)")
plt.show()
st.pyplot(plt)
#________________________________________________________________________________________________________________________________________

#Boxplot 3
plt.figure(figsize=(16,6))
sns.boxplot(
    x="Month",
    y="Sum_count",
    data=df_day1,
    palette=["blue", "navy"]
)
plt.xlabel("Month (Bulan)")
plt.ylabel("Total Rides (Total Perjalanan)")
plt.title("Total dari Bikeshare Rides by Month (Total dari Perjalanan Bikeshare per Bulan)")
plt.show()
st.pyplot(plt)
##########################################################################################################################################
#Pertanyaan 1
plt.figure(figsize=(10,6))
sns.barplot(x='Month', y='Sum_count', data=df_day1, hue='Year')
plt.xlabel("Month (Bulan)")
plt.ylabel("Total Rides (Total Perjalanan)")
plt.title("Total of bikeshare rides per Month (Jumlah Perjalanan Bikeshare per Bulan)")
plt.show()
st.pyplot(plt)
st.caption('Pada tahun 2011 jumlah permintaan akan bikesharing memiliki jumlah permintaan tertinggi terjadi pada bulan Juni. Dan pada tahun 2012 jumlah permintaan terhadap bikesharing memiliki jumlah permintaan tertinggi terjadi pada bulan September.')

#Pertanyaan 2
plt.figure(figsize=(10,6))
sns.scatterplot(x='Temperature', y='Sum_count', data=df_day1, hue='Season')
plt.xlabel("Temperature (Suhu)")
plt.ylabel("Total Rides (Total Perjalanan)")
plt.title("Clusters of Bikeshare Rides by Season and Temperature in 2011-2012")
plt.tight_layout()
plt.show()
st.pyplot(plt)
st.caption('Permintaan akan bikeriding relatif rendah pada suhu kurang dari 20 derajat Celcius.Dan permintaan bikeriding relatif tinggi ketika pada suhu 25-30 derajat Celcius.')

#Pertanyaan 3
rental_jam = df_BikeSharing.groupby('hr')['cnt_hour'].mean()
plt.bar(rental_jam.index, rental_jam.values, color='green')
plt.title('Mean Penyewaan per Jam')
plt.xlabel('Hour (Jam)')
plt.ylabel('Mean dari Penyewaan')
plt.show()
st.pyplot(plt)
st.caption('Berdasarkan hasil output di atas maka dapat dilihat bahwa nilai mean dari penyewaan sepeda paling banyak terjadi pada saat jam 17 dan 18 atau jam 5 pm dan 6 pm dan yang paling sedikit saat jam 4 am')