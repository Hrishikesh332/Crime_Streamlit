import streamlit as st
import folium as f
import pandas as pd
import numpy as np
import os
from plotly import graph_objects as go
from plotly.subplots import make_subplots
from streamlit_folium import folium_static
import folium
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

#Then go for the analysis stuff
    
#Then go for the analysis stuff
upload=st.sidebar.file_uploader(label="Upload Crime Record file in csv format", type=["csv"])
#df=pd.read_csv('Crimes_-_2001_to_Present.csv')
df1=pd.read_csv('Police_Stations.csv')
df2=pd.read_csv('chattisgarh.csv')
df3=pd.read_csv('crime.csv')

df3.dropna()
selected = option_menu(
            menu_title=None,  
            options=["Crime Hotspot", "About us"],  
            icons=["geo-alt", "pin-map", "bar-chart", "info-circle"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )

#df4=pd.read_csv('Chicago_Crimes_2012_to_2017.csv')
#df4['Date']= pd.to_datetime(df4['Date'], format='%m/%d/%Y %I:%M:%S %p')
#df4['index'] = pd.DatetimeIndex(df4['Date'])


if (selected=="Crime Hotspot"):
    global df
    if upload is not None:
        try:
            df=pd.read_csv(upload)
        except Exception as e:
            print(e)
    try:
        m= f.Map(location=[41.70,-87.67], zoom_start=12)
        tooltip="Click for info"
    
        f.TileLayer('Stamen Terrain').add_to(m)
        f.TileLayer('Stamen Toner').add_to(m)
        f.TileLayer('Stamen Water Color').add_to(m)
        f.TileLayer('cartodbpositron').add_to(m)
        f.TileLayer('cartodbdark_matter').add_to(m)
        f.LayerControl().add_to(m)
        df=df.dropna()
        #year=st.sidebar.selectbox("Select the Year: ", df["Year"].drop_duplicates().sort_values().tolist(), 0)
        year=st.sidebar.slider("Select the year range: ", 2001, 2022, (2015, 2022))
        
        #type1=st.sidebar.selectbox("Type of Crime: ", df["Type"].unique().tolist(), 0)
        type1= st.sidebar.multiselect("Type of Crime: ", df.Type.unique().tolist())
        
        dist=st.sidebar.selectbox("Select the District: ", df["District"].drop_duplicates().sort_values().tolist(), 0)
        #def fun1():
        #        for x in range(0, len(df)):
        #                   if ((df.iloc[x]["Type"]==type1) and (df.iloc[x]["District"]==dist) and (df.iloc[x]["Year"]<=year[0]) and (df.iloc[x]["Year"]<=year[1])):
        #                       f.CircleMarker(location=[df.iloc[x]['Latitude'], df.iloc[x]['Longitude']],  radius=25, popup=df.iloc[x]["Type"], color=df.iloc[x]["color1"], fill=True, fill_color=df.iloc[x]["color2"]).add_to(m)
        def fun1(p, color1, color2):
            df11=df[df["Type"]==p]
            for x in range(0, len(df11)):
                if ((df11.iloc[x]["District"]==dist) and (df11.iloc[x]["Year"]<=year[0]) and (df11.iloc[x]["Year"]<=year[1])):
                    f.CircleMarker(location=[df11.iloc[x]['Latitude'], df11.iloc[x]['Longitude']],  radius=25, popup=df11.iloc[x]["Type"], color=color1, fill=True, fill_color=color2).add_to(m)
              


        for p in range(len(type1)):
            color1=['#ff005a',
 '#AB96FF',
 '#FCE49C',
 '#FE9A65',
 '#7BFC90',
 '#CFFC8F',
 '#A5FCD4',
 '#95FDEA',
 '#FF785A',
 '#FF785A',
 '#EF511F',
 '#F9B0A5',
 '#8FBDFF',
 '#FF5244',
 '#FF8861',
 '#FF81C9',
 '#FAFC87',
 '#9BFBB4',
 '#737BFF',
 '#FDFD89',
 '#FAEB70',
 '#FE9491',
 '#F9C4C2',
 '#D1F9C2',
 '#CDFEC0',
 '#E74A31',
 '#FCE096']
            color2=['#eb0c83',
 '#7251F9',
 '#FBCF4F',
 '#FD7C37',
 '#11F537',
 '#B6FA54',
 '#6CFFBA',
 '#5FFCE0',
 '#FC4B24',
 '#FC4B24',
 '#B63208',
 '#DE7E6F',
 '#1B73F3',
 '#F71300',
 '#FF521B',
 '#FF119A',
 '#E1E412',
 '#1AF953',
 '#0915CF',
 '#FCFC41',
 '#F7DE06',
 '#B60904',
 '#F10C05',
 '#5EE12D',
 '#75F951',
 '#DD270B',
 '#FBC127']
            fun1(type1[p], color1[p], color2[p])
        st.markdown("<style> code { display: none;  margin: 0 !important; padding: 0 !important; width: 0px !important; height: -50% !important;} </style>", unsafe_allow_html=True)
        st.markdown("<style> .css-1v0mbdj img {position: absolute; top: -400px; left: 50%; width: 500px; height: 500px; margin-top: -250px; margin-left: -250px;} </style>", unsafe_allow_html=True)
        
        #class="stMarkdown"
        #st.markdown("<style> .stMarkdown { display: none;  margin: 0; padding: 0; width: 0px; height: 0px; } <style>", unsafe_allow_html=True)
        sum1=0

        for x in range(len(type1)):
            df4=df[df["Type"]==type1[x]]
            sum1+=len(df4)
        total=sum1
        station=len(df1)
        sum2=0
        for x in range(len(type1)):
            df4=df[df["Type"]==type1[x]]
            df5=df4[df4["District"]==dist]
            sum2+=len(df5)
        crime=sum2
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.markdown(f"Total {type1} Crime Committed overall:")
            st.title(f"{total}")
    

        with right_column:
            st.markdown(f"Total {type1} Crime Committed in the District no. {dist}:")
            st.title(f"{crime}")
        with middle_column:
            st.markdown(f"Total police station in the city chicago :")
            st.title(
            
                         station)
        for x in range(len(type1)):
            df11=df[df["Type"]==type1[x]]
            df22=df11[df11["District"]==dist]
            st.write(df22)
            
        
        def fun2():
                for x in range(0, len(df1)):
                    if len(df1.iloc[x]["DISTRICT NAME"])>0:
                        f.Marker([df1.iloc[x]['LATITUDE'], df1.iloc[x]['LONGITUDE']], popup=df1.iloc[x]["DISTRICT NAME"], tooltip=tooltip, icon=f.features.CustomIcon('policeman.png', icon_size=(50, 50))).add_to(m),
                        
        def fun3():
                for x in range(0, len(df2)):
                    if len(df2.iloc[x]["Address"])>0:
                        f.Marker([df2.iloc[x]['LATITUDE'], df2.iloc[x]['LONGITUDE']], popup=df2.iloc[x]["Address"], tooltip=tooltip, icon=f.features.CustomIcon('policeman.png', icon_size=(50, 50))).add_to(m),
                        
        
        fun2()
        fun3()
        st.image("Suraksha.png")
        folium_static(m, width=750, height=600)


    except Exception as e:
        print(e)
        st.subheader("Please upload the crime record data in this format:")
        st.image("temp.png", caption="Format to be followed", width=400)

    

elif (selected=="About us"):
    st.write("Made by Team: Four Bits")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('Ranjeet Saw')
        
        st.image("Ranjeet (3).jpeg")

    with col2:
        st.markdown("Hrishikesh Yadav")
        st.image("hrishi.jpeg")

    with col3:
        st.markdown("Abhishek Mishra")
        st.image("Abhishek.jpg")


