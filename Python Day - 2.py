#!/usr/bin/env python
# coding: utf-8

# # Glossary Terms 

# Algorithm: A set of instructions for solving a problem or accomplishing a task
# 
# Boolean: A data type that has only two possible values, usually true or false
# 
# Branching: The ability of a program to alter its execution sequence
# 
# Comparator: An operator that compares two values and produces Boolean values (True/False)
# 
# def: A keyword that defines a function at the start of the function block
# 
# Docstring: A string at the beginning of a function’s body that summarizes the function’s behavior and explains its arguments and return values
# 
# elif: A reserved keyword that executes subsequent conditions when the previous conditions are not true 
# 
# else: A reserved keyword that executes when preceding conditions evaluate as False
# 
# Function: A body of reusable code for performing specific processes or tasks
# 
# if: A reserved keyword that sets up a condition in Python
# 
# Logical operator: An operator that connects multiple statements together and performs complex comparisons
# 
# Modularity: The ability to write code in separate components that work together and that can be reused for other programs
# 
# Modulo: An operator that returns the remainder when one number is divided by another
# 
# Refactoring: The process of restructuring code while maintaining its original functionality
# 
# return: A reserved keyword in Python that makes a function produce new results which are saved for later use
# 
# Reusability: The capability to define code once and using it many times without having to rewrite it
# 
# Self-documenting code: Code written in a way that is readable and makes its purpose clear

# ## Functions! 

# In[12]:


def Grade_Is(Grade):
    if Grade >= 45:
        print("You have Passed")
    else:
        print("You have not Passed")
    return Grade


# In[13]:


def Grade_Is(Grade):
    if isinstance(Grade, (int, float)):  # Check if Grade is numeric
        if Grade >= 45:
            print("You have Passed")
        else:
            print("You have not Passed")
    else:
        print("Invalid input. Please provide a numeric grade.")
    
    return Grade


# In[14]:


def area_triangle(base, height):
    return base*height/2


# In[15]:


area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

total_area = area_a + area_b

total_area


# In[26]:


def get_seconds(hr , minute , sec):
    total_seconds = 3600*hr + 60*minute + seconds
    return total_seconds


# In[30]:


def get_seconds(hr , minute , sec):
    total_seconds = 3600*hr + 60*minute + sec
    return total_seconds

get_seconds(1,2,3)


# In[31]:


def area_triangle(base,height):
    area = base * height * (1/2)
    return area

area_triangle(12,4)


# In[37]:


name = str(input("Enter your name please!"))
length = len(name)
number = length * 9

print ("Hello " + name + ", Your Lucky Number is " + str(number))


# In[38]:


def lucky_no(name):
    number = len(name)* 9
    print ("Hello " + name + ", Your Lucky Number is " + str(number))
    
lucky_no("Saradind")
lucky_no("Sai")


# ## Comparators in Python!!!!

# In[39]:


print(10>1)


# In[40]:


print(10<1)


# In[41]:


print(2 != 2)


# In[42]:


print(2 != 1)


# In[44]:


print(2>1 and 1>2) 


# 
# Even if one statement is True, the AND operator prints as False

# In[46]:


print(2>1 or 1>2) 


# The OR operator is different

# In[47]:


x = 3
my_list = [3, 4, 6, 10]
print(x < 3 and x != 0)
print(x >= len(my_list) or x == min(my_list))
print(x not in my_list)


# ## IF AND IF ELSE STATEMENTS!!!! 

# In[61]:


def username_generator(username):
    if len(username) <= 3:
        print("Username Too Short")
    else:
        print("Username Accepted")

# Example usage:
username = input("Enter a Username Please: ")
username_generator(username)


# In[65]:


def username_length(username):
    if len(username) < 8:
        print("Invalid Username, Must be at least 8 characters in length")
    else:
        print("Username Accepted!")

username_check = input("Enter Your Username Please: ")
username_length(username_check)


# In[71]:


def is_even(number):
    if number % 2 == 0:
        print("The number " , number , " is EVEN")
    else:
        print("The number " , number , " is ODD")
number = int(input("Enter a Number"))
is_even(number)


# In[72]:


is_even(12)


# #### The define we have used till now can be called now: 

# In[73]:


Grade_Is(23)


# In[74]:


area_triangle(5,4)


# In[75]:


get_seconds(1,2,3)


# In[76]:


lucky_no("Saradind")


# In[78]:


username_generator('saradind')


# In[79]:


is_even(26547454)


# In[80]:


def weather_condition(weather):
    if weather == 'Sunny':
        print("I think we can go for a Game outside!")
    elif weather == 'Rainy':
        print("You can watch a Movie whie eating Pakodas!")
    elif weather == 'Cold':
        print("A cup of coffee always helps!")
    elif weather == 'Humid':
        print("Better not step Out!")
    else:
        print("Select from the following: Rainy,Cold,Humid or Sunny")
    
weather = str(input("Enter how the weather looks today!"))
weather_condition(weather)


# In[81]:


weather_condition('winter')


# In[85]:


def username_again(username):
    if len(username) < 8:
        print("The username can not be less than 8 characters")
    else:
        if len(username) > 20:
            print("The username can not be over 20 characters")
        else:
            print("Valid Username")
username = str(input("Enter a new username please!"))
username_again(username)

