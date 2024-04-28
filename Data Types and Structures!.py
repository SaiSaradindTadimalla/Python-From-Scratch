#!/usr/bin/env python
# coding: utf-8

# # Let's get to know about Data types & Data Structures!

# ## Lists!!!!!!

# In[6]:


List_1 = [34, 34,23,65,88,44,23,76]
print(List_1[1])


# In[4]:


List_2 = ['Ace','Itachi','Sasuke','Law','Sanji','Sung']
print(List_2[3])


# In[8]:


'Itachi' in List_2


# In[14]:


List_2.index('Sanji')


# In[12]:


Index_of_Itachi = List_2.index('Itachi')
print(Index_of_Itachi)


# In[16]:


List_2.append('Aizen')


# In[17]:


List_2


# In[18]:


List_2.insert(2 ,'Gojo')


# In[19]:


List_2


# In[20]:


List_2.remove('Law')


# In[21]:


List_2


# ### Tuples!!!
# 

# In[22]:


Tuple1 = ('Itachi','Sanji','Sung','Aizen')


# In[23]:


Tuple1


# In[41]:


Fav_Characters = [
    ('Itachi Uchiha','Naruto','5/5'),
    ('Vinsmoke Sanji','One Piece','5/5'),
    ('Gojo Satoru','Jujutsu Kaisen','4/5'),
    ('Sung Jin Woo','Solo Leveling','5/5'),
    ('Aizen Sosuke','Bleach','5/5'),
    ('Sasuke Uchiha','Naruto','3/5'),
    ('Portugas D Ace','One Piece','3/5'),    
]


# In[27]:


Fav_Characters


# ## Complexity with Loops, Lists and Tuples!!!

# In[28]:


Fav_Characters


# In[41]:


def rating(Chars):
    result =[]
    for name, anime, rating in Chars:
        result.append("Name: {} \nRating: {}".format(name, rating))
    return result
for chars in rating(Fav_Characters):
    print(chars)
    


# In[33]:


def rating(Chars):
    result = []
    for name, anime, rating in Chars:
        result.append("Name: {} \nRating: {}".format(name, rating))
    return result

for chars in rating(Fav_Characters):
    print(chars)


# In[1]:


for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]" , end="")
    print('\n')


# In[15]:


Countries = ['India','Singapore','Saudi Arabia']
Capitals = ['Delhi','Singapore','Riyad']
Countries_Capitals = zip(Countries , Capitals)
print(Countries_Capitals)
print(list(Countries_Capitals))


# In[17]:


Countries_Capitals = zip(Countries, Capitals)


# In[18]:


Countries, Capitals = zip(*Countries_Capitals)  # Unzipping the zipped object
print(Countries)
print(Capitals)


# In[21]:


Fav = ['Itachi','Sanji','Zoro','Sung Jin Woo','Hinata','Robin','Nami','Nobara','Maki']
for index, Fav in enumerate(Fav):
    print(index, Fav)


# In[22]:


Fav = ['Itachi','Sanji','Zoro','Sung Jin Woo','Hinata','Robin','Nami','Nobara','Maki']
for index, Fav in enumerate(Fav , 1):
    print(index, Fav)


# ## Let's move to Dictionaries 

# In[27]:


Favourite_Food = {
    'Vineeth' : 'Biriyani',
    'Uma'     : 'Shawarma',
    'Vamsi' : 'Burgers',
    'Sai' : 'Pizza',
    'Ankith' : 'Milkshake'
}


# In[28]:


print(Favourite_Food)


# In[31]:


Favourite_Food['Sai']


# In[32]:


Favourite_Food['Pizza']


# In[35]:


Favourite_Character = dict(
    Vineeth = 'Zoro',
    Uma     = 'Shanks',
    Vamsi = 'Ayanokyoji',
    Sai = 'Itachi Uchiha',
    Ankith = 'Kakashi Hatake'
)


# In[37]:


Favourite_Character['Nani'] = 'Crocodile'
Favourite_Character


# In[38]:


print('Uma' in Favourite_Character)


# In[42]:


print(Fav_Characters)


# In[47]:


def rating(Chars):
    result =[]
    for name, anime, rating in Chars:
        result.append("Name: {} \nRating: {}".format(name, rating))
    return result
for chars in rating(Fav_Characters):
    print(chars)


# In[50]:


new_methood = {}
for name, anime, rating in Fav_Characters:
    if anime in new_methood:
        new_methood[anime].append((name, rating))
    else:
        new_methood[anime] = [(name, rating)]
new_methood


# In[51]:


new_methood['One Piece']


# In[52]:


new_methood['Naruto']


# In[53]:


new_methood['Bleach']


# In[54]:


new_methood['Jujutsu Kaisen']


# In[55]:


new_methood['Solo Leveling']


# In[ ]:




