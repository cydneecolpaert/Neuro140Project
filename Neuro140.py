#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import sys, os


# In[4]:


import urllib


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


ls


# In[7]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


# In[8]:


import numpy as np


# In[104]:


img = cv2.imread('Images/test15.jpg')


# In[105]:


#img = np.full((100,80,3), 12, np.uint8)


# In[106]:


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[107]:


faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# In[108]:


faces


# In[109]:


faces = face_cascade.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=True)


# In[110]:


faces[0]


# In[111]:


faces[2]


# In[112]:


for(x,y,w,h) in faces[0]:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (255,0,0), 2)


# In[113]:


print(img.shape)
plt.imshow(gray, cmap='gray')
plt.show


# In[ ]:


print(cv2.imshow)
cv2.imshow('img', img)
plt.imshow(img)
plt.show
cv2.waitKey()


# In[ ]:




