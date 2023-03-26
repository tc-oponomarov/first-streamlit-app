import streamlit
import pandas as pd
import requests

streamlit.title('Hello to cool app!')
streamlit.header('Cool header')
streamlit.text('Some text describing whats going on here')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
# streamlit.text(fruityvice_response.json())

# convert json response into dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display dataframe
streamlit.dataframe(fruityvice_normalized)
