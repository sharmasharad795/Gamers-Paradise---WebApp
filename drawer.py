import json
import requests
import pandas as pd
import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import  numpy as np


url='https://inf551-faa51.firebaseio.com/vgsales.json'
response = requests.get(url)
k=json.dumps(response.json(), indent=4)
k_=json.loads(k)
df=pd.DataFrame(k_)
df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]

s=df['Publisher'].value_counts().head(10)

labels=s.keys()
plt.figure(figsize=(10,7))

plt.pie(s, labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.axis('equal')
plt.show()

plt.figure(figsize=(10,7))
Global_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="Global_Sales"')

glsales=json.dumps(Global_SalesSort.json(),indent=4)
glsales_=json.loads(glsales)
glsales_df=pd.DataFrame(glsales_)
glsales_df = glsales_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
glsales_df=glsales_df.sort_values(by='Global_Sales',ascending=False)
df2=glsales_df.head(20)



ax = sns.barplot(x="Global_Sales", y="Name",hue="Publisher" ,data=df2)

NA_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="NA_Sales"')
nasales=json.dumps(NA_SalesSort.json(),indent=4)
nasales_=json.loads(nasales) 
nasales_df=pd.DataFrame(nasales_)
nasales_df = nasales_df[['Name','NA_Sales','Global_Sales']]
nasales_df=nasales_df.sort_values(by='NA_Sales',ascending=False).head(10)
nasales_df.set_index('Name', inplace=True)


fig = plt.figure(figsize=(10,7)) 
ax = fig.add_subplot(111) 
ax2 = ax.twinx() 
width = 0.4

nasales_df.NA_Sales.plot(kind='bar', color='orange', ax=ax, width=width, position=1)
nasales_df.Global_Sales.plot(kind='bar', color='yellow', ax=ax2, width=width, position=0)

ax.set_ylabel('NA_Sales')
ax2.set_ylabel('Global_Sales')


plt.show()


GenreFilter=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="Genre"&equalTo="Sports"')

genre=json.dumps(GenreFilter.json(),indent=4)
genre_=json.loads(genre)

df=[]
for key,value in genre_.items():
    df.append(genre_[key])
    
genre_df=pd.DataFrame(df)

genre_df = genre_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
genre_df=genre_df.sort_values(by='Genre')



NA_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="EU_Sales"')
nasales=json.dumps(NA_SalesSort.json(),indent=4)
nasales_=json.loads(nasales) 
nasales_df=pd.DataFrame(nasales_)
nasales_df = nasales_df[['Name','EU_Sales','Global_Sales']]
nasales_df=nasales_df.sort_values(by='EU_Sales',ascending=False).head(10)
nasales_df.set_index('Name', inplace=True)


fig = plt.figure(figsize=(10,7)) 
ax = fig.add_subplot(111) 
ax2 = ax.twinx() 

width = 0.4

nasales_df.EU_Sales.plot(kind='bar', color='orange', ax=ax, width=width, position=1)
nasales_df.Global_Sales.plot(kind='bar', color='yellow', ax=ax2, width=width, position=0)

ax.set_ylabel('EU_Sales')
ax2.set_ylabel('Global_Sales')



plt.show()

url='https://inf551-faa51.firebaseio.com/vgsales.json'
response = requests.get(url)
k=json.dumps(response.json(), indent=4)
k_=json.loads(k)
df=pd.DataFrame(k_)
df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]


df.groupby('Genre')['Global_Sales'].agg(np.sum).plot()

plt.show()


url='https://inf551-faa51.firebaseio.com/vgsales.json'
response = requests.get(url)
k=json.dumps(response.json(), indent=4)
k_=json.loads(k)
df=pd.DataFrame(k_)
df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]


grouped=df.groupby('Genre')
pf=grouped['Global_Sales'].agg(np.sum)

labels=pf.keys()
plt.figure(figsize=(10,7))

plt.pie(pf, labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.axis('equal')
plt.show()

