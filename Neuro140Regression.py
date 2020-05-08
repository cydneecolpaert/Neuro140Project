#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


from scipy import stats


# In[4]:


import numpy as np


# In[5]:


weight = np.array([0, 0, 0, 0, 0, 0, 0, 7.716403, 7.827261, 8.40504, 
                   8.41837, 8.51831, 8.57784, 9.12925, 9.66138])


# In[6]:


meanrq = np.array([9.35714, 7.71429, 4.5, 4.14286, 4, 3.28571, 3.14286, 6.92857, 6.35714, 7.14286, 
                   7.14286, 6.92857, 5.42857, 9.85714, 9.64286])


# In[9]:


plt.plot(weight, meanrq, 'o' )
plt.title('Unedited Mean Realistic Quality vs Output Weight')
plt.ylabel('Mean Realistic Quality')
plt.xlabel('Weight - 100')


# In[11]:


m, b = np.polyfit(weight, meanrq, 1)


# In[12]:


m


# In[13]:


b


# In[15]:


plt.plot(weight, m*weight + b)


# In[17]:


eweight = np.array([7.716403, 7.827261, 8.40504, 8.41837, 8.51831, 8.57784, 9.12925, 9.66138])


# In[18]:


emeanrq = np.array([ 6.92857, 6.35714, 7.14286, 7.14286, 6.92857, 5.42857, 9.85714, 9.64286])


# In[20]:


plt.plot(eweight, emeanrq, 'o' )
plt.title('Edited Mean Realistic Quality vs Output Weight')
plt.ylabel('Mean Realistic Quality')
plt.xlabel('Weight - 100')


# In[21]:


em, eb = np.polyfit(eweight, emeanrq, 1)


# em

# In[22]:


em


# In[23]:


eb


# In[24]:


plt.plot(eweight, em*eweight + eb )


# In[33]:


slope, intercept, r_value, p_value, std_err = stats.linregress(eweight,emeanrq)


# In[34]:


print ("r-squared:", r_value**2)


# In[35]:


print (p_value)


# In[36]:


print (slope)


# In[37]:


print (std_err)


# In[38]:


slope, intercept, r_value, p_value, std_err = stats.linregress(weight,meanrq)


# In[39]:


print ("r-squared:", r_value**2)


# In[40]:


print (p_value)


# In[41]:


print (slope)


# In[42]:


print (std_err)


# In[ ]:





# In[ ]:




