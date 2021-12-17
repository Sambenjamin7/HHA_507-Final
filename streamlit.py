#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:00:59 2021

@author: samanthabenjamin
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import matplotlib.pyplot as plt
import seaborn as sns



st.title('HHA 507 Streamlit Final Assiggnment')
st.write('Questions aiming towards the Hospital, Outpatient and Inpatient datasets')

df_hospital = hospitalinfo = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

df_outpatient = outpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

df_inpatient = inpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

@st.cache
def load_hospitals():
    df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital.csv')
    return df_Hospital

@st.cache
def load_inpatient():
    df_Inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient.csv')
    return df_Inpatient

@st.cache
def load_outpatient():
    df_Outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient.csv')
    return df_Outpatient


st.title('Loading the all dataset Files')

##Load the Data:
hospital_info = load_hospitals()
outpatient2015 = load_outpatient()
inpatient2015 = load_inpatient()

st.header('Hospital Dataset')
st.dataframe(hospitalinfo)

st.header('Inpatient Dataset')
st.dataframe(inpatient2015)

st.header('Outpatient Dataset')
st.dataframe(outpatient2015)

st.subheader('Hospital Type ')
bar1 = df_hospital['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.markdown('The different hospital type breakdowns: Acute Care, Critical Access Care, AC Department of defense, Childrens, and Psychiatric.') 

st.subheader('Pie Chart of the different Hospital Type')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)



