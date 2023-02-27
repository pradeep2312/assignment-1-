#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


assign = pd.read_csv("Desktop\StudentsPerformance.csv")


# In[4]:


assign


# In[5]:


# Scatter plot with parental level of education against math score
plt.scatter(assign['parental level of education'], assign['math score'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('parental level of education')
plt.ylabel('math score')
 
plt.show()


# In[15]:


# Bar chart with day against tip
plt.bar(assign['parental level of education'], assign['math score'])
 
plt.title("Bar Chart")
 
# Setting the X and Y labels
plt.xlabel('parental level of education')
plt.ylabel('math score')
 
# Adding the legends
plt.show()


# In[17]:


# histogram of reading score
plt.hist(assign['reading score'])
 
plt.title("Histogram")
 
# Adding the legends
plt.show()


# In[18]:


import seaborn as sns


# In[20]:


# draw lineplot
sns.lineplot(x="gender", y="reading score", data=assign)
 
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')
 
plt.show()


# In[21]:


sns.barplot(x='gender',y='reading score', data=assign,
            hue='lunch')
 
plt.show()


# In[ ]:




