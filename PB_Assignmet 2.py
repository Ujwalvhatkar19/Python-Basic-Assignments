#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QUE 1:
get_ipython().set_next_input('What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:


Answer 1:
There are 2 values of Boolean data type that is True & False. It can be written in first letter will be Capital that is 
T & F and remaining will be lower case.


# In[ ]:


Que 2:
get_ipython().set_next_input('What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


Answer 2:
3 differetnt boolean operators are and, or, not. 


# In[ ]:


Que 3:
Make a list of each Boolean operator truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).


# In[ ]:


Anwer 3:
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True 
False or True is True 
False or False is False

not True is False
not False is True


# In[ ]:


Que 4:
get_ipython().set_next_input('What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[ ]:


False
False
True
False
False
True 


# In[ ]:


Que 5:
    get_ipython().set_next_input('    What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


Answer 5:
==, !=, <, >, <=, and >=.


# In[ ]:


Que 6:
How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.


# In[ ]:


Answer 6:
== is the equal to operator that compares two values and evaluates to a Boolean, while = is the
assignment operator that stores a value in a variable.
A condition is an expression used in a flow control statement that evaluates to a Boolean value.


# In[ ]:


Que 7:
Identify the three blocks in this code:
spam = 0
if spam == 10:
print("eggs")
if spam > 5:
print("bacon")
else:
print('ham')
print('spam')
print('spam')


# In[ ]:


Answer 7:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')


# In[ ]:


Que 8:
Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.


# In[39]:


spam = 3
if spam ==1:
    print('Hello')
elif spam == 2:
    print ('Howdy')
else:
    print ("Greetings!")


# In[ ]:


Que 9:
get_ipython().set_next_input('If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')


# In[ ]:


Answer 9:
Need to click on CTRL + C if programme stuck in endless loop.


# In[ ]:


Que 10:
    get_ipython().set_next_input('    How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')


# In[ ]:


Answer 10:
Break actually terminate the execuation of current loop and pass the control over next loop.
Continue actually control reamins within the loop.


# In[ ]:


Que 11:
In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[ ]:


Answer 11:
In range function there are 3 different parameters start, stop, step
in this range funtion it is not compulsory to have start function.


# In[ ]:


Que 12:
Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalentprogram that prints the numbers 1 to 10 using a while loop.


# In[9]:


a = 1
while a < 11:
    print (a)
    if a == 10:
        break
    a = a + 1


# In[6]:


t = (1,2,3,4,5,6,7,8,9,10)


# In[7]:


for i in t:
    print (i)


# In[ ]:


Que 13:
If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


Answer 13:
This function called spam.bacon()

