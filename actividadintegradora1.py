import streamlit as st
import pandas as pd

df = pd.read_csv('https://1drv.ms/u/s!Ap6XABHnyNvlpVqiu81lGSyg9bVP?e=8wDpM5')

st.dataframe(df)

st.markdown('Hola')

mapa=pd.DataFrame(df['Latitude'], df['Longitude'])
mapa=mapa.dropna()
st.map(mapa.astype(int))

mapa.info()
