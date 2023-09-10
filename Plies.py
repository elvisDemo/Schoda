import streamlit
import pandas
import snowflake.connector
import requests
import subprocess
# subprocess.Popen(["pip", "install", "--upgrade", "urllib3"])

streamlit.title('Strong Tower')
streamlit.header('🍞Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & 🥑Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')


streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_responser = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




