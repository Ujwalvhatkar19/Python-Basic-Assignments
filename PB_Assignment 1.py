#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QUE1:
In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
()
+
6


# In[ ]:


Answer 1:
Operators: +, -, *, /
Values: 'hello', -88.5, 6


# In[ ]:


QUE 2:
get_ipython().set_next_input('What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[ ]:


Answer 2:
Variable is something which already have lables. Like int, complex, float.  
String is a series of character / data in single or double quotes. 


# In[ ]:


QUE 3:
Describe three different data types.


# In[ ]:


Answer 3:
1.Boolean data type which stores True & False data.
2.Numeric data type in which there are three sub type a) int b)complex c)float . 
3.Set data type in which list will be in unorder that random order but set is unchangable, unordered and duplicates are not allowed. 


# In[ ]:


QUE 4:
get_ipython().set_next_input('What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


Answer 4:
Expression is made up of variables, values, operators and functions too. 
We can evaluate the expressions then we will get the result.


# In[ ]:


QUE 5:
This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')


# In[ ]:


Answer 5:
Statement is something that python interprefer can execute. So spam=10 is a statement. 
An Expression always evaluates to a value.


# In[ ]:


QUE 6:
get_ipython().set_next_input('After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[ ]:


Answer 6:
The bacon variable is set to 20. 
The bacon + 1 expression does not reassign the value in bacon 
(that would need an assignment statement: bacon = bacon + 1)


# In[ ]:


QUE 7:
get_ipython().set_next_input('What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' *3 


# In[6]:


'spam' + 'spamspam'


# In[7]:


'spam' *3 


# In[ ]:


Answer 7:
For both the term value will be same 'spamspamspam'


# In[ ]:


QUE 8:
get_ipython().set_next_input('Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')


# In[ ]:


Answer 8:
Variable has some limitations. Variable can start with alphabates only so thats why eggs is valid variable
and for 100 it is invalid as Variables are sensitive. Variables cannot start with numbers. so we can declare them as a separate variable, and after that, you can concatenate number
with string


# In[ ]:


QUE 9:
What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')


# In[ ]:


Answer 9:
The int(), float(), and str() functions will evaluate to the integer, floating-point number,
and string versions of the value passed to them.


# In[ ]:


QUE 10:
get_ipython().set_next_input('Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten'; + 99 + 'burritos'


# In[ ]:


Answer 10:
The expression causes an error because 99 is an integer, 
and only strings can be concatenated to other strings with the + operator. 
The correct way is 'I have eaten ' + str(99) + ' burritos.'.


# In[ ]:




