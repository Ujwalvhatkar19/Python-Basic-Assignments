#!/usr/bin/env python
# coding: utf-8

# # Que 1:
# Create an assert statement that throws an AssertionError if the variable spam is a negative
# integer.

# In[ ]:


Answer 1:
assert spam >= 10, 'The spam variable is less than 10'


# # Que 2: Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, &#39;hello&#39; and &#39;hello&#39; are considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same). 

# In[ ]:


Annswer 2:
assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!'


# # Que 3: Create an assert statement that throws an AssertionError every time.

# In[ ]:


Answer 3:
assert False, 'This assertion always triggers.'


# # Que 4: What are the two lines that must be present in your software in order to call logging.debug()?

# In[ ]:


Answer 4:
import logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s %(levelname)s %(message)s')


# # Que 5: What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

# In[ ]:


Answer 5:
import logging
logging.basicConfig(filename= 'programeLogtext', level=logging.DEBUG, format = '%(asctime)s %(levelname)s %(message)s')


# # Que 6: What are the five levels of logging?

# In[ ]:


Answer 6:
DEBUG, INFO, WARNING, ERROR, CRITICAL


# # Que 7: What line of code would you add to your software to disable all logging messages?

# In[ ]:


Answer 7: 
logging.disable(logging.CRITICAL)


# # Que 8:Why is using logging messages better than using print() to display the same message?

# In[ ]:


Answer 8:
We can disable logging messages without removing the logging function calls. 
We can selectively disable lower-level logging messages. We can create logging messages. 
Logging messages provides a timestamp.


# # Que 9: What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# In[ ]:


Abswer 9:
The Step In button will move the debugger into a function call. The Over button will quickly 
execute the function call without stepping into it. The Out button will quickly execute the 
rest of the code until it steps out of the function it currently is in.


# # Que 10: After you click Continue, when will the debugger stop ?

# In[ ]:


Answer 10: 
the debugger will stop when it has reached the end of the program or a line with a breakpoint.


# # Que 11: What is the concept of a breakpoint?

# In[ ]:


Answer 11: 
A breakpoint is a setting on a line of code that causes the debugger to pause when the 
program execution reaches the line.

