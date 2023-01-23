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

std_names = df_data['Standard'].drop_duplicates()

LookUp.set_index("Element", inplace=True)
st.write(LookUp)
#st.write(LookUp.loc[['Al'], ['Further information']])

st.sidebar.header("Select data:")
# Standard auswählen
standard = st.sidebar.multiselect("Select a standard:", options = df_data["Standard"].unique()) #, default = df_data["Standard"].unique())

st.write("Data for selected standard:")
df_data_selection = df_data.query("Standard == @standard")
st.dataframe(df_data_selection)

#st.write(LookUp['Element'])
#Element(e) auswählen und Infos aus df_data anzeigen. In LookUp schauen: Wenn nicht N/A in LookUp für diese Element(e) die eingetragenen Werte als Spalten aus df_data anzeigen

# Element auswählen
elements = df_data.columns[26:104]
element = st.sidebar.multiselect("Select an element", options=list(elements)) #, default=list(df_data.columns[26:27]))

st.write("Please select an element / elements to see their concentrations for all standards.")  
fil = df_data['Constituent'] == 'Concentration'
df_data_conc_only = df_data[fil]

furtherinfo = LookUp.loc[element]
st.write(furtherinfo) 

fullEllist = []
for i in furtherinfo['Further information'].tolist():
  res = i.split('_')
  fullEllist = fullEllist + res

#fullEllist = []
#for i in furtherinfo['Further information'].tolist():
  #i.apply(str)
  #if i == str:
    #res = i.split('_')
 # else: 
    #fullEllist.append(i)
#fullEllist = fullEllist + res
## res is not defined

#fullEllist = []
#for i in furtherinfo['Further information'].tolist():
  #i.apply(str)
  #res = i.split('_')
  #fullEllist = fullEllist + res
## 'str' object has no attribute 'apply'



  
fil2 = df_data_conc_only['Standard'] == standard
st.write(df_data_conc_only[fil2] + fullEllist)
  
#st.write(fullEllist)

#furtherinfo = LookUp.loc[[element], ['Further information']]
#st.write(df_data_conc_only[["Standard"] + element + furtherinfo])

#if options in LookUp further ist ungleich N/A
#  st.write(LookUp['Eintrag in LookUp']

#st.write(df_data_conc_only2[["Standard"] + element])

#Gestein auswählen
#rocktype = st.sidebar.multiselect("Select your rock type:", options = df_metadata["Rock type"].unique(), default = df_data["Rock type"].unique())

#st.write(df_data.iloc[:, 3:25])
#st.write(df[oxide])

##Drag and drop Menü um Daten hinzuzufügen:
  #st.write('Add your own data:')
  #uploadedfile = st.file_uploader("Choose your file")
  #df2 = pd.read_excel(uploadedfile)

#def SelectData (name):
    #fil  = df_data['Standard'] == name
    #return df_data.loc[fil].T
