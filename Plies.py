import streamlit
import pandas
# import snowflake.connector

streamlit.title('Strong Tower')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & 🥑Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')
# Showthis = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])   
# fruitsShow = my_fruit_list.loc(Showthis)
streamlit.dataframe(my_fruit_list)
