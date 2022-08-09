#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
iris_dataset=load_iris()


# In[11]:


#We have 4 parameter sepallength,sepalwidth,petallength,petalwidth
print("keysof iris",iris_dataset.keys())


# In[12]:


print(iris_dataset['DESCR'][:]+"\n...")


# In[14]:


print("TargetVariable",iris_dataset['target_names'])


# In[17]:


print("FeaturesVariable",iris_dataset['feature_names'])


# In[19]:


print("Type of Data",type(iris_dataset['data']))


# In[24]:


print("Entries of Data",iris_dataset['data'].shape)# 150 rows of data and 4 columns./attributes of data


# In[26]:


print("Record of Data",iris_dataset['data'][:])


# In[27]:


print("Type of Data",type(iris_dataset['target']))


# In[28]:


print("Entries of Data",iris_dataset['target'].shape)


# In[29]:


print("Target:",iris_dataset['target'])


# In[60]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=1)#here X_train is (sepallength,sepalwidth,petallength,petalwidth)(#here Y_train in traget)
#(here X_test is for 30% test data which is (sepallength,sepalwidth,petallength,petalwidth)
#(here Y_test is for 30% testdata in traget)


# In[61]:


print("X_train shape",X_train.shape)
print("Y_train shape",y_train.shape)


# In[62]:


print("X_train shape",X_test.shape)#unseen record sample without Replacement 
print("Y_train shape",y_test.shape)


# In[63]:


# Visualization 
#Bivarient Analysics
iris_dataframe=pd.DataFrame(X_train,columns=iris_dataset.feature_names)
#Scatter Plot
pd.plotting.scatter_matrix(iris_dataframe ,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=0.8)


# In[64]:


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)


# In[65]:


X_new=np.array([[6.8,2.8,4.8,1.4]])
print("X_newShapew",X_new.shape)


# In[66]:


prediction=knn.predict(X_new)
print("Prediction",prediction)
print("Prediction targetName",iris_dataset['target_names'][prediction])


# In[67]:


y_predict=knn.predict(X_test)
print("Test the prediction",y_predict)


# In[68]:


print("Test set score:{:.2f}".format(np.mean(y_predict==y_test)))


# In[ ]:





# In[ ]:




