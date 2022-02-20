#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:18:43 2022

@author: abhingude
"""
import streamlit as st
import pandas as pd
import random
def app():
    st.title('Give us your vegetable waste')
    st.write("Don't throw your vegetable waste. Instead give it to us. We'll use this for preparing manure and we all can enjoy organic products.")
    p=['Daily','Once in two days']
    freqy=st.radio("Choose a frequency when you want us to pick up",p)
    l=['Home','Hotel']
    h=st.radio("Choose a location : Home or Hotel",l)
    rid=[]
    stre=[]
    city1=[]
    stat=[]
    zipd=[]
    frequency=[]
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
            st.write("Hurray, the truck will arrive at your "+h+" "+freqy+" at 10AM!!")
            st.write("Your RequestId: "+request_id)
            st.write("Thanks for volunteering in converting vegetable waste to manure.")
            rid.append(request_id)
            stre.append(street)
            city1.append(city)
            stat.append(state)
            zipd.append(zipcode)
            frequency.append(freqy)
    df=pd.DataFrame()
    df['Request_Id']=rid
    df['Street']=stre
    df['City']=city1
    df['State']=stat
    df['zipcode']=zipd
    df['Frequency']=frequency
    df.to_csv('vegetable_waste.csv', mode='a',index=False,header=False)
    
            
    