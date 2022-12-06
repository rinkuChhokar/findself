from deta import Deta
import os
import streamlit as st



# DETA_KEY = st.secrets["dkey"]

# DETA_KEY2 = st.secrets["dkey2"]


deta = Deta(st.secrets["DETA_KEY"])

deta1 = Deta(st.secrets["DETA_KEY2"])

db = deta.Base("info_db")

usrdb = deta1.Base("login_db")


# Functions related to admin page-

def insert_new_admin(username,name,password):

  return usrdb.put({"key":username,"Name":name,"Password":password})
 

def fetch_admin_details():

  res = usrdb.fetch()

  return res.items


# Functions related to home page-

def insert_values(date_t,uid,name,gender,ptype,result):

  return db.put({"Date and Time":date_t,"key":uid,"Name":name,"Gender":gender,"Person":ptype,"Personality Type":result})
 

def fetch_details():

  res = db.fetch()

  return res.items



