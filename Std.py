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

st.sidebar.header("Select here:")
standard = st.sidebar.multiselect("Select your standard:", options = df_data["Standard"].unique(), default = df_data["Standard"].unique())

##Drag and drop Menü um Daten hinzuzufügen:
  #st.write('Add your own data:')
  #uploadedfile = st.file_uploader("Choose your file")
  #df2 = pd.read_excel(uploadedfile)

## Standard auswählen
  #Standards = std_names (diese Liste, die wir definiert haben)
option = st. selectbox ('Choose a standard:', (std_names))
st.write('Selected:', option)

#def SelectData (name):
    #fil  = df_data['Standard'] == name
    #return df_data.loc[fil].T
