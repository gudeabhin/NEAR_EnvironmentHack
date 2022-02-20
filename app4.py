#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:43:52 2022

@author: abhingude
"""

import streamlit as st
import random
import pandas as pd
def app():
    st.title("Wanna grow plants at home?")
    st.write("Give us your location details and we'll deliver them within one day.")
    options = st.multiselect(
     'What are your favorite plants',
     ['Bird of Paradise','Dragon Tree','Norfolk Island Pine','Fishtail Palm','European Olive'])
    
    if options:
        for i in options:
            quantity=st.text_input("Enter the required quantity of "+i)
    st.write("Delivery Address")
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
            st.write("Hurray, Order Received")
            st.write("Your plants will be delivered within a day!!")
            st.write("OrderId: "+request_id)
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
    
    
    df.to_csv('plant_orders.csv', mode='a',header=False)