import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.title("IfG Powder Standards Database")
###st.write('Data')
df_data = pd.read_csv('OxAndEl2.csv', sep=';')
LookUp = pd.read_csv('LookUpTable.csv', sep=';')
df_meta = pd.read_csv('Meta.csv', sep=';')
df_abb = pd.read_csv('Abbreviations.csv', sep=';')
df_ci = pd.read_csv('CI-MORB-OIB-PM.csv', sep=';')
df_alplst = pd.read_csv('AlphabeticListStd.csv', sep=';') 
#error_bad_lines=False
st.write(df_data) # zeigt alle Daten

std_names = df_data['Standard'].drop_duplicates()

LookUp.set_index("Element", inplace=True)
st.write(LookUp) # zeigt Zusatzinformationen
#st.write(LookUp.loc[['Al'], ['Further information']])

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Standard", "Element", "Search", "CI, MORB, OIB, PM", "Abbreviations"])

with tab1:
   standard = st.multiselect("Select one or more standards:", options = df_data["Standard"].unique()) #, default = df_data["Standard"].unique())
   if len(standard) > 0:
      st.write("Element concentrations for selected standard(s):")
      df_data_selection = df_data.query("Standard == @standard")
      ###df_data_selection
      #df_data_selection.index = df_data_selection['Standard']
      st.dataframe(df_data_selection.T)

      st.write('Information for the selected standard(s):')
      #df_meta = pd.read_csv('Meta.csv', sep=';')
      df_meta.set_index("Standard", inplace = True)

      standardlist = []
      for i in standard:
         standardlist.append(i)

      metadata = df_meta.loc[standardlist]
      st.dataframe(metadata.T)
      
# Define the CSS style
      def color_alternate_rows(x):
         if x[::2]:
            return 'background-color: #f2f2f2'
         else:
            return 'background-color: #ffffff'

# Apply the style to the dataframe
      styled_df_data = df_data.style.applymap(color_alternate_rows)
         
# Display the styled dataframe
      #styled_df_data

   #df=pd.DataFrame(index=np.arange(10),columns=[1,2],data=np.random.normal(size=[10,2]))

      #df_meta.style.pipe(dfdark)
      #dfdark(df_meta)
      #st.write('meta neu')

      #df_meta.style.set_table_styles( [ {'selector': 'th', 'props': [('background-color', 'lightgray')] }, {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', EVEN_ROW_COLOR)] }])
    
with tab2:
   elements = df_data.columns[26:104]
   element = st.multiselect("Select one or more elements", options=list(elements)) #, default=list(df_data.columns[26:27]))
   if len(element) > 0:
      fil = df_data['Constituent'] == 'Concentration'
      df_data_conc_only = df_data[fil]

      ###furtherinfo = LookUp.loc[element]
      #st.write(furtherinfo) 
      #st.write(element)

      fullEllist = []

      for i in element:
         furtherinfo = LookUp.loc[i]
         fullEllist.append(i)
         for j in furtherinfo: #['Further information']  
            if isinstance(j, str):
               res = j.split('_')
               fullEllist.append(res)
            else:
               res = 'none'
      ### fullEllist

     ### flat nested list
      newlist = []
      for i in fullEllist:
         if type(i) is list:
            for j in i:
               newlist.append(j)
         else:
            newlist.append(i)
         #newlist.append(i)
      ### newlist

      dfselected = df_data[newlist]
      #st.write(dfselected)

      dfstd = df_data[['Standard','Constituent']]
      dfstandard = pd.DataFrame(dfstd)
      dfstandard.columns = ['Standard', 'Constituent']
      #dfstandard

      dfstandard = dfstandard.join(dfselected)
      dfstandard

      zeilen = df_data[df_data['Constituent'] == 'Concentration'].index # Index der Zeilen, in denen Concentration steht
      for i in element: # für jedes Element Spalte herausfinden, Wert Konzentration zusammen mit Zeile herausfinden, Auswahlmöglichkeiten, if/else
        auswahl = df_data.columns.get_loc(i) #Spalten der ausgewählten Elemente herausfinden
        d = df_data.iloc[zeilen, auswahl] # Zeilen mit Konzentration der ausgewählten Elemente anzeigen # Konzentrationswerte aller Stabdards für Element
        scale = st.radio('Choose a scale', ("linear scale", "log scale"), key=i)
        if scale == "log scale":
            fig2 = px.scatter(x=std_names, y=d, log_y=True,  title = i)
        else:
            fig2 = px.scatter(x=std_names, y=d, title = i)
        fig2.update_layout(xaxis_title="Standards", yaxis_title="Concentration in ppm")
        #st.plotly_chart(fig2)

         # plots # zeigt zwei Mal Element nebeneinander
        col1, col2 = st.columns(2)
        with col1:
           st.plotly_chart(fig2)
        with col2:
           st.plotly_chart(fig2)

      #zeilen = df_data[df_data['Constituent'] == 'Concentration'].index # Jede Zeile zeigen in der Concentration steht
      #for i in element:
        #auswahl = df_data.columns.get_loc(i)
        #d = df_data.iloc[zeilen, auswahl]
        #fig2 = px.scatter(x=std_names, y=d, log_y=True,  title = i)
        #fig2.update_layout(xaxis_title="Standards", yaxis_title="Concentration in ppm")
        #st.plotly_chart(fig2)


      #zeilen = df_data[df_data['Constituent'] == 'Concentration'].index # Jede Zeile zeigen in der Concentration steht
      #for i in element:
        #auswahl = df_data.columns.get_loc(i)
        #d = df_data.iloc[zeilen, auswahl]
        #updatemenus = [dict(type="buttons",direction="right",buttons=list([dict(args=[{'yaxis.type': 'linear'}],label="Linear Scale",method="relayout"),
              #dict(args=[{'yaxis.type': 'log'}],label="Log Scale", method="relayout" )  ]) ),]
        #fig2 = px.scatter(x=std_names, y=d,  title = i)
        #fig2.update_layout(updatemenus=updatemenus, xaxis_title="Standards", yaxis_title="Concentration in ppm")
        #st.plotly_chart(fig2)
   
   
with tab3:
   st.header("Search")
   st.write('To get more information about the standard(s) please switch to the tab "Standards".')
   #rocktypes = df_meta['rock type']
   #rocktype = st.multiselect("Select one or more rock types", options=list(rocktypes)) # Ausgewählte Gesteine
   #df_meta.set_index("rock type", inplace = True)
   #df_meta.loc[rocktype, :]
   
   
   # Search Rock Type
   rocktypes = df_alplst['Content'].drop_duplicates()
   rocktype = st.multiselect("Select one or more rock types", options=list(rocktypes)) 
   df_alplst.set_index("Content", inplace = True)
   df_alplst.loc[rocktype, :]
   
   
   # Search Producer
   producers = df_alplst['Producer'].drop_duplicates()
   producer = st.multiselect("Select one or more producers", options=list(producers)) 
   df_alplst.set_index("Producer", inplace = True)
   #st.write(df_alplst)
   df_alplst.loc[producer, :]
   
   # Search Location
   locations = df_alplst['Location'].drop_duplicates()
   location = st.multiselect("Select one or more locations", options=list(locations)) 
   df_alplst.set_index("Location", inplace = True)
   df_alplst.loc[location, :]
   
   #rocktypelist = []
   #for i in rocktype:
      #auswahl2 = df_meta.index[df_meta['rock type']==i] # soll Zeilen aller ausgewählten Gesteine angeben
      #auswahl2
   #df_meta.iloc[auswahl2]
      #e = df_meta.iloc[auswahl2, 1]
      #rocktypelist.append(i)
      #typestd = df_meta.loc[rocktypelist]
      #st.dataframe(typestd.T)
      
      
with tab4:
   st.header("CI, MORB, OIB, PM")
   st.write("Please select a standard to see the corresponding information.")
   type = st.radio('Choose a standard', ("CI Chondrite", "E-MORB", "N-MORB", "OIB", "PM"))
   df_ci.set_index("Rock", inplace = True)
   #st.write(df_ci)
   df_ci.loc[type, :]
   
      
with tab5:
   st.header("Abbreviations")
   st.write("List of Abbreviations for Entities and US States")
   st.write(df_abb)

      
     


#st.write(LookUp['Element'])
#Element(e) auswählen und Infos aus df_data anzeigen. In LookUp schauen: Wenn nicht N/A in LookUp für diese Element(e) die eingetragenen Werte als Spalten aus df_data anzeigen

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

#fil2 = df_data['Standard'] == standard
#df_data_std = df_data[fil2]
#st.write(standard + fullEllist)

#furtherinfo = LookUp.loc[[element], ['Further information']]
#st.write(df_data_conc_only[["Standard"] + element + furtherinfo])

#st.write(df_data_conc_only2[["Standard"] + element])

##Drag and drop Menü um Daten hinzuzufügen:
  #st.write('Add your own data:')
  #uploadedfile = st.file_uploader("Choose your file")
  #df2 = pd.read_excel(uploadedfile)

#def SelectData (name):
    #fil  = df_data['Standard'] == name
    #return df_data.loc[fil].T
