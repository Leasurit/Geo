import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

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
elements = df_data.columns[26:104]
element = st.sidebar.multiselect("Select an element", options=list(elements)) #, default=list(df_data.columns[26:27]))

tab1, tab2, tab3 = st.tabs(["Standard", "Element", "Owl"])

with tab1:
   st.header("Standard")
   st.write("Please select a standard / standards to see all information.")
   st.write("Data for selected standard:")
   df_data_selection = df_data.query("Standard == @standard")
   st.dataframe(df_data_selection.T)

with tab2:
   st.header("Element")
   st.write("Please select an element / elements to see their concentrations for all standards.")  
   fil = df_data['Constituent'] == 'Concentration'
   df_data_conc_only = df_data[fil]

   ###furtherinfo = LookUp.loc[element]
   #st.write(furtherinfo) 
   ###st.write('element')
   ###st.write(element)

   fullEllist = []

   ###for i in furtherinfo['Further information'].tolist():
     ###if isinstance(i, str):
        ###res = i.split('_')
        ###fullEllist = fullEllist + res
   ###else:
     ###res = 'none'
   ###st.write("fullEllist")
   ###st.write(fullEllist)
   
   for i in element:
      furtherinfo = LookUp.loc[i]
      fullEllist.append(i)
      for j in furtherinfo: #['Further information']  
         if isinstance(j, str):
            res = j.split('_')
            fullEllist.append(res)
         else:
            res = 'none'
   fullEllist
   
   flatelements = []
   for sublist in fullEllist:
      for i in sublist:
         flatelements.append(i)
   flatelements
   
    
   dfselected = df_data[flatelements]
   st.write('dfselected')
   st.write(dfselected)

   dfstd = df_data['Standard']
   dfstandard = pd.DataFrame(dfstd)
   dfstandard.columns = ['Standard']
   #dfstandard

   dfstandard = dfstandard.join(dfselected)
   dfstandard

   zeilen = df_data[df_data['Constituent'] == 'Concentration'].index # Jede Zeile zeigen in der Concentration steht
   for i in element:
     auswahl = df_data.columns.get_loc(i)
     d = df_data.iloc[zeilen, auswahl]
     fig2 = px.scatter(x=std_names, y=d, log_y=True,  title = i)
     fig2.update_layout(xaxis_title="Standards", yaxis_title="Concentration in ppm")
     st.plotly_chart(fig2)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



#st.write(LookUp['Element'])
#Element(e) auswählen und Infos aus df_data anzeigen. In LookUp schauen: Wenn nicht N/A in LookUp für diese Element(e) die eingetragenen Werte als Spalten aus df_data anzeigen

# Element auswählen



#st.write(fullEllist)

#Anforderungen Befehl
# Ich möchte ein Element / mehrere Elemente auswählen und dann alle Einträge, die es zu meiner Auswahl gibt für alle Standards angezeigt bekommen.
# Es sollen also die Spalten Standard und zum Beispiel Al und Al2O3 meiner ursprünglichen Tabelle angezeigt werden
# Vorgang: Element auswählen -> in der Look Up Tabelle schauen ob es weitere Einträge gibt -> wenn ja auch diese anzeigen -> alle relevanten Spalten in einer Tabelle

# Vorbereitung Befehl
# df_data[fullEllist] # zeigt alle zusätzlichen Spalten zum ausgewählten Element
# df_data[element] # zeigt Spalten aller ausgewählten Elemente
# df_data['Standard'] # zeigt Spalte Standard



# Ende Befehl

# Anforderungen Befehl
# Soll die Konzentrationen für ausgewähltes Element von allen Standards in Plot zeigen
# auch für Oxide und weitere Bestandteile (z.B. Carbon Inorga)?
# wenn mehrere Element ausgewählt werden, sollen mehrere Plots erstellt werden
# x-Achse: Standards 
# y-Achse: Elementkonzentration von ausgewähltem Element
# Weiteres: Plots gut anordnen, Achsen beschriften, sinnvolle Werte/Größenordung

# Vorbereitung Befehl
#Test: st.write(zeilen)
#Auswahl = df_data.columns.get_loc('Al') # Spaltennummer von Element Al
#c = df_data.iloc[zeilen, Auswahl] # Zeilen mit Concentration und Spaltennummer des Elements
# Test: st.write(c)
#fig = px.scatter(x=std_names, y=c, log_y=True)
#st.plotly_chart(fig)



# Ende Befehl



#fig1, ax = plt.subplots()
#ax.scatter(x,y)


#fil2 = df_data['Standard'] == standard
#df_data_std = df_data[fil2]
#st.write(standard + fullEllist)


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
