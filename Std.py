import pandas as pd
import streamlit as st
import matplotlib as plt
#import numpy as np

st.title("Hello world!")
st.write('Data')
df_data = pd.read_csv('OxAndEl2.csv', sep=';')
LookUp = pd.read_csv('LookUpTable.csv', sep=';')
#error_bad_lines=False
st.write(df_data)
st.write(LookUp)
std_names = df_data['Standard'].drop_duplicates()

LookUp.set_index("Element", inplace=True)
st.write(LookUp.loc[['Al'], ['Further information']])

#st.write(LookUp['Element'])
#Element(e) auswählen und Infos aus df_data anzeigen. In LookUp schauen: Wenn nicht N/A in LookUp für diese Element(e) die eingetragenen Werte als Spalten aus df_data anzeigen

st.sidebar.header("Select data:")
# Standard auswählen
standard = st.sidebar.multiselect("Select a standard:", options = df_data["Standard"].unique()) #, default = df_data["Standard"].unique())

# Element auswählen
elements = df_data.columns[26:104]
element = st.sidebar.multiselect("Select an element", options=list(elements)) #, default=list(df_data.columns[26:27]))



st.write("Please select an element / elements to see their concentrations for all standards.")  
fil = df_data['Constituent'] == 'Concentration'
df_data_conc_only = df_data[fil]
st.write(df_data_conc_only[["Standard"] + element + furtherinfo])

#if options in LookUp further ist ungleich N/A
#  st.write(LookUp['Eintrag in LookUp']
#furtherinfo = 



## Oxid auswählen
#oxides = df_data.iloc[:, 3:25]
#oxide = st.sidebar.multiselect("Select an oxide", options=list(oxides)) #, default=list(df_data.columns[3:25]))
#Gestein auswählen
#rocktype = st.sidebar.multiselect("Select your rock type:", options = df_metadata["Rock type"].unique(), default = df_data["Rock type"].unique())

st.write("Data for selected standard:")
df_data_selection = df_data.query("Standard == @standard")
st.dataframe(df_data_selection)



st.write("Please select an oxide / oxides to see their concentrations for all standards.")  
fil2 = df_data['Constituent'] == 'Concentration'
df_data_conc_only2 = df_data[fil2]
st.write(df_data_conc_only2[["Standard"] + oxide])

#st.write(df_data.iloc[:, 3:25])
#st.write(df[oxide])

##Drag and drop Menü um Daten hinzuzufügen:
  #st.write('Add your own data:')
  #uploadedfile = st.file_uploader("Choose your file")
  #df2 = pd.read_excel(uploadedfile)

## Standard auswählen
  #Standards = std_names (diese Liste, die wir definiert haben)
#option = st. selectbox ('Choose a standard:', (std_names))
#st.write('Selected:', option)

#def SelectData (name):
    #fil  = df_data['Standard'] == name
    #return df_data.loc[fil].T
