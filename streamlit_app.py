import streamlit
import pandas as pd

streamlit.title('Hello to cool app!')
streamlit.header('Cool header')
streamlit.text('Some text describing whats going on here')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
