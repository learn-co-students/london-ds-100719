#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


data = pd.read_csv('kc_house_data.csv')
data.head()


# In[3]:


data.info()


# In[4]:


data.shape


# In[5]:


data.describe()


# In[6]:


data.columns


# In[7]:


data.any().any()


# In[8]:


# tells me how much in total
data.isna().sum()


# In[9]:


#drop all null values
data.dropna(inplace=True)
data.info()


# In[10]:


data.shape


# In[11]:


data['waterfront'].unique()


# In[12]:


data['yr_renovated'].unique()


# In[13]:


#write code for value count see where there are errors

for col in list(data.columns):
    print ("the value count in {} is: /n".format(col), data[col].value_counts())


# In[14]:


data = data[(data['sqft_basement'] != '?')]


# In[15]:


data.sqft_basement.value_counts().sort_values()


# In[16]:


data['bedrooms'] = data['bedrooms'].astype('float64')
data['sqft_basement'] = data['sqft_basement'].astype('float64')

data.info()


# In[17]:


# groupbyby()
#  detecting missing data
#import seaborn as sns
#data.groupby('grade')['price'].mean()
#data.groupby(data['zipcode'].mean()
f, ax = plt.subplots(figsize=(8,6))
fig = sns.boxplot(x='grade', y='price', data=data)


# In[18]:


data['year_sold'] = data['date'].map(lambda x: x[-4:])


# In[19]:


data.yr_renovated.unique()


# In[20]:


data.info()


# In[21]:


#convert year sold to integer
data['year_sold'] = data['year_sold'].astype('int64')


# In[22]:


#using lambda function to find the age of the building by taking out yr built from yr sold
data = data.assign(age = lambda x: x['year_sold'] - x['yr_built'])
data.head()


# In[23]:


import statsmodels.api as sm

data1 = data.loc[:,['price', 'sqft_living', 'grade', 'yr_renovated', 'age', 'lat', 'long']]
x = data1.drop('price', axis=1)
y = data1['price']
x = sm.add_constant(x)
model_sm = sm.OLS(y,x)
results = model_sm.fit()
r2 = results.rsquared
r2 = r2.round(2)
print('R2 = {}'.format(r2))
est_b = results.params
print(est_b.round(4))
results.summary()


# In[24]:


data2 = data.loc[:,['price', 'sqft_living', 'grade', 'yr_renovated', 'age', 'lat', 'long']]
data2['price'] = np.log(data['price'])
data2.head()


# In[25]:


data3 = data2.loc[:,['price', 'sqft_living','yr_renovated', 'age','lat']]
x = data3.drop('price', axis=1)
y = data3['price']
x = sm.add_constant(x)
model_sm = sm.OLS(y,x)
results = model_sm.fit()
r2 = results.rsquared
r2 = r2.round(2)
print('R2 = {}'.format(r2))
est_b = results.params
print(est_b.round(4))
results.summary()


# In[26]:


data4 = data2.loc[:,['price', 'sqft_living', 'grade','age','lat','long']]

# Setting up the LEARNER
x = data4.drop('price', axis=1)
y = data4['price']


x = sm.add_constant(x)
model_sm = sm.OLS(y,x)
results = model_sm.fit()
r2 = results.rsquared
r2 = r2.round(2)
print('R2 = {}'.format(r2))
est_b = results.params
print(est_b.round(4))
results.summary()


# In[ ]:


data.head(5)


# In[ ]:


import statsmodels.api as sm

# Setting up the LEARNER
X = sm.add_constant(X)
model_sm = sm.OLS(y,X)

# Actually LEARNING
results = model_sm.fit()

# Evaluating performance
r2 = results.rsquared
r2 = r2.round(2)
print('R2 = {}'.format(r2))

# # Understanding the LEARNED model
est_b = results.params
print(est_b.round(4))


# In[ ]:


1+1


# In[ ]:




