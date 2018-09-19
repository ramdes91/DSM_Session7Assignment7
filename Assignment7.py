
# coding: utf-8

# In[4]:


import numpy as np
def moving_average(a,k):#a is the input array and k is the window#
    temp=np.cumsum(a,dtype=float)
    temp[3:]=temp[3:]-temp[:-3]
    return temp[3-1:]/3

lst=[3,5,7,2,8,10,11,65,72,81,99,100,150]#input#
a = np.array(lst)

op_array = moving_average(a,k=3)#output#
print("Moving average of",lst,"are:\n")
print("Output:\n",op_array)

