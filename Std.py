import pandas as pd
import streamlit as st
import matplotlib as plt
#import numpy as np

st.title("Hello world!") 
st.write('Standards')
df_data = pd.read_csv('OxAndEl2.csv', sep=';')
#error_bad_lines=False
st.write(df_data)
std_names = df_data['Standard'].drop_duplicates() 

##Drag and drop Menü um Daten hinzuzufügen:
  #st.write('Add your own data:')
  #uploadedfile = st.file_uploader("Choose your file")
  #df2 = pd.read_excel(uploadedfile)

## Standard auswählen
  #Standards = std_names (diese Liste, die wir definiert haben)
  #option = st. selectbox ('Chosse a standard:', (Standard))
  #st.write('Selected:', optionx)


#df = pd.read_csv('Bastar Craton.csv')
         
#df = pd.read_csv("./data/titanic.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

#wb = openpyxl.load_workbook(‘workbook.xlsx’)
#sheet = wb[‘data’]
