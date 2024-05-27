#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[18]:


#Send a request to the Wikipedia page:
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page= requests.get(url)

#Parse the HTML content using BeautifulSoup:
soup=BeautifulSoup(page.text, 'html')


# In[3]:


soup.find('table')


# In[4]:


#Find the relevant table that contains the list of companies:
soup.find_all('table')[1]


# In[5]:


soup.find('table', class_ = 'wikitable sortable')


# In[6]:


table = soup.find_all('table')[1]
print(table)


# In[7]:


world_titles = table.find_all('th')


# In[8]:


world_titles


# In[9]:


#Extract the table headers:
world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[10]:


#Create a DataFrame using pandas:
import pandas as pd


# In[11]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[19]:


#Populate the DataFrame with the data from the table:
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[14]:


df


# In[17]:


#Save the DataFrame to a CSV file:
df.to_csv(r'C:\Users\Albert\Documents\Data Analyst\Largest_Companies.csv', index = False)


# In[ ]:




