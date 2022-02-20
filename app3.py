#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:33:27 2022

@author: abhingude
"""
import streamlit as st
import pandas as pd
import random
def app():
    st.title("Send us a location where it is untidy")
    st.write("Our team will asess the issue and be right there to clean that up")
    picture = st.camera_input("Take a picture where it is untidy")

    #if picture:
        #st.image(picture)
    st.write("Now, give us the location details")
    rid=[]
    nam=[]
    stre=[]
    city1=[]
    stat=[]
    zipd=[]
    with st.form("my_form"):
        name=st.text_input("Name")
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
            st.write("Thanks for your time")
            st.write("The team will be there soon to clean it up.!!")
            #st.write("Your RequestId: "+request_id)
            rid.append(request_id)
            nam.append(name)
            stre.append(street)
            city1.append(city)
            stat.append(state)
            zipd.append(zipcode)
    df=pd.DataFrame()
    df['Request_Id']=rid
    df['Name']=nam
    df['Street']=stre
    df['City']=city1
    df['State']=stat
    df['zipcode']=zipd
    
    df.to_csv('unclean_requests.csv', mode='a',header=False)
    