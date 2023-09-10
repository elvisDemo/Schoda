import streamlit
import pandas
#import snowflake.connector
import requests


streamlit.title('Strong Tower')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & 🥑Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')


streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruityvice_responser = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
# my_fruit_list = my_fruit_list.set_index('Fruit')
# Showthis = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])   
# fruitsShow = my_fruit_list.loc(Showthis)

streamlit.dataframe(my_fruit_list)
streamlit.header('Fruitvice Fruit Advice!')
streamlit.text(fruityvice_responser.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_responser.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
