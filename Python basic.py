#!/usr/bin/env python
# coding: utf-8

# In[1]:


m = [2,3,4, 'shubh', 'xyz', (2+45)]


# In[2]:


m


# In[3]:


m[::-1]


# In[4]:


word = str(input("Enter any word: "))
if(word[::-1]==word):
    print("Word is pelindrome.")
else:
    print("Word is not pelindrome.")


# In[1]:


for i in range(4):
    print(i)


# In[2]:


l=[3,4,5,6]
for i in l:
    print(i)


# In[6]:


for i in range(1,6):
    print (i*' * ')


# In[7]:


l=["apple","banana","orange"]
for i in l:
    print(i)


# In[11]:


for i in range(0,20,5):
 print(i)


# In[12]:


l=[2,3,5,7]
for i in l[::-1]:
    print(i)


# In[13]:


word = str(input("Enter any word: "))
for i in word[::-1]:
    print(i)
    


# In[20]:


fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if i=="banana": 
        break


# In[21]:


fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if i=="banana": 
        pass


# In[22]:


fruits=["apple","banana","orange"]
for i in fruits:
    if i=="banana": 
        continue
    print(i)


# In[23]:


for i in range(6):
    print(i)
else:
    print("Finally finished")


# In[11]:


l=[1,2,3,4]
m=[5,6,7,8]
for i in l:
    for j in m:
        print(i,j)


# In[12]:


for i in range(6):
    for j in range(i+1):
        print('*',end=" ")
    print()


# In[13]:


num= int(input(" Enter any number:"))
for i in range(num):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[14]:


num=int(input("Enter any number: "))
for i in range(num):
    for j in range(i+1):
        letter=chr(65+i)
        print(letter,end=" ")
    print()


# In[15]:


num=int(input("Enter any number: "))
for i in range(num):
    for j in range(i+1):
        letter=chr(65+j)
        print(letter,end=" ")
    print()


# In[16]:


num= int(input(" Enter any number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[4]:


a=1
while a<6:
    print(a)
    a=a+1


# In[5]:


a=1
while a<6:
    print(a)
    if a==4:
        break
    a=a+1


# In[1]:


a=1
while a<6:
    print(a)
    a=a+1
    if a==4:
        continue


# In[2]:


num= int(input("Enter any number: "))
i=1
while i<=num:
    print((num-i),"*"*i)
    if i==4:
            break


# In[1]:


n=int(input("Enter any number:"))
for i in range(1,11):
        print(n,"*",i,"=",n*i)


# In[32]:


h=float(input("Enter your height(in m): "))
w=float(input("Enter your weight(in kg): "))
print("Your BMI is ", w/(h*h))


# In[35]:


h=float(input("Enter your height(in m): "))
w=float(input("Enter your weight(in kg): "))
bmi=w/(h*h)
if bmi<20:
    print("Your BMI is ",bmi,", You are underweight.")
elif bmi<25:
    print("Your BMI is ",bmi,", You are Normal.")
elif bmi<30:
    pritn("Your BMI is ",bmi,", You are overweight.")
else:
    print("Your BMI is ",bmi,", You have obesity")


# In[ ]:




