import pandas as pd
import streamlit as st


#df = pd.read_excel("OxAndEl2.xlsx", "Tabelle1")


#wb = openpyxl.load_workbook(‘workbook.xlsx’)
#sheet = wb[‘data’]


st.write("Add your own data:")
uploadedfile = st.file_uploader("Choose your file")
df2 = pd.read_excel(uploadedfile)

