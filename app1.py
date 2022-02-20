#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 12:35:13 2022

@author: abhingude
"""
import streamlit as st
import random
import pandas as pd
def app():
    st.title('Dump your waste instantly')
    st.write("In this service, if you have a lot of garbage or plastic waste we'll come and pick up as soon as possible.")
    st.write("Send us your location and we'll be there to pick up")
    l=['Home','Hotel']
    st.radio("Choose a location : Home or Hotel",l)
    rid=[]
    stre=[]
    city1=[]
    stat=[]
    zipd=[]
    with st.form("my_form"):
        street=st.text_input("Street1")
        city=st.text_input("City")
        state=st.text_input("State")
        zipcode=st.text_input("Zipcode")
    # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            request_id=""
            for i in range(10):
                a=random.randint(1,9)
                request_id+= str(a)
            st.write("Request Submitted")
            st.write("Hurray, the truck will be on the way soon !!")
            st.write("Your RequestId: "+request_id)
            rid.append(request_id)
            stre.append(street)
            city1.append(city)
            stat.append(state)
            zipd.append(zipcode)
    df=pd.DataFrame()
    df['Request_Id']=rid
    df['Street']=stre
    df['City']=city1
    df['State']=stat
    df['zipcode']=zipd
    
    df.to_csv('dump_requests.csv', mode='a',header=False)
    
            
            
           
            
           
    