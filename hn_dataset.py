#!/usr/bin/env python
# coding: utf-8

#                                          Ask HN vs Show HN

# My objective is to take the dataset from the documet "hacker_news.csv" and find which kinds of posts recieve more comments: Ask HN or Show HN, as well as seeing if older posts get more comments on average.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


hn=pd.read_csv("hacker_news.csv", parse_dates=['created_at'])


# Sorting the data to be ordered by date

# In[3]:


hn.sort_values(by='created_at', inplace=True)


# In[4]:


hn.head()


# Finding how many posts are "ask HN" or "show HN" within the dataset and subtracting them from the total number of posts.

# In[5]:


ask_hn = hn.query('title.str.startswith("Ask HN: ")')
show_hn = hn.query('title.str.startswith("Show HN: ")')
posts_left = len(hn) - len(ask_hn) - len(show_hn)


# In[6]:


print(f"There are {ask_hn['id'].count()} posts for Ask HN and {show_hn['id'].count()} posts for Show HN")


# In[7]:


print(f"Out of the {len(hn)} posts, there are {posts_left} posts left")


# In[8]:


xval=hn['created_at']
yval=hn['num_comments']


# Plotting the number of comments and their post dates to find if their is a correlation.

# In[9]:


plt.scatter(xval,yval)


# In[ ]:





# In[ ]:




