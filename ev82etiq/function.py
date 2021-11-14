#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from ipywidgets import interact, fixed


# In[2]:


def im_resized(x, height, ratio=False):
    image = Image.open(im)
    w,h = image.size
    
    if ratio: # keep aspect ratio
        #resize
        asp_ratio = (w/h)
        new_width = int(asp_ratio * height)
        resized = image.resize((new_width,height))
    
    # resize image to a square of dimension height*height
    else: 
        resized = image.resize((height, height))
    return resized


# In[3]:


im = r"C:\Users\Roarke\Desktop\maot classes and stuff\DSSS\final\ev82etiq\data"


# In[4]:


interact(im_resized, x=fixed(im), height=(100,1000,100), ratio=[True, False])


# In[ ]:




