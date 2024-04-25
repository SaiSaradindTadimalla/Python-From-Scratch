#!/usr/bin/env python
# coding: utf-8

# ## Glossary terms

# Argument: Information given to a function in its parentheses
# 
# Assignment: The process of storing a value in a variable
# 
# Attribute: A value associated with an object or class which is referenced by name using dot notation
# 
# Cells: The modular code input and output fields into which Jupyter Notebooks are partitioned
# 
# Class: An object’s data type that bundles data and functionality together
# 
# Computer programming: The process of giving instructions to a computer to perform an action or set of actions
# 
# Data type: An attribute that describes a piece of data based on its values, its programming language, or the operations it can perform
# 
# Dot notation: How to access the methods and attributes that belong to an instance of a class
# 
# Dynamic typing: Variables that can point to objects of any data type
# 
# Explicit conversion: The process of converting a data type of an object to a required data type
# 
# Expression: A combination of numbers, symbols, or other variables that produce a result when evaluated
# 
# Float: A data type that represents numbers that contain decimals
# 
# Immutable data type: A data type in which the values can never be altered or updated
# 
# Implicit conversion: The process Python uses to automatically convert one data type to another without user involvement
# 
# Integer: A data type used to represent whole numbers without fractions
# 
# Jupyter Notebook: An open-source web application for creating and sharing documents containing live code, mathematical formulas, visualizations, and text
# 
# Keyword: A special word in a programming language that is reserved for a specific purpose and that can only be used for that purpose
# 
# Markdown: A markup language that lets the user write formatted text in a coding environment or plain-text editor 
# 
# Method: A function that belongs to a class and typically performs an action or operation
# 
# Naming conventions: Consistent guidelines that describe the content, creation date, and version of a file in its name
# 
# Naming restrictions: Rules built into the syntax of a programming language 
# 
# Object: An instance of a class; a fundamental building block of Python
# 
# Object-oriented programming: A programming system that is based around objects which can contain both data and code that manipulates that data
# 
# Programming languages: The words and symbols used to write instructions for computers to follow
# 
# String: A sequence of characters and punctuation that contains textual information
# 
# Syntax: The structure of code words, symbols, placement, and punctuation
# 
# Typecasting: Converting data from one type to another (see explicit conversion)
# 
# Variable: A named container which stores values in a reserved location in the computer’s memory

# # Basic Python Statements

# ### Let us start with the simple Print Statements!

# In[27]:


print("Hello World!")


# In[1]:


print(222)


# ### Now let us move on to the Type Statement!

# In[13]:


type('Hello Python')


# In[10]:


type(222)


# In[11]:


type('222')


# In[12]:


type('FALSE')


# ### What about going forward to the IF-ELSE Statements? 

# In[18]:


age = int(input())
if age >= 18:
    print ("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# In[32]:


Percentage = int(input())
if Percentage >= 90:
    print ("A")
elif Percentage >=80:
    print("B")
elif Percentage >= 70:
    print("C")
elif  Percentage >= 60:
    print("D")
else:
    print("F")


# ### Lists basic Statements 

# In[20]:


for numbers in [1,2,3,4,5,6]:
    print(numbers)


# In[25]:


my_list = [2,4,8]
for x in my_list:
    print(x/2)


# ### Defining a Function??? 

# In[2]:


def vote(age):
    if age >= 18:
        print("Is Eligible to Vote")
    else:
        print("Is not Eligible to Vote")


# In[3]:


vote(12)


# In[4]:


vote(59)


# In[5]:


Name = "SARADIND SAI"


# In[6]:


print(type(Name))


# In[8]:


Name = Name.swapcase()
Name


# In[10]:


Name = Name.replace("SAI", "TADIMALLA")
Name


# ### We don't have to memorise all the Methods, instead after the dot press the TAB key and you get all the Methods you can ues for that Function!

# In[15]:


Name = Name.capitalize()


# # Variables & Datatypes!

# In[17]:


age_list = [23,65,34,21,16,99]
age_list


# In[19]:


max_age = max(age_list)
max_age


# In[20]:


min_age = min(age_list)
min_age


# In[22]:


max_age = str(max_age)
max_age


# In[23]:


type(max_age)


# In[30]:


S = ("This is a String")


# In[37]:


S


# In[38]:


type(S)


# In[35]:


I = 5 # this is an Integer


# In[34]:


I 


# In[36]:


type(I)


# In[39]:


F = 2.345 # this is Float 


# In[40]:


F


# In[41]:


type(F)


# ### Converting Datatypes: 

# ##### Implicit Conversion 

# In[42]:


print(2 + 2.5)  #self identification of the Datatype


# ##### Explicit Conversion

# In[43]:


print('2+2 = ' + str(2+2))   #We provide the Datatype we require


# In[ ]:




