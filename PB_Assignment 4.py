#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Que 1:
    What exactly is []?


# In[ ]:


Answer 1:
    This is empty list value which do not have any items inside.


# In[ ]:


Que 2:
    In a list of values stored in a variable called spam, how would you assign the value 'hello'
    as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
    Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.


# In[ ]:


Answer 2:
    Spam[2] = 'hello'


# In[ ]:


Que 3:
    What is the value of spam[int(int('3' * 2) / 11)]?


# In[ ]:


Answer 3:
    'd'


# In[ ]:


Que 4:
    What is the value of spam[-1]?


# In[ ]:


Answer 4:
    'd' 


# In[ ]:


Que 5:
    What is the value of spam[:2]?


# In[ ]:


Answer 5:
    ['a', 'b']


# In[ ]:


Que 6:
    What is the value of bacon.index('cat')?


# In[ ]:


Answer 6:
    1


# In[ ]:


Que 7:
    get_ipython().set_next_input('    How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')


# In[ ]:


Answer 7:
    [3.14, 'cat', 11, 'cat', True, 99]


# In[ ]:


Que 8:
    get_ipython().set_next_input("    How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')


# In[ ]:


Answer 8:
    [3.14, 11, 'cat', True, 99]


# In[ ]:


Que 9:
    get_ipython().set_next_input('    What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


Answer 9: 
    List concentration operation is '+' and for replication is '*'


# In[ ]:


Que 10:
    What is difference between the list methods append() and insert()?


# In[ ]:


Answer 10:
    While append() will add values only to the end of a list, 
    insert() can add them anywhere in the list.


# In[ ]:


Que 11:
    get_ipython().set_next_input('    What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:


Answer 11:
    The del statement and the remove() list method are two ways to remove values from a list.


# In[ ]:


Que 12:
    Describe how list values and string values are identical.


# In[ ]:


Answer 12:
    Both lists and strings can be passed to len(), have indexes and slices, 
    be used in for loops, be concatenated or replicated, 
    and be used with the in and not in operators.


# In[ ]:


Que 13:
    get_ipython().set_next_input('    What is the difference between tuples and lists');get_ipython().run_line_magic('pinfo', 'lists')


# In[ ]:


Answer 13:
    Lists are mutable; they can have values added, removed, or changed. 
    Tuples are immutable; they cannot be changed at all. Also,
    tuples are written using parentheses, ( ujwal ), 
    while lists use the square brackets, [ ujwal ].


# In[ ]:


Que 14:
    How do you type a tuple value that only contains the integer 42?


# In[ ]:


Answer 14:
    (42,) 
    The trailing comma is mandatory


# In[ ]:


Que 15:
    get_ipython().set_next_input("    How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')


# In[ ]:


Answer 15:
    The tuple() and list() functions, respectively


# In[ ]:


Que 16:
    Variables that "contain" list values are not necessarily 
    get_ipython().set_next_input('    lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')


# In[ ]:


Answer 16:
    They contain references to list values.


# In[ ]:


Que 17:
    How do you distinguish between copy.copy() and copy.deepcopy()?


# In[ ]:


Answer 17:
    The copy.copy() function will do a shallow copy of a list, 
    while the copy.deepcopy() function will do a deep copy of a list. 
    That is, only copy.deepcopy() will duplicate any lists inside the list.

