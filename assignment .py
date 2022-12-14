#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# 

# #### Import NumPy as np

# In[3]:


import numpy as np 


# #### Create an array of 10 zeros 

# In[9]:


import numpy as np 
a=np.zeros(10)
a


# #### Create an array of 10 ones

# In[11]:


a=np.ones(10)
a


# #### Create an array of 10 fives

# In[17]:


a=np.ones(10)*5
a


# #### Create an array of the integers from 10 to 50

# In[28]:


a=np.arange(10,51)
a


# #### Create an array of all the even integers from 10 to 50

# In[29]:


a=np.arange(10,51,2)
a


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[32]:


a1=np.arange(0,9).reshape(3,3)
a1


# #### Create a 3x3 identity matrix

# In[33]:


a=np.identity(3)
a


# #### Use NumPy to generate a random number between 0 and 1

# In[36]:


a=np.empty(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[37]:


a=np.empty(25)
a


# #### Create the following matrix:

# In[41]:


a=np.arange(0.01,1.01,0.01).reshape(10,10)
a


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[42]:


a=np.linspace(0, 1, 20)
a


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[62]:


mat = np.arange(1,26).reshape(5,5)
mat


# # WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# # BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# # BE ABLE TO SEE THE OUTPUT ANY MORE
# 

# In[64]:


x=mat[2:,1:]
print(x)


# In[40]:





# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[70]:


x=mat[3][4]
x


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[77]:


x=mat[0:3,1].reshape(3,1)
print(x)


# In[42]:





# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[83]:


x=mat[-1,:]
x


# In[46]:





# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[85]:


x=mat[-2:,:]
x


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[87]:


s=mat.sum()
s


# #### Get the standard deviation of the values in mat

# In[93]:


standard=mat.std()
standard


# #### Get the sum of all the columns in mat

# In[94]:


s=mat.sum(axis=0)
s


# In[53]:





# In[ ]:





# # Great Job!
