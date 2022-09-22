#!/usr/bin/env python
# coding: utf-8

# # Que 1: What are escape characters, and how do you use them?

# In[ ]:


Answer 1:
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.


# # Que 2: What do the escape characters n and t stand for?

# In[ ]:


Answer 2:
escape charater is  "\" backlash
"\n" stands for newline
"\t" stands for tab


# # Que 3: What is the way to include backslash characters in a string?

# In[ ]:


Answer 3:
if you want to include a backslash character itself, 
you need two backslashes or use the @ verbatim string. 


# # Que 4:The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# In[ ]:


Answer 4:
The single quote in Howl's is fine because we've used double 
quotes to mark the beginning and end of the string.


# # Que 5 : How do you write a string of newlines if you don't want to use the n character?

# In[ ]:


Answer 5:
Multiline strings allow you to use newlines in strings. 


# # Que 6: What are the values of the given expressions?
# 'Hello, world!'[1]
# 'Hello, world!''[0:5]
# 'Hello, world!'[:5]
# 'Hello, world'[3:]

# In[1]:


'Hello, world!'[1]


# In[2]:


'Hello, world!'[0:5]


# In[3]:


'Hello, world!'[:5]


# In[4]:


'Hello, world'[3:]


# # Que 7: What are the values of the following expressions?
# 'Hello'.upper()
# 'Hello'.upper().isupper()
# 'Hello'.upper().lower()

# In[5]:


'Hello'.upper()


# In[6]:


'Hello'.upper().isupper()


# In[7]:


'Hello'.upper().lower()


# # Que 8:What are the values of the following expressions?
# 'Remember, remember, the fifth of July.'.split()
# '-'.join('There can only one.'.split()) 

# In[8]:


'Remember, remember, the fifth of July.'.split()


# In[9]:


'-'.join('There can only one.'.split())


# # Que 9: What are the methods for right-justifying, left-justifying, and centering a string?

# In[ ]:


Answer 9:
The rjust(), ljust(), and center() string methods, respectively


# # Que 10: What is the best way to remove whitespace characters from the start or end?

# In[ ]:


Answer 10:
The lstrip() and rstrip() methods remove whitespace from 
the left and right ends of a string, respectively.

