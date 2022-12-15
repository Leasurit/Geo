import pandas as pd
import streamlit as st
import openpyxl

#df = pd.read_excel("OxAndEl2.xlsx", "Tabelle1")


#wb = openpyxl.load_workbook(‘workbook.xlsx’)
#sheet = wb[‘data’]

uploadedfile = st.file_uploader("OxAndEl2")
df = pd.read_excel(uploadedfile)

