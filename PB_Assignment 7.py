#!/usr/bin/env python
# coding: utf-8

# # Que 1: What is the name of the feature responsible for generating Regex objects?

# In[ ]:


Answer 1: 
The re.compile() function returns Regex objects.


# # Que 2: Why do raw strings often appear in Regex objects?
Answer 2:
Raw strings are used so that backslashes do not have to be escaped.
# # Que 3: What is the return value of the search() method?

# In[ ]:


Answer 3
The search() method returns Match objects.


# # Que 4: From a Match item, how do you get the actual strings that match the pattern?

# In[ ]:


Answer 4: 
The group() method returns strings of the matched text.


# # Que 5: In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 2? Group 1?

# In[ ]:


Answer 5:
Group 0 is the entire match, group 1 covers the first set of parentheses,
and group 2 covers the second set of parentheses.


# # Que 6:
# In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
# a regex that you want it to fit real parentheses and periods?

# In[ ]:


Answer 6:
Periods and parentheses can be escaped with a backslash: \., \(, and \).


# # Que 7:
# The findall() method returns a string list or a list of string tuples. What causes it to return one of
# the two options?

# In[ ]:


Answer 7:
If the regex has no groups, a list of strings is returned. If the regex has groups, 
a list of tuples of strings is returned.


# # Que 8:In standard expressions, what does the | character mean?

# In[ ]:


Answer 8:
The | character signifies matching "either, or" between two groups.


# # Que 9:In regular expressions, what does the character stand for?

# In[ ]:


Answer 9:
character can either mean "match zero or one of the preceding group" 
or be used to signify nongreedy matching.


# # Que 10. In regular expressions, what is the difference between the + and * characters?

# In[ ]:


Answer 10:
The + matches one or more. The * matches zero or more.


# # Que 11: What is the difference between {4} and {4,5} in regular expression?

# In[ ]:


Answer 11:
The {4} matches exactly four instances of the preceding group. 
The {4,5} matches between four and five instances


# # Que 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?

# In[ ]:


Answer 12:
The \d, \w, and \s shorthand character classes match a single digit, 
word, or space character, respectively.


# # Que 13: What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

# In[ ]:


Answer 13:
The \D, \W, and \S shorthand character classes match a single character that is not a digit, 
word, or space character, respectively.


# # Que 14. What is the difference between .*? and .*?

# In[ ]:


Answer 14:
The .* performs a greedy match, and the .* performs a nongreedy match.


# # Que 15. What is the syntax for matching both numbers and lowercase letters with a character class?

# In[ ]:


Answer 15:
Either [0-9a-z] or [a-z0-9]


# # Que 16: What is the procedure for making a normal expression in regax case insensitive?

# Answer 16:
# Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.

# # Que 17:What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?

# In[ ]:


Answer 17:
The . character normally matches any character except the newline character. 
If re.DOTALL is passed as the second argument to re.compile(), 
then the dot will also match newline characters.


# # Que 18: If numReg = re.compile(r'\d+'), what will numRegex.sub('X', 11 drummers, 10 pipers, five rings, 4hen) return?

# In[ ]:


Answer 18:
'X drummers, X pipers, five rings, Xhen'


# # Que 19:What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

# In[ ]:


Answer 19:
re.VERBOSE allows us to add white space and comments to the string passed to re.compile()


# # Que 20:How would you write a regex that match a number with comma for every three digits? It must match the given following: '42'
# 
# '1,234'
# 
# '6,368,745'
# 
# but not the following:
# 
# '12,34,567' (which has only two digits between the commas)
# 
# '1234' (which lacks commas)

# In[ ]:


Answer 20:
re.compile(r'^\d{1,3}(,\d{3})*$')


# # Que 21:How would you write a regex that matches the full name of someone whose last name is Watanabe?You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# 
# 'Haruto Watanabe'
# 
# 'Alice Watanabe'
# 
# 'Robocop Watanabe'
# 
# but not the following:
# 
# 'haruto Watanabe' (where the first name is not capitalized)
# 
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 
# 'Watanabe' (which has no first name)
# 
# 'Haruto watanabe' (where Watanabe is not capitalized)

# In[ ]:


Answer21:
re.compile(r'[A-Z][a-z]*\sWatanabe')


# In[ ]:


Que 22: How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'

'Bob pets cats.'

'Carol throws baseballs.'

'Alice throws Apples.'

'BOB EATS CATS.'

but not the following:

'Robocop eats apples.'

'ALICE THROWS FOOTBALLS.'

'Carol eats 7 cats.'


# In[ ]:


Answer 21:
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.IGNORANCE)

