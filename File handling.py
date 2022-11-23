#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('ls', '')


# In[1]:


get_ipython().run_line_magic('ls', '')


# In[2]:


f=open('readme.txt',"r+")
f.name


# In[3]:


with open('readme.txt','w') as f:
    f.write('Create a new text file!')


# In[5]:


with open('readme.txt','w') as f:
    f.write('I can write lines at current cursor')     #overide last statement


# In[6]:


try:
    with open('docs/readme1.txti','r') as f:
        f.write('Create a new file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")


# In[7]:


f.close()


# In[8]:


f1=open('readme.txt','w')


# In[10]:


f1.write("I can write lines at current cursor")


# In[11]:


f=open('readme.txt','w')


# In[12]:


f.write("I can write lines at current cursor.")


# In[13]:


f.close()


# In[14]:


f=open('readme.txt','w')


# In[15]:


f.seek(5)


# In[21]:


f=open('readme.txt','w')
f.write('I can write lines at current cursor')


# In[22]:


f.seek(5)


# In[23]:


f.close()


# In[2]:


f= open('readme.txt','w')


# In[3]:


f.write("I love python")


# In[4]:


f.close()


# In[1]:


f=open('readme.txt','r')


# In[9]:


f.seek(3)


# In[10]:


f.close()


# In[11]:


get_ipython().run_line_magic('ls', '')


# In[12]:


import os
os.remove('readme.txt')


# In[13]:


get_ipython().run_line_magic('ls', '')


# In[14]:


f=open('readme.txt','r')


# In[19]:


with open('handle.docs','w') as file1:
    file1.write("Hello, you are welcome to the file name 'handle', We are learning file handling in python.")


# In[20]:


file1.close()


# In[25]:


file1=open('handle.docs','w')


# In[26]:


file1.write("Good morning everyone to 'handle'")


# In[27]:


get_ipython().run_line_magic('ls', '')


# In[32]:


import os
os.remove('handle.docs')


# In[33]:


get_ipython().run_line_magic('ls', '')


# In[34]:


file1.close()


# In[35]:


import os
os.remove('handle.docs')


# In[36]:


get_ipython().run_line_magic('ls', '')


# In[37]:


with open('xyz.txt','w') as f:
    f.write("Hello welcome to file handling")


# In[41]:


f=open('xyz.txt', 'w')
f.write("I am writning the lines to xyz file")


# In[44]:


pwd()


# In[45]:


os.listdir('C:\\Users\\SHUBHANGINI')


# In[46]:


os.getcwd()


# In[47]:


os.getcwd()


# In[48]:


import logging


# In[49]:


logging.basicConfig(filename = "test.log" ,level = logging.INFO)


# In[50]:


logging.info("this is my info log ")
logging.warning("this is my warning log ")
logging.error("this is my error log")


# In[51]:


logging.shutdown()


# In[52]:


pwd()


# In[54]:


DEBUG 
INFO
WARNING
ERROR
CRITICAL


# In[62]:


import logging


# In[65]:


logging.basicConfig(filename = "test2.log" , level = logging.info)


# In[66]:


logging.shutdown()


# In[9]:


with open('file1.txt', 'w') as f:
    f.write("Welcome to file1!")


# In[10]:


f.close()


# In[11]:


f=open('file1.txt','w')


# In[12]:


f.write("I am write to file1")


# In[13]:


f.close()


# In[14]:


f=open('file1.txt','r+')


# In[15]:


f.read()


# In[16]:


with open('file2.txt','w') as f1:
    f1.write("Hello everyone!")


# In[17]:


f.close()


# In[18]:


f=open('file2.txt','r+')


# In[19]:


f.read()


# In[20]:


f=open('file2.txt','w')


# In[21]:


f.write("I am writing to file2")


# In[22]:


f.close()


# In[23]:


f=open('file2.txt','r+')


# In[24]:


f.read()


# In[25]:


with open('file3.txt','w') as f3:
    f3.write("Hello everyone!")


# In[26]:


f3.close()


# In[27]:


f3=open('file3.txt','r+')


# In[29]:


f3.read()


# In[30]:


f3.write("I am writing to file3")


# In[32]:


f3.close()


# In[33]:


f3=open('file3.txt','r+')


# In[35]:


f3.read()


# In[4]:


import logging


# In[5]:


logging.basicConfig(filename='test77.log', level = logging.info)


# In[1]:


import os
os.remove('file3.txt')


# In[2]:


get_ipython().run_line_magic('ls', '')


# In[5]:


import os
os.remove('test5.txt')


# In[6]:


get_ipython().run_line_magic('ls', '')


# In[7]:


import os
os.remove('class1.txt')


# In[8]:


get_ipython().run_line_magic('ls', '')


# In[9]:


import os
os.remove('file1.txt')


# In[10]:


import os
os.remove('file2.txt')


# In[11]:


get_ipython().run_line_magic('ls', '')


# In[12]:


import os
os.remove('xyz.txt')


# In[10]:


class Pare():
    def __init__(self,name,age,id):
        self.a=name
        self.b=age
        self.c=id
        
    def test(self):
        with open('file2.txt','w') as f:
            f.write("Hello, welcome to the file file2!")
        f.close()
        print(self.a,self.b,self.c)
        
class chil(Pare):
    
    def test(self):
            f=open('file2.txt','r+')
            f.read()

m=Pare('shubh',23,343)
m.test()            


# In[7]:


class P1:
    def test():
        with open('files.txt','w') as f:
            f.write("Hello welcome to file files!")
        f.close()
        print(3)
        
class C1(P1):
    def test():
        print(3)
        f=open('files.txt','r+')
        f.read()  
        print(3)
        
l=P1
l.test()


# In[2]:


with open('files.txt','w') as f:
    f.write("Hello welcome to file files!")
f.close()
f=open('files.txt','r+')
f.read()       


# In[ ]:




