#!/usr/bin/env python
# coding: utf-8

# # Que 1: What does an empty dictionary's code look like?

# In[ ]:


Answer 1:
    Two curly brackets: {}


# # Que 2:What is the value of a dictionary value with the key 'foo' and the value 42?

# In[1]:


Answer 2:
{'foo' : 42}


# # Que 3: What is the most significant distinction between a dictionary and a list?

# In[ ]:


The items stored in a dictionary are unordered, while the items in a list are ordered.


# # Que 4:What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# In[ ]:


Answer 4:
You get a KeyError error.


# # Que 5: If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[ ]:


Answer 5:
    There is no difference. 
    The in operator checks whether a value exists as a key in the dictionary.


# # Que 6: If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# In[ ]:


'cat' in spam checks whether there is a 'cat' key in the dictionary,
while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# # Que 7: What is a shortcut for the following code?
# if 'color' not in spam:
# spam['color'] = 'black'

# In[ ]:


spam.setdefault('color', 'black')


# # Que 8: How do you "pretty print" dictionary values using which module and function?

# In[ ]:


pprint.pprint()

