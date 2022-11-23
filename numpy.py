#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


import numpy as np


# In[40]:


import array as arr


# In[4]:


l=[1,2,'shu','bhu',45.5]
type(l)


# In[7]:


np.array(l)


# In[11]:


type(np.array(l))    #numpy.n dimentional array


# In[18]:


np.array([[1,2],[3,4],[5,6],['s','r']])


# In[19]:


np.array([1,2,3])


# In[20]:


np.array([1,2,3],ndmin=3)


# In[21]:


type(np.array([1,2,3],ndmin=3))


# In[26]:


np.array([1,2,3], dtype= str)


# In[27]:


np.array([1,2,3], dtype= complex)


# In[51]:


a=np.array([(1,2),(3,4)])


# In[52]:


a[1][1]


# In[54]:


a[0][1]


# 

# 

# In[55]:


l=[3,4,5,6,7]


# In[56]:


np.asarray(l)


# In[57]:


np.asanyarray(l)


# In[58]:


np.array(l)


# In[61]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[62]:


arr[1][2]


# In[63]:


arr[1][2]=40


# In[64]:


arr


# In[66]:


arr[0:10]


# In[67]:


arr[-1]


# In[68]:


arr[2]


# In[69]:


arr[0]


# In[70]:


for i in arr:
    print(i)


# In[2]:


import math


# In[3]:


import numpy as n


# In[4]:


import array as ar


# In[4]:


n.array([12,34,56,'shubh'])


# In[6]:


type(n.array([12,34,56,'shubh']))


# In[9]:


n.array([12,34,56,],dtype='complex')


# In[4]:


n.fromfunction(lambda i,j: i==j, (4,4))


# In[5]:


n.fromfunction(lambda i,j: i*j,(3,3))


# In[6]:


n.fromfunction(lambda i,j : i/j, (3,3))


# In[9]:


n.fromstring('1,2,3,4',sep=',',dtype=float)


# In[11]:


n.arange(6)


# In[12]:


n.arange(6.6)


# In[15]:


n.arange(6,10,2)    #slicing


# In[17]:


n.linspace(3,8)


# In[19]:


n.linspace(1,2,3)


# In[20]:


n.zeros(5)


# In[21]:


n.ones(5)


# In[23]:


n.zeros((2,5,3))


# In[24]:


n.ones((2,3,2))+5


# In[26]:


n.eye(3)    #identity matrix


# n.empty(6

# In[95]:


n.empty(8)


# In[30]:


n.linspace(2,4,4,axis=0)


# In[31]:


n.logspace([2,3],4)


# In[35]:


d=n.linspace(4,5,40)


# In[36]:


d


# In[37]:


d.shape


# In[41]:


d.reshape(10,4)


# In[43]:


d.reshape(20,2)


# In[47]:


n.random.rand(3)    #random data creating  in b/w 0-1


# In[48]:


n.random.rand(5,4)


# In[49]:


n.random.rand(2,2,3)


# In[51]:


n.random.randint(4)


# In[53]:


n.random.randint((5,6),40)


# In[55]:


n.random.randn(4,4)


# In[118]:


ar=n.random.randint(3,9,(3,3))


# In[119]:


ar


# In[120]:


ar.reshape(1,1,9)


# In[121]:


ar.reshape(3,3,1)


# In[122]:


ar.reshape(3,-1)


# In[123]:


ar.reshape(3,-9988)


# In[124]:


ar.max()


# In[125]:


ar.min()


# In[126]:


ar=n.random.randint(4,100,(5,5))


# In[127]:


ar


# In[128]:


ar[3:,3:]   #will eliminate matrix in 3*3 and give rest matrix entries


# In[129]:


ar[:,[1,3]]


# In[130]:


ar[ar>50]


# In[131]:


ar>50


# In[132]:


ar*ar


# In[133]:


ar1=n.random.randint(2,5,(2,2))


# In[134]:


ar2=n.random.randint(2,5,(2,2))


# In[135]:


ar1*ar2


# In[136]:


ar1@ar2


# In[137]:


ar1


# In[138]:


ar2


# In[139]:


ar**2


# In[140]:


ar/0


# In[141]:


n.log(ar)  #log values for ar matrix


# In[142]:


n.random.seed(1)
n.random.rand(2,4)


# In[6]:


n.random.seed(11)
n.random.rand(3,5)


# In[7]:


n.random.seed(11)
n.random.rand(3,5)


# In[8]:


n.random.seed(3)
n.random.rand(2,2)


# In[9]:


n.random.seed(3)
n.random.rand(2,2)


# In[10]:


n.random.rand(2,2)


# In[15]:


n.random.seed(12)
n.random.rand(2,2)


# In[18]:


ar


# In[19]:


import math
import numpy as np
import array as arr


# In[20]:


np.array([1,2,3,4])


# In[21]:


arr=np.array([[1,2],[3,4],[5,6],[7,8],['s','p']])


# In[22]:


arr


# In[28]:


arr[4][0]


# In[29]:


type(arr)


# In[32]:


np.array([1,2,3,4],dtype='str')


# In[34]:


np.fromfunction(lambda i,j:i==j,(3,3))


# In[41]:


np.fromfunction(lambda i,j:i*j,(6,6))


# In[42]:


np.fromfunction(lambda i,j:i/j,(5,5))


# In[45]:


np.fromstring('1,2,3,4',sep=',',dtype=complex)


# In[47]:


n.arange(4)


# In[50]:


n.arange(3.4)


# In[52]:


n.arange(3,9,2)


# In[54]:


n.linspace(3,2)


# In[58]:


n.linspace(3,5,6)


# In[60]:


n.zeros(4)+5


# In[63]:


n.ones(5)


# In[66]:


n.zeros((2,5,3))


# In[73]:


n.ones((2,5,3))+4


# In[74]:


n.eye(5)


# In[94]:


n.empty(8)


# In[102]:


n.logspace([2,5],4)


# In[105]:


k=np.linspace(2,3,30)


# In[106]:


k


# In[108]:


k.shape


# In[111]:


k.reshape(10,3)


# In[ ]:




