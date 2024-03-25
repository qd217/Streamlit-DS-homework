import streamlit as st
import pandas as pd
import plotly.express as px

df = st.cache_data(pd.read_csv)("cars.csv")
df = df.rename(columns={'un' : 'Аббревиатура' , 'cars_per_cap' : 'На душу населения' , 'country' : 'Страна' , 'drives_right' : 'Водительские права' , 'age' : 'Возраст'})

# Button!!!
if st.button('RUSSIA????????????'):
    st.write('YEEEEP')

# Select box!!!
option = st.selectbox(
     'Водительские права',
     ('требуются', 'не требуются'))
if option == 'требуются':
    st.write('Egypt,Morocco,Russia,Unated States')
else:
    st.write('India,Japan,Australia',
             'не пон, как можно ездить без прав?')

# Slider!!!
age = st.slider('How old are you?', 16, 18)
if age == 16:
    st.write("Unated States")
elif age == 17:
    st.write("Нигде, увы")
else:
    st.write("Russia,Egypt,Morocco")

# Number input!!!
choice = st.number_input("Авто на душу",0,1000)
if 0 <= choice < 32:
    st.write('India')
elif 32 <= choice < 58:
        st.write('Egypt')
elif 58 <= choice < 135:
        st.write('Morocco')
elif 135 <= choice < 394:
        st.write('Russia')
elif 394 <= choice < 660:
        st.write('Japan')
elif 660 <= choice < 770:
        st.write('Australia')
elif 700 <= choice <= 1000:
        st.write('Unated States')

# Filter!!!
country = st.sidebar.multiselect(
    'Выбери страну',
    df['Страна'].unique()
)
filtred = df[(df['Страна'].isin(country))]
st.write(filtred)

st.dataframe(df)


