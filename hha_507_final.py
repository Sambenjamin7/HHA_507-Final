# -*- coding: utf-8 -*-
"""HHA_507 Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Dm_w-Bt0wZH1Tqy7JAnomJCCBU25MpY

### Importing Packages
"""


# Commented out IPython magic to ensure Python compatibility.



import pandas as pd


pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

"""### Loading in the Files """

##Loading in Files

inpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
outpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
hospitalinfo = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

"""### Exploring the hospital zipcode info """

hospitalinfo['zip_code'] = hospitalinfo['zip_code'].astype(str)

hospitalinfo['zip_code']

"""### Deeper Explore of all three datasets """

print('HospitalInfoLength :', len(hospitalinfo))
print('OutPatientLength :', len(outpatient2015))
print('InPatientLength :', len(inpatient2015))

"""### List of hospital infomation and specififc hospital locations."""

list (hospitalinfo)

"""### data holds the inpatient drg codes as well as payments and medicare coverage"""

list (inpatient2015)

"""### data holds apc codes from the ouptaient locations with both charges and payements"""

list (outpatient2015)

"""### Sample all three datasets"""

hospitalinfo.sample(20)

inpatient2015.sample(20)

outpatient2015.sample(20)

"""### Data Profiling for each dataset"""



"""### Importing the rest of the packages """







"""### Data Cleaning out NaN functions """

outpatient2015 = outpatient2015.dropna()
outpatient2015.sample(20)

inpatient2015 = inpatient2015.dropna()
inpatient2015.sample(20)

hospitalinfo = hospitalinfo.dropna()
hospitalinfo.sample(20)

hospitalinfo['provider_id'] = hospitalinfo['provider_id'].astype(str)
outpatient2015['provider_id'] = outpatient2015['provider_id'].astype(str)
inpatient2015['provider_id'] = inpatient2015['provider_id'].astype(str)

"""### Merging Both inpatient and outpatient datasets with hospital info dataset"""

df_merge_inpt2015 = inpatient2015.merge(hospitalinfo, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
df_merge_inpt2015

df_merge_outpt2015 = outpatient2015.merge(hospitalinfo, how = 'left', left_on = 'provider_id', right_on = 'provider_id')

df_merge_outpt2015.sample(20)

"""### New Inpatient and outpatient length"""

print('NewInpatient2015Length: ', len(df_merge_inpt2015))

print('NewOutpatient2015Length: ', len(df_merge_outpt2015))


"""### Stony brook merged datset for inpatient/ outpatient"""

SBUinfo = hospitalinfo[hospitalinfo['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
SBUinfo

sb_inpatient = inpatient2015[inpatient2015['provider_id'] == 330393]
sb_inpatient

sb_merge_outpt2015 = df_merge_outpt2015[df_merge_outpt2015['provider_id'] == '330393']
sb_merge_outpt2015.sample(10)

sb_merge_inpt2015 = df_merge_inpt2015[df_merge_inpt2015['provider_id'] == '330393']
sb_merge_inpt2015.sample(10)

"""### dataset for hospitals that are not SBU with both merged inpatient/ outpatient hospital data"""

outsidesb_merge_inpt2015 = df_merge_inpt2015[df_merge_inpt2015['provider_id'] != '330393']
outsidesb_merge_inpt2015.sample(10)

ousidesb_merge_outpt2015 = df_merge_outpt2015[df_merge_outpt2015['provider_id'] != '330393']
ousidesb_merge_outpt2015.sample(10)

"""### NY hospitals only dataset"""

NY_nonsb_merge_outpt2015 = ousidesb_merge_outpt2015[ousidesb_merge_outpt2015['provider_state'] == 'NY']
NY_nonsb_merge_outpt2015.sample(10)

NY_nonsb_merge_inpt2015 = outsidesb_merge_inpt2015[outsidesb_merge_inpt2015['provider_state'] == 'NY']
NY_nonsb_merge_inpt2015.sample(10)

sb_merge_outpt2015['mortality_national_comparison'].isna().sum()

NY_nonsb_merge_outpt2015['mortality_national_comparison'].isna().sum()

NY_nonsb_merge_outpt_nonull = NY_nonsb_merge_outpt2015[~NY_nonsb_merge_outpt2015['mortality_national_comparison'].isnull()]
NY_nonsb_merge_outpt_nonull['mortality_national_comparison'].isna().sum()

sb_merge_inpt2015['mortality_national_comparison'].isna().sum()

NY_nonsb_merge_inpt2015['mortality_national_comparison'].isna().sum()

NY_nonsb_merge_inpt_nonull = NY_nonsb_merge_inpt2015[~NY_nonsb_merge_inpt2015['mortality_national_comparison'].isnull()]
NY_nonsb_merge_inpt_nonull['mortality_national_comparison'].isna().sum()

"""### Question 1: How does Stony Brook data compare to the inpatient hospirals for the most expensive DRGs"""

SB_InpatientDRGs_pivot = sb_merge_inpt2015.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
NonSB_InpatientDRGs_pivot = outsidesb_merge_inpt2015.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])

SB_InpatientDRGs_pivot

SB_InpatientDRGs_pivot.sort_values(by=['average_total_payments'], ascending=False)

NonSB_InpatientDRGs_pivot

NonSB_InpatientDRGs_pivot.sort_values(by=['average_total_payments'], ascending=False)

"""### Question 2: How does Stonybrook data compare to the other outpatient hospitals for the most expensive APCs?"""

sb_merge_outpt2015['average_total_payments'].isna().sum()

sb_merge_inpt2015['average_total_payments'].isna().sum()

SB_Outpatient2015_APCs_pivot = sb_merge_outpt2015.pivot_table(index=['provider_id','apc'],values=['average_total_payments'])
NonSB_Outpatient2015_APCs_pivot = ousidesb_merge_outpt2015.pivot_table(index=['provider_id','apc'],values=['average_total_payments'])

SB_Outpatient2015_APCs_pivot

"""### Question 3: How does Stony Brook data compare to the outpatient hospirals for the most expensive DRGs

# OutPatient: 

# How many hospitals for each state?

# which 3 states have the most hospitals 

# what 3 states have the least amount of hospitals
"""

Total_state = pd.value_counts(outpatient2015['provider_state'])
Total_state = pd.DataFrame(Total_state)
Total_state = Total_state.reset_index()

Total_state.columns = ['provider_state', 'Number of Hospitals']




dims = (10, 10)
fig, ax = plt.subplots(figsize=dims)
ax = sns.barplot(x = 'Number of Hospitals', y = 'provider_state', data = Total_state)
ax.set(xlabel = 'Number of Hospitals', ylabel = 'States')
ax.set_title('Number of Hospitals per State')

df= display
display(Total_state)

State_acute_1=NY_nonsb_merge_outpt2015.loc[(NY_nonsb_merge_outpt2015["hospital_type"]=="Acute Care Hospitals") & (hospitalinfo["hospital_overall_rating"]=="1"),["state"]]
State_acute_1.head()

S_A_1=State_acute_1['state'].value_counts()
index=S_A_1.index
values=S_A_1.values
values

dims = (8, 10)
fig, ax = plt.subplots(figsize=dims)

ax=sns.barplot(y=index,x=values,palette='GnBu_d')
ax.set(xlabel='Total number of Acute Care hospitals with 1 rating', ylabel='states')
min([], default="EMPTY")

min([], default="EMPTY")

a= pd.pivot_table(hospitalinfo,values=['hospital_overall_rating'],index=['hospital_ownership'],columns=['hospital_type'],aggfunc='count',margins=False)

plt.figure(figsize=(10,10))
sns.heatmap(a['hospital_overall_rating'],linewidths=.5,annot=True,vmin=0.01,cmap='YlGnBu')
plt.title('Total rating of the types of hospitals under the ownership of various community')

Hospital_owner = pd.value_counts(hospitalinfo['hospital_ownership'])
Hospital_owner = pd.DataFrame(Hospital_owner)
Hospital_owner = Hospital_owner.reset_index()
Hospital_owner.columns = ['Hospital Ownership', 'Number of Hospitals']

dims = (10, 10)
fig, ax = plt.subplots(figsize=dims)
ax = sns.barplot(y = 'Hospital Ownership', x= 'Number of Hospitals', data = Hospital_owner)
ax.set(xlabel = 'Hospital Ownership', ylabel = 'Number of Hospitals')
ax.set_title('Count of the different Types of Hospital Ownership')

display(Hospital_owner)

"""Above the information on the barchart that both the vluntary non-profit private hospital are the most common ownership with all the hospitals

### Question 4: How does the stony brook dataset compare to the NY inpatient hospitalss when focusing on the mortality comparison and the total discharges
"""

SB_Inpatient_MNCs_pivot = sb_merge_inpt2015.pivot_table(index=['provider_id','mortality_national_comparison'],values=['total_discharges'])
NY_NonSB_Inpatient_MNCs_pivot = NY_nonsb_merge_inpt_nonull.pivot_table(index=['provider_id','mortality_national_comparison'],values=['total_discharges'])

SB_Inpatient_MNCs_pivot

NY_NonSB_Inpatient_MNCs_pivot

NY_NonSB_Inpatient_MNCs_pivot['total_discharges'].mean()

SB_Outpatient_MNCs_pivot = sb_merge_outpt2015.pivot_table(index=['provider_id','mortality_national_comparison'],values=['outpatient_services'])
NY_NonSB_Outpatient_MNCs_pivot = NY_nonsb_merge_outpt_nonull.pivot_table(index=['provider_id','mortality_national_comparison'],values=['outpatient_services'])

SB_Outpatient_MNCs_pivot

"""### Question 5: what is the differnece between the total payment for SBU hospital comparing to a differnet hospital **from** a different state."""

average_total_payments = pd.value_counts(hospitalinfo['hospital_name'])
average_total_payments = pd.DataFrame(average_total_payments)
average_total_payments = average_total_payments.reset_index()

average_total_payments.columns = ['hospital_name', 'average_total_payments']

dims = (10, 10)
fig, ax = plt.subplots(figsize=dims)
ax = sns.barplot(x = 'hospital_name', y = 'average_total_payments', data = average_total_payments)
ax.set(xlabel = 'hospital_name', ylabel = 'average_total_payments')
ax.set_title('Average total payments for hospital')

"""### Question 6: What is the correlation between the care care comparing to the readmission national comparison"""

hospitalinfo['effectiveness_of_care_national_comparison'].isna().sum()

hospitalinfo['readmission_national_comparison_footnote'].isna().sum()

readmission_hospital_nonull = hospitalinfo[~hospitalinfo['readmission_national_comparison_footnote'].isnull()]
readmission_hospital_nonull['readmission_national_comparison_footnote'].isna().sum()

readmission_pivot = readmission_hospital_nonull.pivot_table(index=['state', 'effectiveness_of_care_national_comparison'],values=['readmission_national_comparison_footnote'])

readmission_pivot

df_Chart1 = readmission_hospital_nonull[['effectiveness_of_care_national_comparison', 'readmission_national_comparison_footnote']]

df_Chart1

df_Chart1.plot.scatter(x='effectiveness_of_care_national_comparison', y = 'readmission_national_comparison_footnote')
