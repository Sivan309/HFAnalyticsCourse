#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/niteen11/DataAnalyticsAcademy/master/Python/dataset_diabetes/diabetic_data.csv')
df


# In[ ]:


#Turning the list into a df
df1 = pd.DataFrame (df)
df1.dtypes


# In[ ]:


#Isolating descriptive Stats with those that take diabetes medication
df1 = df1[['encounter_id', 'race', 'gender', 'age', 'weight', 'time_in_hospital', 'diabetesMed']]
df1


# In[ ]:


df2 = df1[df1['diabetesMed'].str.contains("Y")]
df2 = df[['diabetesMed', 'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'examide', 'citoglipton', 'insulin',]]
df2


# In[ ]:


#Finding the most used drugs amongst those that also take Diabetes Medication
#Any code that has an error would mean that there is no one that has Steady or Up for that drug
df2['metformin'].value_counts()['Steady']


# In[ ]:


df2['repaglinide'].value_counts()['Steady']


# In[ ]:


df2['nateglinide'].value_counts()['Steady']


# In[ ]:


df2['chlorpropamide'].value_counts()['Steady']


# In[ ]:


df2['glimepiride'].value_counts()['Steady']


# In[ ]:


df2['acetohexamide'].value_counts()['Steady']


# In[ ]:


df2['glipizide'].value_counts()['Steady']


# In[ ]:


df2['glyburide'].value_counts()['Steady']


# In[ ]:


df2['tolbutamide'].value_counts()['Steady']


# In[ ]:


df2['pioglitazone'].value_counts()['Steady']


# In[ ]:


df2['rosiglitazone'].value_counts()['Steady']


# In[ ]:


df2['acarbose'].value_counts()['Steady']


# In[ ]:


df2['miglitol'].value_counts()['Steady']


# In[ ]:


df2['troglitazone'].value_counts()['Steady']


# In[ ]:


df2['examide'].value_counts()['Steady']


# In[ ]:


df2['citoglipton'].value_counts()['Steady']


# In[ ]:


df2['insulin'].value_counts()['Steady']
#Insulin and glipizide are the most common drugs amongst Diabetes patients in this set 


# In[ ]:


#Focusing on demographic details for those who take Diabetes medicine 
df3 = df1[df1['diabetesMed'].str.contains("Y")]
df3


# In[ ]:


#Count of patients in the different age Groups that are taking Diabetes Meds
#We see that most patients are within 50-90 range
df1.groupby('age').size()


# In[ ]:


#Creating a dataframe with the given groupby information
Age = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
Weight = [161, 691, 1657, 3775, 9685, 17256, 22483, 26068, 17197, 2793]
list_of_tuples = list(zip(Age, Weight))

Weight = pd.DataFrame(list_of_tuples, 
                  columns = ['Age', 'Weight'])
Weight


# In[ ]:


#Count of patients gender that are taking Diabetes Meds
#We see that the distrribution is close to even between Males and Females 

df.groupby('gender').size()


# In[ ]:


#Count of patients race that are taking Diabetes Meds
#We see that most diabetes patients in the set are African American or Caucasian
df.groupby('race').size()


# In[ ]:


#Count of patients by weight group 
#Most patients weight more than 50 lbs. 
df.groupby('weight').size()


# In[ ]:




