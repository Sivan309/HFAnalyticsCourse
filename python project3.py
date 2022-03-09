#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('NYPD_Arrest.csv') 


# In[15]:


df.info()


# In[16]:


#Find out the gender split of arrest records
df.groupby(by="PERP_SEX").count()
#Most of the arrests in the set are Male (128910), female are lower (26597)


# In[19]:


#My Question: When and where do robberies occur in this dataset
#Step 1: Filter out dataset to include only LARCENY and ROBBERY
df = df.dropna()
df2 = df[df['OFNS_DESC'].str.contains("LARCENY|ROBBERY")]
#Count of Larceny and Robbery
df2['OFNS_DESC'].value_counts()


# In[27]:


#Step 2: Figure out trends on when these crimes are most likely to happen 
#Converting date to datetime 
df2['ARREST_DATE'] = pd.to_datetime(df2['ARREST_DATE'])
df2.info()


# In[36]:


#Time Series of arrests 
Datecount = df.groupby('ARREST_DATE').size()
plt.figure(figsize = [15,10])
Datecount.plot()


# In[44]:


#Exponential Smoothing to notice any time trends 
plt.figure(figsize = [15,10])
plt.plot(Datecount, label = 'data')
plt.plot(Datecount.rolling(window=15).mean(),label = 'SMA 2 Months')
plt.legend(loc = 1)
#Using the rolling average method we can tke averages of the past 15 days to create a more smoothed line plot 
#the smoothed averages shows us that the theft is most common in February and March and towards the end of the year


# In[45]:


#Next step is to figure out where theft happens the most
df2.groupby('ARREST_BORO').count()
#We can see here that the theft happens most in Manhattan followed by Brooklyn and the Bronx


# In[ ]:




