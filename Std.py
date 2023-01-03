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

st.sidebar.header("Select data:")
# Standard auswählen
standard = st.sidebar.multiselect("Select your standard:", options = df_data["Standard"].unique()) #, default = df_data["Standard"].unique())
# Oxid auswählen
oxide = st.sidebar.multiselect("Select your oxide", options=list(df_data.columns[3:25])) #, default=list(df_data.columns[3:25]))
# Element auswählen
element = st.sidebar.multiselect("Select your element", options=list(df_data.columns[26:104])) #, default=list(df_data.columns[26:104]))
#Gestein auswählen
#rocktype = st.sidebar.multiselect("Select your rock type:", options = df_metadata["Rock type"].unique(), default = df_data["Rock type"].unique())

df_data_selection = df_data.query("Standard == @standard")
st.dataframe(df_data_selection)

st.write(df_data.iloc[:, 3:25])
#st.write(df[oxide])

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
    
#df1.iloc[4:8, [3,5]]
# zeigt Spalten 3 und 5 der Zeilen 4 bis 7
