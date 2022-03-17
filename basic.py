import streamlit as st
import pandas

data = {
    'Series_1':[1,3,4,5,7],
    'Series_2':[10,30,40,100,250]
}

df = pandas.DataFrame(data)

st.title('Our first streamlit app')
st.subheader('introducing streamlit in automate')
st.write('''Bruh This is streamlit. ENJOY ITTT!!''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Farenheit is', myslider * 9/5 + 32)