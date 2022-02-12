#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd 
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')
df


# In[76]:


#Changing Mean Score to a Numeric Value
df["Mean Score"] = pd.to_numeric(df["Mean Score"])
df["Total Tested"] = pd.to_numeric(df["Total Tested"])


# In[77]:


#Extracting only the Columns I will be using for the analysis
df1 = df[['School Name', 'School Level', 'Regents Exam','Year','Mean Score', 'Total Tested']]
df1 = df1.replace({np.nan: ''})
df1


# In[50]:


#Filtering only for the Icahn School name 
df2 = df1[df1['School Name'].str.contains("Icahn")]
df2

column = df2["Year"]
max_value = column.max()
max_value

column = df2["Year"]
min_value = column.min()
min_value


#The icahn school is a K-8 school that has data from 2015 - 2017 in this set


# In[44]:


#Extarcting the Mean score for Students at Icahn that have taken the Common Core Algebra
df3 = df2[df2['Regents Exam'].str.contains('Algebra')]
df3
df3["Mean Score"].mean()
#The mean score for Students at Icahn school for the Core Algebra test is 83%


# In[45]:


#Extarcting the Mean score for Students at Icahn that have taken the Living Envionment
df4 = df2[df2['Regents Exam'].str.contains('Living')]
df4
df4["Mean Score"].mean()
#The mean score for Students at Icahn school for the Living Environment test is 81%


# In[47]:


#Extarcting the Mean score for Students at Icahn that have taken the History Course
df5 = df2[df2['Regents Exam'].str.contains('History')]
df5
df5["Mean Score"].mean()
#There are no results for students who have take the History exam at the Icahn school


# In[ ]:


#How many tests were taken by exam
df2.groupby(by="Regents Exam").sum()


# In[56]:


#Comparing Icahns Test scores in Algebra and Environment to the rest of the City 
df6 = df1[df1['Regents Exam'].str.contains('Algebra')]
df6["Mean Score"].mean()

#The mean city score for the same Algebra exam is 64, much less than that of Icahn's 83%


# In[58]:


#Comparing Icahns Test scores in Algebra and Environment to the rest of the City 
df7 = df1[df1['Regents Exam'].str.contains('Environment')]
df7["Mean Score"].mean()

#The mean city score for the same Algebra exam is 69, much less than that of Icahn's 81%
#Icahn performs siginificantly better than the rest of the city in these two exams 


# In[61]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[85]:


#Pie Chart of Total exams taken across all schools 
df.groupby(['Regents Exam']).sum().plot(kind='pie', y='Total Tested')


# In[63]:


#Create a histogram by Deciles of Mean Algebra score at Icahn
df2['Mean Score'].hist(bins = 10)
#Through this visual we can see that most of the scores for Icahn's Algebra exam fall on the outsides of the curve with most data points being around the 75 and 85-90 level


# In[65]:


#Creating a boxplot to further improve on the effeciency of the Historgram Model
sns.boxplot(x=df2["Mean Score"])
#Here we can see better the distibution of mean scores at Icahn for te Algebra Exam 
#The Min is 74 and Max is 90 with the majority of the data falling between 78-86%


# In[71]:


#Comparing the boxplot of Icahn's Algebra to the rest of the city
sns.boxplot(x=df6["Mean Score"])
#Here we can see that the majority of the city's result are scoring lower than that of Icahn 
#We can also see that the range of city results varies between 20 and 100 with many outliers 
#The middle line shows clearly that Icahn performs better than the rest of the city 

