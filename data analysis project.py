#!/usr/bin/env python
# coding: utf-8

# ![](https://media.bizj.us/view/img/6459592/thinkstockphotos-522779415*750xx2122-1196-0-0.jpg)

# # Investigate [ The Movie Database (TMDb) ] to find out the best investment options

# ### "Data Driven Business Study"  
# ***By Data Scientist : Khaled Saad***  
#     *Date : 23-01-2023*

# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# <li><a href="#refs">Refrences</a></li> 
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > I am considering myself as an investor how want to invest his money in the filmmaking industry
# and now i want to make a data-driven decision to select which is the best genre of movies  to invest in and who is the best movie director i should invest with him
# So i decided to invistagate " The Movie Database (TMDb) " which is avialble on Kaggle 

# <a id='wrangling'></a>
# ## Data Wrangling
# 
# >Now I will do the following steps:
# >    1. load in the data 
# >    2. Exploe the data to decide if it needs cleaning or it needs some modifications 
# >    3. Do the required cleanliness
# >    4. Do the required modifications (adding or droping raws and columns)
# 

# **Step No. (0)** : importing the required packages to do the job

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint

#this magic ward is essntial to plot in-line
get_ipython().run_line_magic('matplotlib', 'inline')


# **Step No. (1)** : loading the data

# In[2]:


my_raw_data = pd.read_csv("tmdb-movies.csv")


# **Step No. (2)** : what is our data looks like ?

# In[3]:


print("\n",'*'*100 ,"\n")
print("The size of the data looks like following: \n \n" , my_raw_data.size)
print("\n",'*'*100 ,"\n")
print("The shape of the data looks like following: \n \n" , my_raw_data.shape)
print("\n",'*'*100 ,"\n")
print("The info of the data looks like following: \n \n", my_raw_data.info())
print("\n",'*'*100 ,"\n")
my_raw_data


# In[4]:


print("\n",'*'*100 ,"\n")
print("The first rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_raw_data.head())
print("\n",'*'*100 ,"\n")
print("\n",'*'*100 ,"\n")
print("The last rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_raw_data.tail())
print("\n",'*'*100 ,"\n")

x = 5

while True:
        explr = input("If you would like to explore more data type 'yes' and press enter or just press enter to skip ")
        if explr.lower() == "yes":
                x += 5
                print("-"*100)
                print("\n As per your selection you are watching the rows from row no. ", x-4,"to row no.",x," \n \n \n ", my_raw_data.iloc[ x-5 : x ] )
                print("-"*100)
        else:
            break   


# **Step (3)** : Tray to simplify the data by droping the un-useful data

# In[5]:


my_data_one = my_raw_data.filter(['release_year','genres', 'original_title', 'director', 'popularity', 'budget', 'revenue'], axis=1)


# **Step No. (4)** : let us see our data after simplification

# In[6]:


print("\n",'*'*100 ,"\n")
print("The size of the data looks like following: \n \n" , my_data_one.size)
print("\n",'*'*100 ,"\n")
print("The shape of the data looks like following: \n \n" , my_data_one.shape)
print("\n",'*'*100 ,"\n")
print("The info of the data looks like following: \n \n", my_data_one.info())
print("\n",'*'*100 ,"\n")
my_data_one


# **Step (5)** : let us simplify the work by adding new valuable column "The Profit" from the budget and revenue 

# In[7]:


my_data_one['profit'] = my_data_one['revenue'] - my_data_one['budget']


# **Step (6)** : and again let us tke a look on our data

# In[8]:


print("\n",'*'*100 ,"\n")
print("The size of the data looks like following: \n \n" , my_data_one.size)
print("\n",'*'*100 ,"\n")
print("The shape of the data looks like following: \n \n" , my_data_one.shape)
print("\n",'*'*100 ,"\n")
print("The info of the data looks like following: \n \n", my_data_one.info())
print("\n",'*'*100 ,"\n")
my_data_one


# In[9]:


print("\n",'*'*100 ,"\n")
print("The first rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_data_one.head())
print("\n",'*'*100 ,"\n")
print("\n",'*'*100 ,"\n")
print("The last rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_data_one.tail())
print("\n",'*'*100 ,"\n")

x = 5

while True:
        explr = input("If you would like to explore more data type 'yes' and press enter or just press enter to skip ")
        if explr.lower() == "yes":
                x += 5
                print("-"*100)
                print("\n As per your selection you are watching the rows from row no. ", x-4,"to row no.",x," \n \n \n ", my_data_one.iloc[ x-5 : x ] )
                print("-"*100)
        else:
            break   


# **Step No. (7)** : now let us make a copy of our simplified data to start clean if from the duplication and empty values 

# In[10]:


my_data_two = my_data_one.copy()


# In[11]:


my_data_two


# **Step No. (8)** : There are many budget and revenue data are missed which will lead to inacurate profit data - which is a very vital information for our last decision -, so now we will remove any row with missed budget or revenue data 

# In[12]:


my_data_two.drop(my_data_two[my_data_two['budget'] == 0].index , inplace = True)


# In[13]:


my_data_two


# In[14]:


my_data_two.drop(my_data_two[my_data_two['revenue'] == 0].index , inplace = True)


# In[15]:


my_data_two


# **Step No. (9)** : remove any other missed values 

# In[16]:


my_data_two.dropna(inplace = True)


# In[17]:


my_data_two


# **Step No. (10)** : remove any duplicated values 

# In[18]:


my_data_two.drop_duplicates(inplace = True)


# In[19]:


my_data_two


# ***
# **Warning: about 65% of the data was not good (either missed or duplicated) and was deleted**  
# 
# **Only 35% of the data is valid for the analysis which is a real limitation**
# ***

# **Step No. (11)** : now let take another look on our final data-set

# In[20]:


print("\n",'*'*100 ,"\n")
print("The size of the data looks like following: \n \n" , my_data_two.size)
print("\n",'*'*100 ,"\n")
print("The shape of the data looks like following: \n \n" , my_data_two.shape)
print("\n",'*'*100 ,"\n")
print("The info of the data looks like following: \n \n", my_data_two.info())
print("\n",'*'*100 ,"\n")


# In[21]:


print("\n",'*'*100 ,"\n")
print("The first rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_data_two.head())
print("\n",'*'*100 ,"\n")
print("\n",'*'*100 ,"\n")
print("The last rows of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_data_two.tail())
print("\n",'*'*100 ,"\n")

x = 5

while True:
        explr = input("If you would like to explore more data type 'yes' and press enter or just press enter to skip ")
        if explr.lower() == "yes":
                x += 5
                print("-"*100)
                print("\n As per your selection you are watching the rows from row no. ", x-4,"to row no.",x," \n \n \n ", my_data.iloc[ x-5 : x ] )
                print("-"*100)
        else:
            break   


# In[22]:


print("\n",'*'*100 ,"\n")
print("The description of the data looks like following: \n \n")
print("\n",'*'*100 ,"\n")
print(my_data_two.describe())
print("\n",'*'*100 ,"\n")


# In[23]:


my_data_two.sort_values(by=['profit'], ascending = False)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > Now our data set are ready to give us the answers to our questions
# 
# ### Research Question 1 : who is the best movie director to invest my money with ?
# 

# In[24]:


#make a list of years 

years = my_data_two['release_year']
years_sorted = years.drop_duplicates().sort_values()
print(years_sorted, '\n\n\n', 'No. of years : ',years_sorted.value_counts().sum())


# In[25]:


#make list of directors

directors = my_data_two['director'].drop_duplicates().sort_values()
print(directors)


# Sub-Question (1) : who is the most profitable directors ?

# In[26]:


#find out the 5 directors with the maximum commulative profit

index1 = 0
max_profit = 0
profit_director_dict = {}

while index1 < 1713 :
    director_profit = my_data_two[my_data_two['director'] == directors.iloc[index1]]['profit'].sum()
    profit_director_dict[directors.iloc[index1]] = director_profit
    if director_profit > max_profit :
        max_profit = director_profit
        profit_director = directors.iloc[index1]
    index1 += 1

print( 'The director "',profit_director, '" has a comulative profit equals to "', max_profit, '$" which is the largest comulative profit ever','\n')
profit_director_df = pd.DataFrame.from_dict(profit_director_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]
print( 'and here is a list of the 5 highest comulative profit directors :',profit_director_df)


# ***Who is the most active director over years ?***

# In[27]:


def director_growth(fam_director) :
    
    """
    this function is called to find out how the cumulative profit 
    of a director is distributed over years
    """
    
    s = []
    t = 0

    while t < 56:

        i = years_sorted.iloc[t]
        a = my_data_two[my_data_two['release_year'] == i ]
        b = a[a['director'] == fam_director]
        c = b['profit'].sum()
        s.append(c)
        t += 1

    return(s)
 


# In[28]:


def plt_director(fam_director_name, fam_director_list) :
    
    """
    this function is called to plot how the cumulative profit 
    of a director is distributed over years
    """
    
    
    plt.plot(years_sorted, fam_director_list)
    plt.xlabel('Release Year')
    plt.ylabel('Profit')
    plt.title(fam_director_name)
    plt.show()


# In[29]:


steven = director_growth('Steven Spielberg')
steven2 = plt_director('Steven Spielberg', steven)


# ***
# This figure shows us how the comulative profit of "steven spleberg" is distributed over years
# ***

# In[30]:


my_data_two[my_data_two['director'] == 'Steven Spielberg'].sort_values(['profit'])


# ****************************************************************************************
# ***Warning : I think that our data set is not accurate enuogh to make money decisions and this is another limitation***
# ****************************************************************************************
# 
# ![image.png](attachment:image.png)

# In[31]:


peter = director_growth('Peter Jackson')
peter2 = plt_director('Peter Jackson', peter)


# ***
# This figure shows us how the comulative profit of "peter jackson" is distributed over years
# ***

# In[32]:


james = director_growth('James Cameron')
james2 = plt_director('James Cameron', james)


# ***
# This figure shows us how the comulative profit of "james cameron" is distributed over years
# ***

# In[33]:


michael = director_growth('Michael Bay')
michael2 = plt_director('Michael Bay', michael)


# ***
# This figure shows us how the comulative profit of "michael bay" is distributed over years
# ***

# In[34]:


david = director_growth('David Yates')
david2 = plt_director('David Yates', david)


# ***
# This figure shows us how the comulative profit of "David yates" is distributed over years
# ***

# In[35]:



plt.subplot(3,3,1)  
plt.plot(years_sorted, steven)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('steven')

plt.subplot(3,3,3)
plt.plot(years_sorted, peter)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('peter')

plt.subplot(3,3,5)
plt.plot(years_sorted, james)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('james')

plt.subplot(3,3,7)
plt.plot(years_sorted, michael)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('michael')

plt.subplot(3,3,9)
plt.plot(years_sorted, david)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('david')

plt.suptitle("Most Profitable Directors")
plt.show()


# In[36]:


plt.plot(years_sorted, steven, label = 'steven')

plt.plot(years_sorted, peter, label = 'peter')

plt.plot(years_sorted, james, label = 'james')

plt.plot(years_sorted, michael, label = 'michael')

plt.plot(years_sorted, david, label = 'david')

plt.xlabel('Release Year')
plt.ylabel('Profit')

plt.legend()

plt.show()

print("This figure show comparison between how the comulative profits of the 5 highest profit dirctors")


# >From this figure, I see that although "steven spielberg" has the highest cumulative profit but "james cameron" has the highest sparks over years

# ***Sub-Question (2) : who is the most popular directors ?***

# >at the beging, let us take a look at the relation between popularity and profit

# In[37]:


plt.scatter(my_data_two['popularity'], my_data_two['profit'])
plt.xlabel('popularity')
plt.ylabel('Profit')
plt.title('popularity - profit \n Positive Relation Proof' )
plt.show()


# > It is obvious that there is a positive relation between popularity and profit

# In[38]:


index2 = 0
max_popularity = 0
popular_director_dict = {}


while index2 < 1713 :
    director_popularity = my_data_two[my_data_two['director'] == directors.iloc[index2]]['popularity'].max()
    popular_director_dict[directors.iloc[index2]] = director_popularity
    if director_popularity > max_popularity :
        max_popularity = director_popularity
        popular_director = directors.iloc[index2]
    index2 += 1


popular_director_df = pd.DataFrame.from_dict(popular_director_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]

print("Top 5 directors gained max popularity")
popular_director_df


# In[39]:


index2 = 0
max_popularity = 0
popular_director_dict = {}


while index2 < 1713 :
    director_popularity = my_data_two[my_data_two['director'] == directors.iloc[index2]]['popularity'].mean()
    popular_director_dict[directors.iloc[index2]] = director_popularity
    if director_popularity > max_popularity :
        max_popularity = director_popularity
        popular_director = directors.iloc[index2]
    index2 += 1


popular_director_df = pd.DataFrame.from_dict(popular_director_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]

print("Top 5 directors gained highest mean popularity")

popular_director_df


# >"Colin Trevorrow" gained the highest popularity ever

# ### Research Question 2 : what is the best movie genre to invest my money in ?
# 

# ***Sub-Question (1) : what is the most profitable movie genre ?***

# In[40]:


#prepare a list of genres

genres = my_data_two['genres'].drop_duplicates()
print(genres)


# In[41]:


index3 = 0
max_genres = 0
profit_genres_dict = {}

while index3 < 1053 :
    genres_profit = my_data_two[my_data_two['genres'] == genres.iloc[index3]]['profit'].sum()
    profit_genres_dict[genres.iloc[index3]] = genres_profit
    if genres_profit > max_genres :
        max_genres = genres_profit
        profit_genres = genres.iloc[index3]
    index3 += 1

profit_genres_df = pd.DataFrame.from_dict(profit_genres_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]
print("Top 5 Genres ")
profit_genres_df


# In[42]:


def genres_growth(fam_genres) :
    
    """
    a function to find out the profit of genres over years
    """

    s = []
    t = 0

    while t < 56:

        i = years_sorted.iloc[t]
        a = my_data_two[my_data_two['release_year'] == i ]
        b = a[a['genres'] == fam_genres]
        c = b['profit'].sum()
        s.append(c)
        t += 1
        
    return(s)


# In[43]:


def plt_director(fam_genres_name, fam_genres_list) :
    
    """
    a function to plot the profit of genres over years
    """
    
    plt.plot(years_sorted, fam_genres_list)
    plt.xlabel('Release Year')
    plt.ylabel('Profit')
    plt.title(fam_genres_name)
    plt.show()


# In[44]:


comedy = genres_growth('Comedy')
comedy2 = plt_director('Comedy', comedy)


# >This figure show that the profit of comedy films increase year after year

# In[45]:


drama = genres_growth('Drama')
Drama2 = plt_director('Drama', drama)


# >This figure show that the profit of drama films increase year after year

# In[46]:


ComedyRomance = genres_growth('Comedy|Romance')
ComedyRomance2 = plt_director('Comedy|Romance', ComedyRomance)


# >This figure show that the profit of comedy or romance films increase year after year but not in the last years

# In[47]:


AdventureFantasyAction = genres_growth('Adventure|Fantasy|Action')
AdventureFantasyAction2 = plt_director('Adventure|Fantasy|Action', AdventureFantasyAction)


# >This figure show that the profit of dventure or fantasy or action films increase year after year but not in the last years

# In[48]:


Action_Adventure_ScienceFiction = genres_growth('Action|Adventure|Science Fiction')
Action_Adventure_ScienceFiction2 = plt_director('Action|Adventure|Science Fiction', Action_Adventure_ScienceFiction)


# >This figure show that the profit of action or adventure or science fiction films increase year after year, and here is the future

# In[49]:



plt.subplot(3,3,1)  
plt.plot(years_sorted, comedy)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('Comedy')

plt.subplot(3,3,3)
plt.plot(years_sorted, drama)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('Drama')

plt.subplot(3,3,5)
plt.plot(years_sorted, ComedyRomance)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('Comedy \n Romance')

plt.subplot(3,3,7)
plt.plot(years_sorted, AdventureFantasyAction)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('Adventure \n Fantasy \n Action')

plt.subplot(3,3,9)
plt.plot(years_sorted, Action_Adventure_ScienceFiction)
plt.xlabel('Release Year')
plt.ylabel('Profit')
plt.title('Action \n Adventure \n Science Fiction')

plt.suptitle("Most Profitable Directors")
plt.show()


# In[50]:


plt.plot(years_sorted, comedy, label = 'Comedy')

plt.plot(years_sorted, drama, label = 'Drama')

plt.plot(years_sorted, ComedyRomance, label = 'Comedy|Romance')

plt.plot(years_sorted, AdventureFantasyAction, label = 'Adventure|Fantasy|Action')

plt.plot(years_sorted, Action_Adventure_ScienceFiction, label = 'Action|Adventure|Science Fiction')

plt.xlabel('Release Year')
plt.ylabel('Profit')

plt.legend()

plt.show()

print("here is a comparison between distributed profit of top 5 genres over years")


# >The future of profit is for "action , adventure, science fiction" movies

# ***Sub-Question (2) : what is the most popular movie genre ?***

# In[51]:


index4 = 0
popular_gen_dict = {}


while index4 < 1053 :
    gen_popularity = my_data_two[my_data_two['genres'] == genres.iloc[index4]]['popularity'].max()
    popular_gen_dict[genres.iloc[index4]] = gen_popularity
    index4 += 1


popular_gen_df = pd.DataFrame.from_dict(popular_gen_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]

print("Top 5 genres according max popularity")
popular_gen_df


# In[52]:


index4 = 0
popular_gen_dict = {}


while index4 < 1053 :
    gen_popularity = my_data_two[my_data_two['genres'] == genres.iloc[index4]]['popularity'].mean()
    popular_gen_dict[genres.iloc[index4]] = gen_popularity
    index4 += 1


popular_gen_df = pd.DataFrame.from_dict(popular_gen_dict, orient='index').sort_values(by = [0], ascending=False).iloc[0:5]

print("Top 5 genres according mean popularity")

popular_gen_df


# In[108]:


def decision(decision_director, decision_genres) :
    
    """
    this function to find the profit over years for a specific director wirh specific genre

    """

    s = []
    t = 0

    while t < 56:

        i = years_sorted.iloc[t]
        a = my_data_two[my_data_two['release_year'] == i ]
        b = a.loc[(a['director'] == decision_director)  & (a['genres'] == decision_genres) ]
        c = b['profit'].sum()
        s.append(c)
        t += 1
    print(s)   
    return(s)


# In[109]:


def plt_decision(decision_name, decision_list) :
    
    """
    this function to plot the profit over years for a specific director wirh specific genre

    """
    
    plt.plot(years_sorted, decision_list)
    plt.xlabel('Release Year')
    plt.ylabel('Profit')
    plt.title(decision_name)
    plt.show()


# In[110]:


decision_a = decision('James Cameron', 'Action|Adventure|Science Fiction')
decision_aa = plt_decision( 'James Cameron  \n Action|Adventure|Science Fiction', decision_a)


# In[111]:


decision_a = decision('James Cameron', 'Adventure|Drama|Science Fiction')
decision_aa = plt_decision( 'James Cameron  \n Adventure|Drama|Science Fiction', decision_a)


# >Unfortunatily,James Cameron has no movies history of "Action|Adventure|Science Fiction" or "Adventure|Drama|Science Fiction" genre   
# But let us check the genres of movies he had directed before we might find some similar genres

# In[112]:


my_data_two.loc[my_data_two['director'] == 'James Cameron'].sort_values('genres')


# >Great,James Cameron has a great history of directing movies of similar genres

# In[113]:


#let's exclude 'Ghosts of the Abyss' because it is not similar genre

my_data_two.drop(my_data_two[my_data_two['original_title'] == 'Ghosts of the Abyss' ].index, inplace = True)


# In[114]:


James_similar_genres = my_data_two.loc[my_data_two['director'] == 'James Cameron'].sort_values('release_year')


# In[115]:


James_similar_genres


# >James Cameron similar genres

# In[116]:


James_similar_genres.describe()


# In[117]:


def plt_decision_s(decision_s, years_s, profit_s, popularity_s) :
    
    """
    this function to plot the profit and popularity over years for a specific director wirh similar genres

    """
         
    plt.plot(years_s, profit_s, label = 'profit')
    plt.plot(years_s, popularity_s, label = 'popularity')   
    plt.xlabel('Release Year')
    plt.title(decision_s)
    plt.legend()
    plt.show()


# In[118]:


#recall the plot fuction


a = James_similar_genres['release_year']
b = James_similar_genres['profit']
c = James_similar_genres['popularity']*100000000 #the popularity value is too small compared to profit and should be magnified to make sense

decision_aa = plt_decision_s( 'James_similar_genres', a, b, c )


# >James Cameron similar genres profit and popularity over years, Really Great History

# In[121]:


decision_a = decision('Colin Trevorrow', 'Action|Adventure|Science Fiction')
decision_aa = plt_decision( 'Colin Trevorrow  \n Action|Adventure|Science Fiction', decision_a)


# In[122]:


decision_a = decision('Colin Trevorrow', 'Adventure|Drama|Science Fiction')
decision_aa = plt_decision( 'Colin Trevorrow  \n Adventure|Drama|Science Fiction', decision_a)


# >Unfortunatily,Colin Trevorrow has no movies history of "Action|Adventure|Science Fiction" or "Adventure|Drama|Science Fiction" genre
# But let us check the genres of movies he had directed before we might find some similar genres

# In[124]:


my_data_two.loc[my_data_two['director'] == 'Colin Trevorrow'] 


# >Unfortunately, we do not have a lot of data about Colin Trevorrow works but one of his works is "Jurassic World" which is one of the most popular and profitable movies over the whole history

# ![image.png](attachment:image.png)

# >Colin Trevorrow is one of the greatest directors ever but unfortunately the data we have - specially atfer cleaning - does not contain most of his works

# <a id='conclusions'></a>
# ## Conclusions
# 
# The purpose of this business study was to make a data-driven decision of which genre of movies should i invest my money in and who is the best movie director should i invest my money with
# 
# and after investigating TMDb i found the following:
# 
# >For the movie director i would select one of the following:
# >1. James Cameron (regarding to profit, he is one of the highest profits directors and is more active over years)
# >2. Colin Trevorrow (regarding to popularity he is one of the most popular ever)
# 
# >For the movie genre i would select one of the following:
# >1. Action|Adventure|Science Fiction (regarding to profit, this genre is one of the highest profits directors and is more active over years)
# >2. Adventure|Drama|Science Fiction (regarding to popularity this genre is one of the most popular ever)
# 

# ### More analysis
# 
# >in the future we can consider also the "run time" of the movie to find out which is more profitable the short or long films

# *********************************************
# ### limitations
# **********************************************
# 
# 1. 65% of the raw data was cleaned and only 35% of the data was valid for the analysis which may lead to inaccurate or biased resultes 
# 
# 2. I googled some data from TMDb and unfortunatily it was not accurate enough to make money decisions
# 
# >Unfortunaltly niether James Cameron or Colin Trevorrow have a previous works of these exact genres "Action|Adventure|Science Fiction" and "Adventure|Drama|Science Fiction" but they had great works with similar genres  
# ***however I think that a movie directed by both "James Cameron and Colin Trevorrow" of the genre "Action|Adventure|Drama|Science Fiction" would be a great investment opportunity***

# <a id='refs'></a>
# ## References
# 
# >https://pydata.org/ ||
# https://stackoverflow.com/ ||
# https://www.geeksforgeeks.org/||
# https://medium.com/
