#!/usr/bin/env python
# coding: utf-8

# ## Glossary Terms 

# break: A keyword that lets a user escape a loop without triggering any ELSE statement that follows it in the loop
# 
# Concatenate: To link or join together
# 
# Escape character: A character that changes the typical behavior of the characters that follow it
# 
# For loop: A piece of code that iterates over a sequence of values
# 
# format(): A string method that formats and inserts specific substrings into designated places within a larger string
# 
# index(): A string method that outputs the index number of a character in a string
# 
# Indexing: A way to refer to the individual items within an iterable by their relative position
# 
# Iterable: An object that’s looped, or iterated, over
# 
# Iteration: The repeated execution of a set of statements, where one iteration is the single execution of a block of code
# 
# Loop: A block of code used to carry out iterations 
# 
# range(): A Python function that returns a sequence of numbers starting from zero, increments by 1 by default, and stops before the given number 
# 
# String slice: A portion of a string that can contain more than one character; also referred to as a substring 
# 
# While loop: A loop that instructs the computer to continuously execute the code based on the value of a condition

# ## String Slicing & Indexing
# 

# Indexing always starts with zero

# In[2]:


pets = 'cats and dogs'
pets.index('s')


# In[3]:


pets.index('ca')


# In[7]:


pets[1]


# In[9]:


pets[6]


# In[10]:


pets[-1]


# In[11]:


pets[-6]


# Let's go into String Slicing now

# In[12]:


Name = 'Vinsmoke Sanji'
Name[1:2]


# In[13]:


Name[1:3]


# In[14]:


Name[0:3]


# In[20]:


Name[1:6]


# In[21]:


Name[8:]


# In[24]:


'Sanji' in Name


# ## Format Method in Python

# In[33]:


First_Name = str(input("Please Enter Your First Name: "))
Middle_Name = str(input("Please Enter Your Middle Name: "))
Last_Name = str(input("Please Enter Your Last Name: "))
Age = int(input("Please Enter Age: "))

print("Hello your full name is {} {} {}, and your age is {}. " .format(First_Name, Middle_Name, Last_Name, Age))


# In[31]:


import random

Name = str(input("Please Enter Your Name: "))
Number = int(input("Please Enter Your Favorite Number: "))

# List of characters
characters = ['Sanji', 'Zoro', 'Luffy', 'Ace', 'Nami', 'Usopp', 'Franky', 'Robin', 'Brook', 'Jimbei', 'Chopper']

# Randomly select a character
your_character = random.choice(characters)

print("Hello {}, your character is {}." .format(Name, your_character))


# In[43]:


def to_celcius(x):
    return (x-32)* 5/9

for x in range(0, 100, 10):
    print(' {:>3} F | {:>6.2f} C' .format(x , to_celcius(x)))

