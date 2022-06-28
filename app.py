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

import chart_studio
import chart_studio.plotly as py
username = 'hrishi332'
api_key = 'CFUwESfbKWWspeJJ8ye8' 
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


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
    temp=False
    if upload is not None:
        try:
            df=pd.read_csv(upload)
            temp=True
        except Exception as e:
            print(e)
    try:
        if temp:
            #st.markdown("<script>img.style.visibility = 'hidden';</script>", unsafe_allow_html=True)
            #st.markdown("<style>img{z-index: -1;}</style>", unsafe_allow_html=True)
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

            df.Date = pd.to_datetime(df.Date, format='%m/%d/%Y %I:%M:%S %p')
            df.index = pd.DatetimeIndex(df.Date)
            df_type=list(df.Type.unique())[0:5]
            type_count=[]
            for x in range(len(df.Type.value_counts())):
    
                type_count.append(int(df.Type.value_counts()[x]))
                if x==4:
                    break
    
            plot11=px.bar(data_frame=df, x=df_type, y=type_count, title="No. of Crimes by Type of Crime: ", color=type_count, color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark")
            py.plot(plot11, filename = 'plot11', auto_open=False)
            # Top 5 place where 
            df_type=list(df.Where.unique())[0:5]
            type_count1=[]
            for x in range(len(df.Where.value_counts())):
    
                type_count1.append(int(df.Where.value_counts()[x]))
                if x==4:
                    break
    

            plot2=px.bar(data_frame=df, x=df_type, y=type_count1, title="Where most of the crime occurred: ", color=type_count, color_continuous_scale=px.colors.sequential.Blues,labels=dict(x="Location", y="No. of crime"), template="plotly_dark")
            py.plot(plot2, filename = 'plot2', auto_open=False)
            #Map
            fig1 = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="Type",hover_data=["block"],
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
                    
            fig1.update_layout(mapbox_style="open-street-map")
            py.plot(fig1, filename = 'plot34', auto_open=False)
            #Month
            plot3=px.bar(data_frame=df, x=['Jan','Feb','Mar',  'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                y=df.groupby([df.index.month]).size(), title="No. of occurrence of crime monthwise:  ", 
                color=df.groupby([df.index.month]).size(),  
                color_continuous_scale=px.colors.sequential.Blues ,labels=dict(x="Days Of Week", y="No. of crime"),template="plotly_dark")
            py.plot(plot3, filename = 'plot3', auto_open=False)
            #days of week
            plot4=px.bar(data_frame=df, x=['Monday','Tuesday','Wednesday',  'Thursday', 'Friday', 'Saturday', 'Sunday'], 
                y=df.groupby([df.index.dayofweek]).size(), title="No. of occurrence of crime in days of a week:  ", 
                color=df.groupby([df.index.dayofweek]).size(),  
                color_continuous_scale=px.colors.sequential.Blues ,labels=dict(x="Days Of Week", y="No. of crime"),template="plotly_dark")
            py.plot(plot4, filename = 'plot4', auto_open=False)

            #Arrest
            #Which Type of Crime is more and arrest is done?
            df_type=list(df_arrest.Type.unique())[0:5]
            type_count2=[]
            for x in range(len(df_arrest.Type.value_counts())):
    
                type_count2.append(int(df_arrest.Type.value_counts()[x]))
                if x==4:
                    break
            plot111 = px.pie(df, values=type_count, names=df_type,title="% of Crime Occurence where the arrest is done: ", color=type_count, color_discrete_sequence=px.colors.sequential.Blues, template="plotly_dark")
            py.plot(plot111, filename = 'plot1111', auto_open=False)
        else:
            #st.markdown("<style> #Hrishi  { display: none; } </style><script></script>", unsafe_allow_html=True)
            print(e)
            st.subheader("Please upload the crime record data in this format:")
            st.image("temp.png", caption="Format to be followed", width=400)

    except Exception as e:
        #a = """![a.png](temp.png)"""
        #st.markdown("![a.png](temp.png)")
        #a=temp.png
        #st.markdown("<img src= "'+a'"  id='a' alt='img'> ", unsafe_allow_html=True)
        print(e)
        st.subheader("Please upload the crime record data in this format:")
        st.markdown('''------------------------Data Type--------------------------------        --------------Column Header Name Expected-------------
                        
                    ________________Date____________________         _____________Date_____________
                        
                        Types of Crime/
                        Tool used to do crime/       Type
                        Type Any Details which
                        helps for investigation
                        
                        District/Ward/Location/      District
                        District Block
                        
                        Latitude                      Latitude
                        
                        Longitude                     Longitude''')
        #st.image("temp.png", caption="Format to be followed", width=400)


    

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
        st.image("abhishek.jpg")


