#!/usr/bin/env python
# coding: utf-8

# # Que 1: Is the Python Standard Library included with PyInputPlus?

# In[ ]:


Answer 1:
PyInputPlus is not a part of the Python Standard Library, 
we must install it separately using Pip.


# # Que 2:Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# In[ ]:


Answer 2:
we can import the module with import pyinputplus as pyip so that we can enter a 
shorter name when calling the module’s functions.


# # Que 3: How do you distinguish between inputInt() and inputFloat()?

# In[ ]:


Answer 3:
when we use InputInt programme expects an integer and when the we use inputFloat that time it 
expects float value i.e numbers with decimal.  


# # Que 4: Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# In[ ]:


Answer 4:
By using pyip.inputInt(min = 0, max = 99)


# # Que 5: What is transferred to the keyword arguments allowRegexes and blockRegexes?

# In[ ]:


Answer 5:
regex strings that are either explicitly allowed or denied.


# # Que 6: If a blank input is entered three times, what does inputStr(limit=3) do?

# In[ ]:


Answer 6:
The function will raise RetryLimitException.


# # Que 7:If blank input is entered three times, what does inputStr(limit=3, default= 'hello') do?

# In[ ]:


Answer 7:
The function returns the value 'hello'


# In[ ]:




