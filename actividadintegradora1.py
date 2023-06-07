import streamlit as st
import pandas as pd

df = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')

st.dataframe(df)

st.markdown('Hola')

mapa=pd.DataFrame(df['Latitude'], df['Longitude'])
mapa=mapa.dropna()
st.map(mapa.astype(int))

mapa.info()