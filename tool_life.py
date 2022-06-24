#!/usr/bin/env python
# coding: utf-8

# In[32]:

#Imports
import pandas as pd
import os
import glob
import datetime as dt
from glob import glob as g
import warnings
import pickle
warnings.filterwarnings("ignore")


# In[2]:


#Load all files of /Absolute Position-11-10-21
path = os.getcwd()
files = glob.glob(os.path.join(path, "Tool Life/Absolute Position/11-10-21/*.csv"))

#Create a DataFrame
abs_pos_11 = pd.DataFrame()
content = []

#Append all csv files in the dataframe
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

abs_pos_11 = pd.concat(content)

#Dropping Columns with only NULL values
abs_pos_11.dropna(axis='columns',how='all',inplace=True)

print("The total number of rows in abs_pos : ",abs_pos_11.shape[0])
print("The total number of columns in abs_pos : ",abs_pos_11.shape[1])


# In[3]:


#Load all files of /Feed Rate-11-10-21
path = os.getcwd()
files = glob.glob(os.path.join(path, "Tool Life/FeedRate/11-10-21/*.csv"))

#Create a DataFrame
feed_Rate_11 = pd.DataFrame()
content = []

#Append all csv files in the dataframe
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

feed_Rate_11 = pd.concat(content)

#Dropping Columns with only NULL values
feed_Rate_11.dropna(axis='columns',how='all',inplace=True)

print("The total number of rows in feed_Rate : ",feed_Rate_11.shape[0])
print("The total number of columns in feed_Rate : ",feed_Rate_11.shape[1])


# In[4]:


#Load all files of /Relative Position-11-10-21
path = os.getcwd()
files = glob.glob(os.path.join(path, "Tool Life/Relative Position/11-10-21/*.csv"))

#Create a DataFrame
rel_pos_11 = pd.DataFrame()
content = []

#Append all csv files in the dataframe
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

rel_pos_11 = pd.concat(content)

#Dropping Columns with only NULL values
rel_pos_11.dropna(axis='columns',how='all',inplace=True)

print("The total number of rows in rel_pos : ",rel_pos_11.shape[0])
print("The total number of columns in rel_pos : ",rel_pos_11.shape[1])


# In[5]:


#Load all files of /Servo Load-11-10-21
path = os.getcwd()
files = glob.glob(os.path.join(path, "Tool Life/Servo Load/11-10-21/*.csv"))

#Create a DataFrame
servoLoad_11 = pd.DataFrame()
content = []

#Append all csv files in the dataframe
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

servoLoad_11 = pd.concat(content)

#Dropping Columns with only NULL values
servoLoad_11.dropna(axis='columns',how='all',inplace=True)

print("The total number of rows in Servo_load : ",servoLoad_11.shape[0])
print("The total number of columns in Servo_load : ",servoLoad_11.shape[1])


# In[6]:


#Load all files of /Servo Speed-11-10-21
path = os.getcwd()
files = glob.glob(os.path.join(path, "Tool Life/servospeed/11-10-21/*.csv"))

#Create a DataFrame
servoSpeed_11 = pd.DataFrame()
content = []

#Append all csv files in the dataframe
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

servoSpeed_11 = pd.concat(content)

#Dropping Columns with only NULL values
servoSpeed_11.dropna(axis='columns',how='all',inplace=True)

print("The total number of rows in Servo_Speed : ",servoSpeed_11.shape[0])
print("The total number of columns in Servo_Speed : ",servoSpeed_11.shape[1])


# In[7]:


ele=pd.DataFrame()
ele['Date']=abs_pos_11['date']
ele['MAZAK_FZ:Absolute position MAZAK_FZ P1 A0-Value']=abs_pos_11['MAZAK_FZ:Absolute position MAZAK_FZ P1 A0-Value']
ele['MAZAK_FZ:Absolute position MAZAK_FZ P1 A1-Value']=abs_pos_11['MAZAK_FZ:Absolute position MAZAK_FZ P1 A1-Value']
ele['MAZAK_FZ:Absolute position MAZAK_FZ P1 A2-Value']=abs_pos_11['MAZAK_FZ:Absolute position MAZAK_FZ P1 A2-Value']
ele['MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value']=feed_Rate_11['MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value']
ele['MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value.1']=feed_Rate_11['MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value.1']
ele['MAZAK_FZ:Relative position MAZAK_FZ P1 A0-Value']=rel_pos_11['MAZAK_FZ:Relative position MAZAK_FZ P1 A0-Value']
ele['MAZAK_FZ:Relative position MAZAK_FZ P1 A1-Value']=rel_pos_11['MAZAK_FZ:Relative position MAZAK_FZ P1 A1-Value']
ele['MAZAK_FZ:Relative position MAZAK_FZ P1 A2-Value']=rel_pos_11['MAZAK_FZ:Relative position MAZAK_FZ P1 A2-Value']
ele['MAZAK_FZ:Relative position MAZAK_FZ P1 A3-Value']=rel_pos_11['MAZAK_FZ:Relative position MAZAK_FZ P1 A3-Value']
ele['MAZAK_FZ:Servo load MAZAK_FZ P1 A0-Value']=servoLoad_11['MAZAK_FZ:Servo load MAZAK_FZ P1 A0-Value']
ele['MAZAK_FZ:Servo load MAZAK_FZ P1 A1-Value']=servoLoad_11['MAZAK_FZ:Servo load MAZAK_FZ P1 A1-Value']
ele['MAZAK_FZ:Servo load MAZAK_FZ P1 A2-Value']=servoLoad_11['MAZAK_FZ:Servo load MAZAK_FZ P1 A2-Value']
ele['MAZAK_FZ:Servo load MAZAK_FZ P1 A3-Value']=servoLoad_11['MAZAK_FZ:Servo load MAZAK_FZ P1 A3-Value']
ele['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A0-Value']=servoSpeed_11['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A0-Value']
ele['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A1-Value']=servoSpeed_11['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A1-Value']
ele['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A2-Value']=servoSpeed_11['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A2-Value']
print("The total number of rows in ele : ",ele.shape[0])
print("The total number of columns in ele : ",ele.shape[1])


# In[11]:


ele.fillna(0,inplace=True)


# In[12]:


ele=ele.rename(columns = {'MAZAK_FZ:Absolute position MAZAK_FZ P1 A0-Value': 'Abs_Pos_A0', 
                          'MAZAK_FZ:Absolute position MAZAK_FZ P1 A1-Value': 'Abs_Pos_A1',
                          'MAZAK_FZ:Absolute position MAZAK_FZ P1 A2-Value':'Abs_Pos_A2',
                          'MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value':'Feed_P1',
                          'MAZAK_FZ:Feed rate F [actual] MAZAK_FZ P1-Value.1':'Feed_P11',
                          'MAZAK_FZ:Relative position MAZAK_FZ P1 A0-Value':'Rel_Pos_A0',
                          'MAZAK_FZ:Relative position MAZAK_FZ P1 A1-Value':'Rel_Pos_A1',
                          'MAZAK_FZ:Relative position MAZAK_FZ P1 A2-Value':'Rel_Pos_A2',
                          'MAZAK_FZ:Relative position MAZAK_FZ P1 A3-Value':'Rel_Pos_A3',
                          'MAZAK_FZ:Servo load MAZAK_FZ P1 A0-Value':'Ser_ld_A0',
                          'MAZAK_FZ:Servo load MAZAK_FZ P1 A1-Value':'Ser_ld_A1',
                          'MAZAK_FZ:Servo load MAZAK_FZ P1 A2-Value':'Ser_ld_A2',
                          'MAZAK_FZ:Servo load MAZAK_FZ P1 A3-Value':'Ser_ld_A3',
                          'MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A0-Value':'Ser_spd_A0',
                          'MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A1-Value':'Ser_spd_A1',
                          'MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A2-Value':'Ser_spd_A2',
                         }, inplace = False)


# In[14]:


del ele['Rel_Pos_A3']
del ele['Ser_ld_A3']


# In[15]:


ele.head()


# In[16]:


ele.describe()


# In[17]:


import numpy as np
#generating dummy dataframe with abnormal condition
np.random.seed(1)
dummy = pd.DataFrame({"Abs_Pos_A0" : np.random.randint(low=0, high=400, size=136800),
                      "Abs_Pos_A1" : np.random.randint(low=0, high=400, size=136800),
                      "Abs_Pos_A2" : np.random.randint(low=0, high=400, size=136800),
                      "Feed_P1" : np.random.randint(low=0, high=50000, size=136800),
                      "Rel_Pos_A0" : np.random.randint(low=-300, high=0.5, size=136800),
                      "Rel_Pos_A1" : np.random.randint(low=-300, high=0.5, size=136800),
                      "Rel_Pos_A2" : np.random.randint(low=-300, high=3000, size=136800),
                      "Ser_ld_A0" : np.random.randint(low=0, high=250, size=136800),
                      "Ser_ld_A1" : np.random.randint(low=0, high=250, size=136800),
                      "Ser_ld_A2" : np.random.randint(low=0, high=250, size=136800)})


# In[18]:


dummy.head()


# In[19]:


#assigning label
conditions=[(dummy['Abs_Pos_A0'] <= 370) & (dummy['Abs_Pos_A1'] <= 370) & (dummy['Abs_Pos_A2'] <= 370) & (dummy['Abs_Pos_A0'] >= 0) & (dummy['Abs_Pos_A1'] >= 0) & (dummy['Abs_Pos_A2']>= 0) & (dummy['Feed_P1'] <=45000) & (dummy['Rel_Pos_A0'] <=1) & (dummy['Rel_Pos_A1'] <=1) & (dummy['Rel_Pos_A2'] <=1800)& (dummy['Ser_ld_A0'] <=200)& (dummy['Ser_ld_A1'] <=200)& (dummy['Ser_ld_A2'] <=200),
            (dummy['Abs_Pos_A0'] > 370) | (dummy['Abs_Pos_A1'] > 370) | (dummy['Abs_Pos_A2'] > 370) |(dummy['Abs_Pos_A0'] < 0) | (dummy['Abs_Pos_A1'] <= 0) | (dummy['Abs_Pos_A2']<= 0) | (dummy['Feed_P1'] >=45000) | (dummy['Rel_Pos_A0'] >=1) | (dummy['Rel_Pos_A1'] >=1) | (dummy['Rel_Pos_A2'] >=1800)| (dummy['Ser_ld_A0'] >=200)| (dummy['Ser_ld_A1'] >=200)| (dummy['Ser_ld_A2'] >=200)
            ]
choices = [0,1]
dummy['Class'] = np.select(conditions, choices)


# In[20]:


dummy.head()


# In[21]:


dummy['Class'].value_counts()


# In[22]:


#assigning label
conditions=[(ele['Abs_Pos_A0'] <= 370) & (ele['Abs_Pos_A1'] <= 370) & (ele['Abs_Pos_A2'] <= 370) & (ele['Abs_Pos_A0'] >= 0) & (ele['Abs_Pos_A1'] >= 0) & (ele['Abs_Pos_A2']>= 0) & (ele['Feed_P1'] <=45000) & (ele['Rel_Pos_A0'] <=1) & (ele['Rel_Pos_A1'] <=1) & (ele['Rel_Pos_A2'] <=1800)& (ele['Ser_ld_A0'] <=200)& (ele['Ser_ld_A1'] <=200)& (ele['Ser_ld_A2'] <=200),
            (ele['Abs_Pos_A0'] > 370) | (ele['Abs_Pos_A1'] > 370) | (ele['Abs_Pos_A2'] > 370) |(ele['Abs_Pos_A0'] < 0) | (ele['Abs_Pos_A1'] <= 0) | (ele['Abs_Pos_A2']<= 0) | (ele['Feed_P1'] >=45000) | (ele['Rel_Pos_A0'] >=1) | (ele['Rel_Pos_A1'] >=1) | (ele['Rel_Pos_A2'] >=1800)| (ele['Ser_ld_A0'] >=200)| (ele['Ser_ld_A1'] >=200)| (ele['Ser_ld_A2'] >=200)
            ]
choices = [0,1]
ele['Class'] = np.select(conditions, choices)


# In[23]:


ele['Class'].value_counts()


# In[24]:


del ele['Date']


# In[25]:


np.any(np.isnan(ele))
np.all(np.isfinite(ele))


# In[26]:


#TREE
X = ele.iloc[:, :-1].values
y = ele.iloc[:, -1].values


# In[27]:


#import numpy as np
X[np.isnan(X)] = 0
y[np.isnan(y)] = 0


# In[28]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# In[29]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[30]:


from sklearn.tree import RandomForestClassifier
classifier = RandomForestClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# In[33]:

pickle.dump(classifier,open('model_1.pkl','wb'))
model=pickle.load(open('model_1.pkl','rb'))
