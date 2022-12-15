import pandas as pd
import streamlit as st

#wb = openpyxl.load_workbook(‘workbook.xlsx’)
#sheet = wb[‘data’]

st.title("Hello world!") 
df = pd.read_excel("OxAndEl2.xlsx")
st.write(df)
st.write("Add your own data:")
uploadedfile = st.file_uploader("Choose your file")
df2 = pd.read_excel(uploadedfile)

#df = pd.read_csv("./data/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
