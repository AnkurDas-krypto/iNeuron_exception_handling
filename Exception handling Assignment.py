#!/usr/bin/env python
# coding: utf-8

# #### 1. Write a function to compute 5/0 and use try/except to catch the exceptions. 

# In[1]:


def error():
    try:
        a = int(input('enter a'))
        b = int(input('enter b'))
        c = a/b
        print(c)
    except Exception:
        print('division by 0 error')
        
error() 


# #### 2. Implement a Python program to generate all sentences where subject is in  ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in  ["Baseball","cricket"]. 

# In[3]:


subjects=["Americans ","Indians"] 
verbs=["play","watch"] 
objects=["Baseball","Cricket"] 


lst = [subjects[i]+ ' ' +verbs[j]+ ' ' +objects[k] for i in range(2) for j in range(2) for k in range(2)]         

for i in lst:
    print(i)


# In[ ]:




