#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(4):
    print(i)


# In[2]:


l=[3,4,5,6]
for i in l:
    print(i)


# In[9]:


for i in range(1,6):
    print (i*'*')


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


# In[7]:


l=[1,2,3,4]
m=[5,6,7,8]


# In[132]:


for i in range(6):
    for j in range(i+1):
        print('*',end=" ")
    print()


# In[135]:


num= int(input(" Enter any number:"))
for i in range(1,num):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[133]:


num=int(input("Enter any number: "))
for i in range(num):
    for j in range(i+1):
        letter=chr(65+i)
        print(letter,end=" ")
    print()


# In[136]:


num=int(input("Enter any number: "))
for i in range(num):
    for j in range(i+1):
        letter=chr(65+j)
        print(letter,end=" ")
    print()


# In[138]:


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


# In[ ]:


num= int(input("Enter any number: "))
i=1
while i<=num:
    print((num-i),"*"*i)


# In[10]:


n=int(input("Enter any number:"))
for i in range(1,11):
        print(n,"*",i,"=",n*i)


# In[32]:


h=float(input("Enter your height(in m): "))
w=float(input("Enter your weight(in kg): "))
print("Your BMI is ", w/(h*h))


# In[18]:


h=float(input("Enter your height(in m): "))
w=float(input("Enter your weight(in kg): "))
bmi=w/(h*h)
if bmi<20:
    print("Your BMI is ",bmi,", You are underweight.")
elif bmi<25:
    print("Your BMI is ",bmi,", You are Normal.")
elif bmi<30:
    print("Your BMI is ",bmi,", You are overweight.")
else:
    print("Your BMI is ",bmi,", You have obesity")


# In[139]:


num=int(input("Enter any number: "))
for i in range(1,num):
    for j in range(1,num):
        print("*",end=" ")
    print()


# In[3]:


m=[2,3,4,5]


# In[5]:


type(m)


# In[6]:


l=[3,4,5,'shubh',(8+8j)]


# In[7]:


l


# In[8]:


print(l)


# In[9]:


l[3]


# In[11]:


for i in l:
    print(i)


# In[12]:


l[2]=100


# In[13]:


l


# In[16]:


l1=[[2,3,4],[4,5,6]]
l2=[[2,4,5],[4,5,7]]
l1+l2


# In[15]:


a=l1.append(l2)
print(a)


# In[18]:


l2[1][0]


# In[19]:


t=(2,3,4)
print(t)


# In[21]:


t[1]


# In[22]:


t=[3,4,'shubh',[5,6],(7,8,"shubhu","nck")]


# In[25]:


t[4][3]


# In[26]:


t1=(4,5,'shubh',[6,7])


# In[30]:


t1[3][0]=8


# In[31]:


t1


# In[32]:


#sets


# In[33]:


s={1,2,34,"shubh","shubhu",'xyz'} #set is unordered and cant repeat the values.


# In[34]:


s


# In[36]:


a={1,2,3,'shubh',(8,9,'xyz')} # set doesn't include list elements.


# In[38]:


dict1={1:"shubh",2:'k1',3:'xyz',4:[3,4,5]}


# In[39]:


dict1


# In[41]:


dict1[2]


# In[17]:


dict1={1:[3,5,'xy'],2:'shubh',3:(6,7,8),4:{6,7,'haj','hhjk'}}


# In[47]:


x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "Children":("Ann","Billy"),
    "Pets":None,
    "Cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}


# In[48]:


x


# In[66]:


x['Cars'][0]['mpg']


# In[8]:


s={
  "colors": [
    {
      "color": "black",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,255,1],
        "hex": "#000"
      }
    },
    {
      "color": "white",
      "category": "value",
      "code": {
        "rgba": [0,0,0,1],
        "hex": "#FFF"
      }
    },
    {
      "color": "red",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,0,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "blue",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [0,0,255,1],
        "hex": "#00F"
      }
    },
    {
      "color": "yellow",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "green",
      "category": "hue",
      "type": "secondary",
      "code": {
        "rgba": [0,255,0,1],
        "hex": "#0F0"
      }
    },
  ]
}


# In[9]:


s


# In[12]:


s["colors"][0]["code"]["rgba"][2]


# In[23]:


l=[1,2,3,4]
m=[1,5,3,4]
for i in l:
    for j in m:
       if i==j:
            print(i)


# In[6]:


for i in range(1,6):
    for j in range(1,i):
        print("*",end=" ")
    print()


# In[2]:


dict1={1:"shubh",2:"jsk",3:"srp",4:"kcjj",5:89}


# dict1

# In[3]:


dict1


# In[9]:


for i in dict1:
    dict1.values()
print(dict1.values())
print(dict1.keys())


# In[13]:


l=[2,3,45,6,'ncjk',"dks",6+6j,[1,2]]


# In[32]:


for i in l:
    if type(i)==int:
        print(i)
    if type(i)==list:
        print(i)


# In[26]:


l=[]
l1=[3,4,5,"shubh","kcj",67]
for i in l1:
    if type(i)==int:
        a=i
    else:
        continue
    l.append(a)
print(l)


# In[1]:


a=["apple","orange","mango"]
b=["chikoo","banana","lichi"]
a.append(b)
print(a)


# In[2]:


a=[2,3,4,5]
a.append(6)
print(a)


# In[14]:


dict1={1:"shubh",2:"jsk",3:"srp",4:"kcjj",'nc':"hjkb",5:89}
for i in dict1.values():
    print(i)


# In[22]:


l=["name","emailid","phone","address"]
for i in l:
    print(i +"shubh")


# In[25]:


l=[3,4,5,6,"shubh",6+6j,9,9]
s="shubh"
for i in l:
    if l=="l":
        break
    print(i)
else:
    print(" Don't print if its not printing my name.")


# In[31]:


l= "shubh"
for i in l:
    if i=='b':
        break
    print(i)


# In[25]:


l=[]
l1=[3,4,5,"shubh","kcj",67]
for i in l1:
    if type(i)==int:
        a=i
    else:
        continue
    l.append(a)
print(l)


# In[104]:


l=[1,2,3,4,"fdg",5,"dj",[6,7,8,"dxj"],9]
m=[]
for i in l: 
    if type(i)==int:
        a=i
        m.append(a)
    if type(i)==list:
        for j in i:
            if type(j)==int:
                b=j
                m.append(b)
print(m)


# In[21]:


def test():
    print("shubh")


# In[13]:


test()


# In[14]:


def test1():
    print("hello world")


# In[15]:


test1()


# In[16]:


def name():
    print("shubhangini")


# In[17]:


name()


# In[23]:


def test2(a):
    print(a)
test2(2)


# In[31]:


a=int(input("Enter any value of a: "))
b=int(input("Enter any value of b: "))
def test3(a,b):
    print(a+b,a*b,a/b,a-b)
test3(a,b)


# In[38]:


def add(a,b):
    """This is the function of addition of two numbers"""   #Docstring defined in tripple quotes
    print(a+b)
add(3,4)


# In[40]:


def sub(a,b):
    """This is the function of subtraction of two numbers"""
    print(a-b)
sub(3,4)


# In[41]:


def mult(a,b):
    """This is the function of multiplication of two numbers"""
    print(a*b)
mult(3,4)


# In[43]:


def div(a,b):
    """This is the function of division of two numbers"""
    print(a/b)
div(3,4)


# In[44]:


div(4,5)


# In[45]:


sub(4,5)


# In[56]:


#calculate BMI by using function
w=float((input("Enter your weight in (kg): ")))
h=float(input("Enter your height in (meter): "))
def bmi(w,h):
    """This is a function to calculate  our BMI."""
    return w/(h*h)
if bmi(w,h)<=18:
    print("Your bmi is ",bmi(w,h),", so you are underweight.")
elif bmi(w,h)<=25:
    print("Your bmi is ",bmi(w,h),", so you are normal.")
elif bmi(w,h)<=30:
    print("Your bmi is ",bmi(w,h),", so you are overweight.")
else:
    print("Your bmi is ",bmi(w,h),", so you have obesity.")


# In[3]:


a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
def calc(a,b):
    """This function is used to calculate binary operation."""
    s=int(input("Enter any number from 1 to 4: "))
    if s==1:
        print("Addition is:")
        return a+b
    elif s==2:
        print("Subtraction is:")
        return a-b
    elif s==3:
        print("Multiplication is:")
        return a*b
    elif s==4:
        print("Division is:")
        return a/b
    else:
        print("Try again.")
calc(a,b)


# In[6]:


m=[2,3,5,3]


# In[7]:


type(m)


# In[3]:


def travel_or_not(Bike,Car):
    travel=Bike or Car

    print(f"You  have Bike: {Bike}")        #f_string
    print(f"You have Car: {Car}")
    print(f"You can travel 100km: {travel}\n")
    
travel_or_not(False,False)
travel_or_not(False,True)
travel_or_not(True,False)
travel_or_not(True,True)


# In[4]:


def travel_or_not(Bike,Car):
    travel=Bike and Car

    print(f"You  have Bike: {Bike}")        #f_string
    print(f"You have Car: {Car}")
    print(f"You can travel 100km: {travel}\n")
    
travel_or_not(False,False)
travel_or_not(False,True)
travel_or_not(True,False)
travel_or_not(True,True)


# In[12]:


def test2(a=10,b=10,c=30):
    return a+b+c


# In[13]:


test2()


# In[17]:


test2(4,2,5)


# In[18]:


def travel_or_not(Bike=True,Car=False):
    travel=Bike or Car

    print(f"You  have Bike: {Bike}")        #f_string
    print(f"You have Car: {Car}")
    print(f"You can travel 100km: {travel}\n")
    
travel_or_not()


# In[21]:


travel_or_not(False)


# In[20]:


travel_or_not(False,False)


# In[29]:


def travel_or_not(Bike=False,Car=True):
    travel=Bike and Car

    print(f"You  have Bike: {Bike}")        #f_string
    print(f"You have Car: {Car}")
    return f"You can travel 100km: {travel}\n"          #return with f_string
    
result=travel_or_not()
print(result)


# In[33]:


def test7(*awrg):
    return awrg
test7(1,2,3,[4,5],'def',{5,6}, (6,7))


# In[41]:


def test8(*awrg):
    return awrg
test8({1:'s',2:'def',3:[4,5],4:{6,7,'sdf'}})


# In[43]:


def test9(a,*b):
    return a,b
test9(4,5,6,7,[1,2])


# In[44]:


def test10(*a,b):
    return a,b             #argument variable can't be first input var also can't possible both var as argument.
test10(4,5,6,7,[1,2])


# In[45]:


def test9(a=10,*b):
    return a,b        # it will overwrite value of var
test9(4,5,6,7,[1,2])


# In[47]:


def test10(**kwarg):
    return kwarg
test10(a=10,b=20,c=30)


# In[55]:


def test11(a,*b,**c):         #arguments must be swquential(var,arg_var,keyward_arg_var)
    return a,b,c
test11(1,{1:'def',2:'g',3:34},34,"srp",s=10,f=20)


# In[28]:


n=7
for i in range(n):
    for j in range(1,n-i):
        print("*",end=" ")
    print()


# In[26]:


n=int(input("Enter any number: "))
for i in range(1,n):
    for j in range(1, i):
        print(' ',end='')
    for k in range(i, n):
        print("* ",end='')
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(i,n):
        print("* ",end='')
    print()


# 

# In[2]:


x=lambda a,b:(a*b,a+b)


# In[3]:


x(35,45)


# In[6]:


h=lambda *hh:hh


# In[7]:


h(4,5,6,[6,7],(6,7))


# In[17]:


x=lambda *a:a


# In[18]:


x(3,4)


# In[10]:


v=lambda i:i**2


# In[12]:


v(2)


# In[19]:


x=lambda x:[i for i in x]


# In[24]:


x([4,5,6])


# In[27]:


l=[3,4,5,6]
l1=[]
for i in l:
    l1.append(i)
l1


# In[26]:


l1


# In[30]:


x=lambda **kwarg:kwarg
x(a='h',b=23,c=34)


# In[37]:


l=[1,2,3,4,5]
def test10(a):
    l1=[]
    for i in a:
        l1.append(i+2)
    return l1


# In[38]:


test10(l)


# In[46]:


d1={}
for i in range(1,5):
    d1[i]=i**3             #power of n can be given by a**n=a^n


# In[47]:


d1


# In[51]:


l=[3,4,5,'s','s','r','r']
l.remove('s')


# In[52]:


l


# In[57]:


s="I Love Python"         #Global variable(defined outside the function)
def f():
    print(s)
s="I Love Python"        #Global variable
f()
def g():
    print(s)
g()


# In[63]:


def f():
    s1="I Love Python"
    print(s1)
f()

print(s1)        #local variable(defined inside the function)


# In[72]:


s2="I love Python"
def f():
    s2="I love C"
    print(s2)
    print(id(s2))
f()
print(s2)
print(id(s2))


# In[73]:


#map is takng two input arguments
#r=map(function,iteration)


# In[74]:


def square(num):
    return num**2


# In[75]:


square(5)


# In[90]:


print(tuple(map(square,(1,2,3,4,5))))
print(list(map(square,[6,7,8])))


# In[103]:


def cube(num):
    return num**3

for i in map(cube,[1,2,3,4,5]):
    print(i)


# In[ ]:


#write a function called inspect() that accepts a string as an argument and return the word 
#even if the string is of even length and return its 1st charactor if the string is of odd length


# In[6]:


def check_even(num):
    return num%2!=0


# In[7]:


check_even(7)


# In[8]:


mynum=[1,2,3,4,5]


# In[9]:


value =filter(check_even,mynum)


# In[10]:


list(value)


# In[14]:


def check_even(num):
    return num%2==0

mynum=[1,2,3,4,5,6]
print(list(filter(check_even,mynum)))
print(list(map(check_even,mynum)))


# In[15]:


def check_even(num):
    return num%2==0

mynum=[1,2,3,4,5,6]
for i in filter(check_even,mynum):
    print(i)


# In[4]:


def square(num):
    return num**2

mynum=[1,2,3,4,5]
print(list(map(square,mynum)))


# In[5]:


map(lambda num:num*num,mynum)
print(list(map(lambda num:num*num,mynum)))


# In[8]:


name=["shubh","purani"]
print(list(map(lambda x:x[0],name)))


# In[7]:


name=input("Enter your name: ")
vowel=list(filter(lambda ch:ch in "AaEeIiOoUu",name))
if len(vowel)==0:
    print("No vowel in your name.")
else:
    print("Vowels in your name: ",vowel)


# In[9]:


import functools         #import used to call library/package/module to function
list1 =[1,23,4,5,6]
print(functools.reduce(lambda a,b:a+b, list1))
print(functools.reduce(lambda a,b:a if a>b else b, list1))


# In[11]:


import array as arr            #Python array function

a=arr.array('i',[1,2,3])

print("Array before insertion:",end=" ")
for i in range(3):
    print(i,end=" ")
    
print("Array after insertion:",end=" ")
for i in (a):
    print(i, end=" ")


# """write a function called inspect() that accepts a string as an argument and return the word 
# even if the string is of even length and return its 1st charactor if the string is of odd length"""

# In[5]:


string=["January","February"]
print(list(map(lambda mystring: "EVEN" if len(mystring)%2==0 else mystring[0],string)))


# In[12]:


def func1():
    print("Hello world")
func2=func1     #decorate function
func2()

del func1     #to delete the function
func2()


# In[14]:


def func3(num):
    if num==0:
        return print
    if num==1:
        return int
a=func3(0)
print(a)


# In[40]:


def func1():
    x=3
    def func2():
        print(x)
    func2()
func1()


# In[35]:


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("hello")
    return nowexec
@dec1
def func2():
    print("hello world")
    
#func2=dec1(func2)
func2()


# In[30]:


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
pretty=make_pretty(ordinary)
pretty()


# In[38]:


def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15=create_adder(15)
print(add_15(10))


# In[55]:


def star(func):
    def inner(*args,**kwargs):
        print("*" * 30)
        func(*args,**kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print("!"*30)
        func(*args,**kwargs)
        print("!" * 30)
    return inner

@star
@percent

def printer():
    for i in range(30):
        print(" "*11, end=" ")
        print("Hello")
        break
printer()


# In[12]:


def shout(text):
    return text.lower()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))


# In[13]:


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
  
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())


# In[16]:


def my_decorator(func):
    #define a new function
    def modified_func(a, b):
        print("Addition started")
        print(func(a, b))
        print("Addition completed")
    #return the new function
    return modified_func

@my_decorator
def add(a, b):
    return a+b

add(5, 6)


# In[28]:


def f(num):
    def g():
        print("$")
        print(num())
        print(4)
    return g
@f
def h():
    return 5+3
h()


# In[29]:


list1=[1,2,3,4]
list2=list1  ## = mean same memory location
print(list1)
print(list2)


# In[30]:


list1,list2


# In[31]:


list2[1]=100


# In[32]:


print(list2)


# In[37]:


id(list1)


# In[38]:


id(list2)


# In[39]:


list1=[1,2,3,4]
list2=list1.copy()  ## make a different memory location


# In[40]:


list2


# In[41]:


list1


# In[42]:


id(list1)


# In[43]:


id(list2)


# In[46]:


import copy   ##deep copy

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.deepcopy(old_list)

print("Old_list:",id(old_list))
print("New_list:",id(new_list))


# In[47]:


try:
    a=5
    a/0
except:
    print("error")


# In[49]:


try:
    a=5
    a/0
except Exception as e:     #Exception is a superclass where e is allias
    print(e)


# In[55]:


try:
    n=int(input("Enter integer value: "))
except Exception as e:
    print(e)


# In[63]:


try:
    l=[2,3,4,5,6]
    for i in range(len(l+3)):
        print(l)
except Exception as e:
    print(e)


# In[66]:


try:
    l=[2,3,4,5,6]
    for i in range(len(l)+3):
        print(l[i])
except Exception as e:
    print(e)


# In[71]:


def test(a):
    if a=="sjs":
        raise ZeroDivisionError("you have entered a negative value", a)     #we can raise an error with userdefined docstring statement
    return a
test(ksjs)


# In[74]:


x='shubh'
if not type(x) is int:
    raise TypeError("Only integers are allowed")


# In[75]:


test("sjs")


# In[2]:


class test:
    print("shubh")
    
obj=test()


# In[8]:


class test1:
    def func(self):
        return "this is my first day"
    def func1(self):
        return "this is my second day in office"
    
obj=test1()
obj.func()


# In[10]:


class test1:
    def func(self):
        return "this is my first day"
    def func1(self):
        return "this is my second day in office"
    
obj=test1()
print(obj.func())        #to run both the functions we need to print those functions
print(obj.func1())


# In[13]:


class class3:
    def test1(self,a,b):
        print(a,b)
        
obj=class3()
obj.test1(3,4)       


# In[24]:


class calc:
    
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y

a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
obj=calc()
obj.add(4,5)


# In[20]:


class xyz:
    """this program is for try and exception in class"""
    try:
        def abc(self,a,b):
            return a/b
        obj=xyz()
        obj.abc(5,0)
    except Exception as e:
        print(e)


# In[5]:


class class1:

    def addi(self,a,b):
        return a+b

obj=class1()
obj.addi(a,b)


# In[6]:


class bmi:
    
    """This is a class to calculate bmi"""

    def bmi_cal(self):
        try:
            bmi= w/(h*h)
            print("Your bmi is:",bmi)
        except Exception as e:
            print(e)
            
try:
    w=float(input("Enter your weight(in kg):"))
    h=float(input("Enter your height(in m):"))
    obj=bmi()
    obj.bmi_cal()
except:
    print("Error in program. Retry.")


# In[2]:


class Person:
    def __init__(self,name,age,id):       #defined init() using double underscore ,called constructor
        self.name=name
        self.age=age
        self.id=id
        
p1=Person("Herry", 26,89)

print(p1.name)
print(p1.age)
print(p1.id)


# In[16]:


class bmi:
    def bmi_cal(self):
        try:
            bmi= 60/(0*0)
            print(bmi)
        except Exception as e:
            print(e)
            
obj=bmi()
obj.bmi_cal()


# In[16]:


class num():
     """This is a program to find out the number is positive or negative"""
        
    def __init__(self,a): 
        self.a=a
        
    
    def num_p(self):
        try:
            if self.a >=0:
                print("This number is positive")
            else:
                print("This number is negative")
        except Exception as e:
            print(e)
            num1=int(input("Enter the number: "))
            
num2=num(-8)
num2.num_p()


# In[12]:


class car:
    def __init__(shubh,body_type,engine,fuel_type,color,door,window):
        shubh.a= body_type
        shubh.b= engine
        shubh.c= fuel_type
        shubh.d= color
        shubh.e= door
        shubh.f= window
        
    def test(shubh):
        print("This is the first method of my class car", shubh.e)
        
obj=car("suv","bs4","diesel","blue",4,4)
obj.test()


# In[9]:


class list1:
    """This program is to find reverse list and find integer elements from the list"""
    
    def __init__(self,l):
        self.l=l
        
    def rev(self):
        if type(self.l)==list:
            return self.l[::-1]
        
    def int_list1(self):
        for i in self.l:
            if type(i)==int:
                print(i)
            
c=list1([2,45,34,'shubh'])
print(c.rev())
print(c.int_list1())


# In[3]:


class Person():
    """The program is for inheritance- Parent class"""
        
    def __init__(self,name,id,age):
        self.a=name
        self.b=id
        self.c=age
        
    def Display(self):
        print(self.a,self.b,self.c)
        
emp=Person("shubh",87,25)
emp.Display()


# In[15]:


class child(Person):
    """The program is for inheritance- child class"""
    
    def __init__(self,name,id,age,xx):
        self.xx=xx
        
        Person.__init__(self,name,id,age)     #in-walk parent class to child class for constructor of child class
            
    def disp(self):
        print(self.xx)
    
    def Print(self):
        print("This is a child class")
        
        
emp_details=child("xyz",34,23,123)

#calling parent class functions
emp_details.Display() 

#calling chil class functions
emp_details.disp()
emp_details.Print()


# In[14]:


class num():
    
    def __init__(self,n):
        self.n=n
        
    def num_p(self):
        try:
            if self.n >= 0:
                print("number is positive.")
            else:
                print("number is negative.")
        except Exception as e:
            print(e)
            
num2=int(input("enter the number:"))            
num1=num(num2)
num1.num_p()


# In[1]:


class calc():
    """This is a program to solve calculator for any two numbers"""
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    try:
        def add(self):
            return self.a + self.b
        def sub(self):
            if self.a >= self.b:
                return self.a - self.b
            else:
                return self.b - self.a
        def mult(self):
            return self.a * self.b
        def div(self):
            return self.a / self.b
    except Exception as e:
        print(e)
        
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))  

cal=calc(n1,n2)

print("Addition:",cal.add())
print("Subtraction:",cal.sub())
print("Multiplication:",cal.mult())
print("Division:",cal.div())


# In[43]:


x=lambda a:a**2
x(5)


# In[13]:


class xyz():                                  #Multi level inheritance
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def test(self):
        print("This is a method of xyz class")
        
class xyz1(xyz):
    def test1(self):
        print("This is a method of xyz1 class")

class xyz2(xyz1):
    def test2(self):
        print("This is a method of xyz2 class")
        
g=xyz2(3,4,4)
g.test2()
g.test1()
g.test()


# In[14]:


##remind mam for file handling exercise


# In[25]:


class abc():                                   #multiple inheritance
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def test3(self):
        print("This is a parent class abc",self.a,self.b)
        
class abc1(abc):
    def test4(self):
        print("This is a child class 1")
        
class abc2(abc):
    def test5(self):
        print("This is a child class 2")

#objects for both child classes
m=abc2(2,3)
n=abc1(2,4)

#calling child classes with their objects
m.test5()
n.test4()

#calling parent class with both chil classes objects
m.test3()
n.test3()


# In[34]:


class facebook():
    def stories(self):
        print("This is facebook stories")
        
class instagram():
    def stories(self):
        print("This is instagram stories")
        
a=facebook()
b=instagram()

a.stories()
b.stories()


# In[1]:


class facebook():
    def stories(self):
        print("This is facebook stories")
        
class instagram(facebook):
    def stories(self):
        super().stories()         #solution of overriding: by calling super class (parent class)
        print("This is instagram stories")
        
a=instagram()

a.stories()              #method overriding : it will call parent class  function but fn_name is same in both so it will override to child class


# In[46]:


class add():
    def result(self,a,b):
       print("Addition:",a+b)
    
class mult(add):
    def result(self,a,b):
        super().result(20,30)          #calling super class to solve overriding
        print("Multiplication:",a*b)
        
c=mult()
c.result(20,20)


# In[56]:


class A:
    def __init__(self,a):
        self.a=a
        
    def __add__(self,b):
        return self.a + b.a
    
obj1=A(1)
obj2=A(2)
obj3=A(" shubh ")
obj4=A(" xyz ")

print(obj1 + obj2)
print(obj3 + obj4)


# In[10]:


class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        return self.a + other.a + self.b + other.b
    
obj1=complex(1,2)
obj2=complex(2,3)
obj3=obj1 + obj2
print(obj3)


# In[11]:


class A:
    def __init__(self,a):
        self.a=a
        
    def __gt__(self,other):
        if self.a > other.a:
            return True
        else:
            return False
        
ob1=A(1)
ob2=A(2)

if (ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")


# In[5]:


class test:       #encapsulation
    def __init__(self,a,b,c):
        self._a=a
        self.__b=b
        self.c=c
        
v=test(2,3,4)


# In[6]:


v._a   # calling protactive variable


# In[10]:


v._test__b    #calling private variable


# In[12]:


v.c     #calling simple variable


# In[19]:


class xyz:
    def __init__(self,name,id,age):
        self.a=name
        self._b=id
        self.__c=age
        print("This is encapulation program")
        
class xyz1(xyz):
    def test(self):
        return self.a, self._b,self.__c
    
w=xyz('shubh',234,23)
print(w.a)          #simple var
print(w._b)         #protactive var
print(w._xyz__c)    #private var


# In[1]:


list1 = [1,2,3,4]
list2 = list1.copy()


# In[2]:


list2


# In[3]:


id(list2)


# In[4]:


id(list1)


# In[ ]:




