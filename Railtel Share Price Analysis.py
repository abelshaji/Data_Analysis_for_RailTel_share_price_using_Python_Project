#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\\Jessica\\Desktop\\pandas\\RAILTEL_NEW.csv')


# In[2]:


df.head(5)


# In[3]:


df.dtypes


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()
#Now we can make sure there are no null values in our data set


# In[6]:


plt.figure(figsize=(15,5))
plt.plot(df["Close"])
plt.title('Railtel Share Close Price',fontsize=12)
plt.ylabel('Price In Rupees')
    


# In[7]:


df['Volume']=df['Volume'].str.replace(',','')
#We should remove the comma to convert the data type of the volume column into float


# In[8]:


df['Volume']=df['Volume'].astype(float)


# In[9]:


df.dtypes


# In[11]:


plt.subplots(figsize=(20,10))
a=['Open','Close','Volume']
for i, col in enumerate(a):
 plt.subplot(2,3,i+1)
 sns.boxplot(df[col])
plt.show()


# In[ ]:


#from datetime import datetime
#df['Date']=pd.to_datetime(df['Date'])
#df['Date']=df['Date'].astype(datetime64)
#sb.regplot(x=to_datetime(df['Date']),y=df['Close'])


# In[12]:


df.dtypes


# In[13]:


split=df['Date'].str.split('-',expand=True)
df['day'] = split[0].astype('float')
df['month'] = split[1].astype('int')
df['year'] = split[2].astype('int')
df.head(3)
# we have seperated the date column in three columns as day,month,year


# In[14]:


df["is_quater"]=np.where(df['month']%3==0,1,0)
#Now we can seperate the data in quaterly wise to analyze the company performance when the quartely results are published


# In[15]:


df.groupby('is_quater').mean()
#prices are higher in the months which are quater end when companred with non quater months
#The volume of trade is also less in quater end months


# In[16]:


df['open-close']=df['Open']-df['Close']
df['low-high']=df['Low']-df['High']
df['target']=np.where(df['Close'].shift(-1)>df['Close'],1,0)
df['target'].value_counts()


# In[17]:


plt.pie(df['target'].value_counts().values,labels=[1,0],autopct='%1.1f%%')
plt.show()


# In[18]:


df['days']=range(248)


# In[19]:


df[['Open','Close','% Change','Volume','days']].corr()
#Correlation analysis measures the strength of the realtionship between two variables
#The correlation between close and volume is lesser than with days column


# In[22]:


#Positive Linear relationship 
sns.regplot(x='days',y='Close',data=df)


# In[ ]:


#Linear Regression


# In[24]:


from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm


# In[29]:


x=df[['days']]
y=df[['Close']]
lm.fit(x,y)


# In[31]:


lm.score(x,y)

