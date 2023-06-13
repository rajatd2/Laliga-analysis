#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import numpy as np
import pandas as pd


# In[2]:


#1.Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data.


# In[8]:


# reading data set from provided CSV to a dataframe 'laliga' using pandas
laliga = pd.read_csv('Desktop/I neuron/Laliga.csv')


# In[9]:


# printing head of the dataframe 'laliga'
laliga.head()


# In[10]:


#checking shape of the 'laliga' dataframe
laliga.shape


# In[11]:


# using replace function to replace '-' with '0' which will allow us arithamatic operations
laliga.replace('-',0,inplace=True)
laliga


# In[12]:


#2.Print all the teams which have started playing between 1930-1980


# In[13]:


# converting values of 'Debut' column into string datatype
laliga['Debut'] = laliga['Debut'].astype(str)

# getting team details to new dataframe 'Debut Year' based on Debut in between 1930 to 1980 (including 1930 but excluding 1980)
Debut_Year = laliga[laliga['Debut'].str[:4].between('1930','1980')]

# printing team name and debut year from 'Debut_Year' dataframe
Debut_Year[['Team','Debut']]


# In[14]:


#3. Print the list of teams which came Top 5 in terms of points.


# In[15]:


# copying 'Team' and 'Points' column to new dataframe 'laliga_sort'
laliga_sort = laliga[['Team','Points']].copy()

# converting values of 'Points' column into int datatype
laliga_sort['Points'] = laliga_sort['Points'].astype(int)

# sorting the dataframe 'laliga_sort' based on 'Points' value
laliga_sort.sort_values(by='Points', ascending=False, inplace=True)

#printing head as top 5 teams in terms of points
laliga_sort.head(5)


# In[19]:


#4. Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference.


# In[20]:


# converting values of 'GoalsFor' and 'GoalsAgainst' column into int datatype
laliga['GoalsFor'] = laliga['GoalsFor'].astype(int)
laliga['GoalsAgainst'] = laliga['GoalsAgainst'].astype(int)

# defining function 'Goal_diff_count()' as per the problem statement needs
def Goal_diff_count():   
     laliga['Goal_diff_count'] = laliga['GoalsFor']-laliga['GoalsAgainst']
     return laliga[['Team','Goal_diff_count']]

# calling 'Goal_diff_count()' function and storing it to 'Goal'
Goal = Goal_diff_count()

# sorting data and printing data from 'Goal'
Goal.sort_values(by = 'Goal_diff_count',ascending=False)


# In[21]:


laliga.shape


# In[22]:


#5.Using the same function, find the team which has the maximum and minimum goal difference.


# In[23]:


# printed first entry of sorted dataframe by calling 'Goal_diff_count()' function 
Goal_diff_count().head(1) # max goal difference


# In[24]:


# printed last entry of sorted dataframe by calling 'Goal_diff_count()' function 
Goal_diff_count().tail(1) # min goal difference


# In[26]:


#6. Create a new column with the name “Winning Percent” and append it to the data set.


# In[30]:


# converting values of 'GamesWon' and 'GamesPlayed' column into int datatype
laliga['GamesWon'] = laliga['GamesWon'].astype(int)
laliga['GamesPlayed'] = laliga['GamesPlayed'].astype(int)

# calculate winning percentage for each team and storing value to new column 'Win Per'
laliga['Win Per'] = (laliga['GamesWon']/laliga['GamesPlayed']) *100

# replacing Null values with 0%
laliga['Win Per'].fillna(0,inplace = True)

# printing team name and winning percentage for each team
laliga[['Team','Win Per']].head(5)


# In[31]:


#6.Group teams based on their “Best position” and print the sum of their points for all positions


# In[32]:


# converting values of 'Points' and 'BestPosition' column into int datatype
laliga['Points'] = laliga['Points'].astype(int)
laliga['BestPosition'] = laliga['BestPosition'].astype(int)

# grouping teams based on 'BeastPosition' column
group_Best = laliga[['Team','Points','BestPosition']].groupby('BestPosition')

# computing sum of grouped values on 'BestPosition' and print them
group_Best['Points'].sum()


# In[ ]:




