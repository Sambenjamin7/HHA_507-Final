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

st.subheader('Hospital Types ')
bar1 = df_hospital['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.markdown('The different hospital type breakdowns: Acute Care, Critical Access Care, AC Department of defense, Childrens, and Psychiatric.') 

st.subheader('Pie Chart of the different Hospital Type')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)


st.header('Hospital types by NY state')
hospitalsny = df_hospital[df_hospital['state'] == 'NY']
st.subheader('Hospital Type NY')
bar1 = hospitalsny['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

##Merging the data 
hospitalinfo['provider_id'] = hospitalinfo['provider_id'].astype(str)
outpatient2015['provider_id'] = outpatient2015['provider_id'].astype(str)
inpatient2015['provider_id'] = inpatient2015['provider_id'].astype(str)

st.header('Hospital and Inpatient Merged Data')
df_merge_inpt2015 = inpatient2015.merge(hospitalinfo, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
df_merge_inpt2015_preview = df_merge_inpt2015.sample(20)
st.dataframe(df_merge_inpt2015_preview)

st.header('Hospital and Outpatient Merged Data')
df_merge_outpt2015 = outpatient2015.merge(hospitalinfo, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
df_merge_outpt2015_preview = df_merge_outpt2015.sample(20)
st.dataframe(df_merge_outpt2015_preview)

st.subheader('Stonybrook Data Hospital and the Outpatient')
# Stony brook data for Hospital and the outpatient merged dataset
sb_merge_outpt2015 = df_merge_outpt2015[df_merge_outpt2015['provider_id'] == '330393']
sb_merge_outpt2015_preview = sb_merge_outpt2015.sample(10)
st.dataframe(sb_merge_outpt2015_preview)

st.subheader('Stonybrook Data Hospital and the Inpatient')
# Stony brook data for Hospital and the Inpatient merged dataset
sb_merge_inpt2015 = df_merge_inpt2015[df_merge_inpt2015['provider_id'] == '330393']
sb_merge_inpt2015_preview = sb_merge_inpt2015.sample(20)
st.dataframe(sb_merge_inpt2015_preview)

st.subheader('Non Stonybrook Data Hospital and the Outpatient')
# Outside Stony Brook Data for Hospital and the Outpatient merged dataset
outsidesb_merge_outpt2015 = df_merge_outpt2015[df_merge_outpt2015['provider_id'] != '330393']
outsidesb_merge_outpt2015_preview = outsidesb_merge_outpt2015.sample(10)
st.dataframe(outsidesb_merge_outpt2015_preview)


st.subheader('Non Stonybrook Data Hospital/Inpatient')
# Outside Stony Brook Data for Hospital and the Inpatient merged dataset
outsidesb_merge_inpt2015 = df_merge_inpt2015[df_merge_inpt2015['provider_id'] != '330393']
outsidesb_merge_inpt2015_preview = outsidesb_merge_inpt2015.sample(10)
st.dataframe(outsidesb_merge_inpt2015_preview)

#Question 1
st.subheader('Question 1')
st.write('Question1: How does Stony Brook data compare to the inpatient hospitals for the most expensive DRGs')
st.markdown('The pivot tables shows: at StonyBrook 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.	with an average total payment of $216636.88 is the most expensive inpatient DRG. 001 - HEART TRANSPLANT OR IMPLANT OF HEART ASSIST SYSTEM W MCC with an average total payment of $449486.11 is the most expensive DRG of the outside facilities StonyBrook inpatient facilities ')

st.subheader('StonyBrook Inpatient DRGs Pivot Table')
SB_Inpatient_DRGs_pivot = sb_merge_inpt2015.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
SB_Inpatient_DRGs_pivot_desc = SB_Inpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(SB_Inpatient_DRGs_pivot_desc)

st.subheader('Outside StonyBrook Inpatient DRGs Pivot Table')
OutsideSB_Inpatient_DRGs_pivot = outsidesb_merge_inpt2015.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
OutsideSB_Inpatient_DRGs_pivot_desc = OutsideSB_Inpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.dataframe(OutsideSB_Inpatient_DRGs_pivot_desc)

###ALL OF NY DATA
st.subheader('All NY data EXCEPT StonyBrook (Outpatient)')
NY_nonsb_merge_outpt2015 = outsidesb_merge_outpt2015[outsidesb_merge_outpt2015['provider_state'] == 'NY']
NY_nonsb_merge_outpt2015_preview = NY_nonsb_merge_outpt2015.sample(10)
st.dataframe(NY_nonsb_merge_outpt2015_preview)

st.subheader('All NY data EXCEPT StonyBrook (Inpatient)')
NY_nonsb_merge_inpt2015 = outsidesb_merge_inpt2015[outsidesb_merge_inpt2015['provider_state'] == 'NY']
NY_nonsb_merge_inpt2015_preview = NY_nonsb_merge_inpt2015.sample(10)
st.dataframe(NY_nonsb_merge_inpt2015_preview)
















