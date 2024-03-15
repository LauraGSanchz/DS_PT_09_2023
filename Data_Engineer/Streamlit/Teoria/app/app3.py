import streamlit as st
import seaborn as sns
import pandas as pd

df = sns.load_dataset('penguins')

st.title('Ejemplo de uso de write st.write()')
st.write('Hola: sunglasses: :heart:')

st.write(1+1)#esto devuelve la respuesta

a=2*3
st.write(a*5)#esto devuelve la respuesta

st.write(df.head(5))

st.write('st.write('text',df)', df.head(7))