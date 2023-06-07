import streamlit as st
import pandas as pd

df = pd.read_csv('https://github.com/samtrrs52/ActividadIntegradora1/blob/bed49a7bf39fc0e5b03a5e6c3f991a5db97670e9/Prueba_Police_Department_Incident_Reports__2018_to_Present.csv', low_memory=False)

st.dataframe(df)

st.markdown('Hola')

mapa=pd.DataFrame(df['Latitude'], df['Longitude'])
mapa=mapa.dropna()
st.map(mapa.astype(int))

mapa.info()
