#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[5]:


df1=(np.arange(0,20).reshape(4,5))
df1


# In[10]:


df=pd.DataFrame(df1)
df


# In[9]:


type(df)


# In[24]:


df=pd.DataFrame(df1,index=['Row1','Row2','Row3','Row4'],
               columns=['Column1','Column2','Column3','Column4','Column5'])


# In[25]:


df.head()    #as default value it will show first five records


# In[19]:


df


# In[14]:


df.head(3)   #will show first 3 records


# In[15]:


df.tail()  #for last records


# In[16]:


df.tail(2)    #for last 2 records


# In[17]:


df.loc['Row1']


# In[18]:


type(df.loc['Row1'])


# In[19]:


df.iloc[:,:]


# In[20]:


df.iloc[1:,3:]


# In[21]:


df.iloc[:,2:]


# In[22]:


type(df.iloc[:,2:])


# In[7]:


#convert dataframe into array
df.iloc[:,1:].values


# In[24]:


type(df.iloc[:,1:].values)


# In[25]:


df['Column1']   #tofetch column values


# In[28]:


df.loc['Row1']  #to fetch row values


# In[33]:


df['Column1'].value_counts()


# In[6]:


df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/Complete-Feature-Engineering/master/mercedesbenz.csv')


# In[7]:


df


# In[8]:


#titanic and tips dataset download


# In[4]:


df1=pd.read_csv('https://gist.githubusercontent.com/fyyying/4aa5b471860321d7b47fd881898162b7/raw/6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f/titanic_dataset.csv')


# In[5]:


df1


# In[6]:


df1.shape


# In[8]:


df1.drop('Parch',axis=1,inplace=True)    #it will drop the mentioned column


# In[10]:


df1


# In[11]:


df1.info()


# In[12]:


df1.dtypes


# In[13]:


df1.describe()


# In[14]:


df1.isnull().sum()


# In[15]:


df1.duplicated()


# In[16]:


df1.duplicated().sum()


# In[2]:


import pandas as p
import numpy as n


# In[19]:


d=n.arange(0,100).reshape(10,10)


# In[20]:


d


# In[21]:


df=pd.DataFrame(d)


# In[22]:


df


# In[23]:


type(df)


# In[26]:


df=pd.DataFrame(d,index=['Row1','Row2','Row3','Row4','Row5','Row6','Row7','Row8','Row9','Row10'],
               columns=['Column1','Column2','Column3','Column4','Column5','Column6','Column7','Column8','Column9','Column10'])


# In[27]:


df


# In[28]:


type(df)


# In[29]:


df.head()


# In[30]:


df.tail()


# In[31]:


df.loc['Row4']


# In[37]:


df['Column5']


# In[38]:


df.iloc[:,:]


# In[39]:


df.iloc[5:,5:]


# In[40]:


df.shape


# In[42]:


df.info()


# In[43]:


df.dtypes


# In[44]:


df.describe()


# In[46]:


df.isnull().sum()


# In[48]:


df.duplicated().sum()


# In[15]:


import numpy as np
import math
import pandas as pd


# In[16]:


df1=(np.arange(0,20).reshape(10,2))


# In[17]:


df1


# In[18]:


df=pd.DataFrame(df1)
df


# In[19]:


type(df)


# In[20]:


df=pd.DataFrame(df1,index=['Row1','Row2','Row3','Row4','Row5','Row6','Row7','Row8','Row9','Row10'],
               columns=['Column1','Column2'])


# In[21]:


df


# In[19]:


df.head()  


# In[20]:


df.tail()


# In[21]:


df.loc['Row1']


# In[22]:


df.iloc[:,:]


# In[24]:


df.iloc[:6,:]


# In[25]:


df.shape


# In[27]:


df.info()


# In[28]:


df.describe()


# In[30]:


df.drop('Column1',axis=1,inplace=True)


# In[31]:


df


# In[32]:


df.duplicated


# In[33]:


df.isnull().sum()


# In[35]:


df.duplicated().sum()


# In[36]:


df.dtypes


# In[1]:


import numpy as np
import pandas as pd


# In[18]:


list1=[[1,2,3],[3,4,np.nan],[5,6,np.nan],[np.nan,np.nan,np.nan]]


# In[19]:


list1


# In[20]:


df=pd.DataFrame(list1)


# In[21]:


df


# In[7]:


df.isnull().sum()   #columnwise null data count


# In[8]:


df.info()


# In[9]:


df.shape


# In[10]:


df.head(2)


# In[11]:


df.tail(2)


# In[13]:


df.dropna(axis=0,inplace=True)


# In[14]:


df


# In[22]:


df.dropna(axis=1,inplace=True)


# In[23]:


df


# In[30]:


df=pd.DataFrame(np.random.randn(10,10),index=['a','b','c','d','e','f','g','h','i','j'],
                columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'])


# In[31]:


df


# In[33]:


df2=df.reindex(['a','b','c','d','e','f','g','h','i','j','w','x','y','z'])


# In[34]:


df2


# In[35]:


df2.dropna(axis=0)


# In[36]:


pd.isna(df2['c1'])


# In[37]:


df2['c1'].notna()


# In[38]:


df2.fillna('missing')


# In[39]:


df2['c1'].values


# In[43]:


df2.info()


# In[44]:


from io import StringIO, BytesIO


# In[45]:


data=('col1,col2,col3\n'
     'x,y,1\n'
     'a,b,2\n'
     'c,d,3')


# In[46]:


data


# In[47]:


type(data)


# In[53]:


pd.read_csv(StringIO(data))


# In[58]:


df=pd.read_csv(StringIO(data),usecols=lambda x: x.upper() in ['COL1','COL3'])


# In[59]:


df


# In[60]:


df.to_csv('test.csv')


# In[61]:


ls


# In[63]:


#fetch countrycode on wikipedia html table file adn use data frame to arrange


# In[9]:


import pandas as pd


# In[ ]:





# In[ ]:





# In[ ]:




