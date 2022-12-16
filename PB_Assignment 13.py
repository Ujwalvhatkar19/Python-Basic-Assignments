#!/usr/bin/env python
# coding: utf-8

# # Que 1:What advantages do Excel spreadsheets have over CSV spreadsheets?

# In[ ]:


Answer 1: 
Excel (XLS and XLSX) file formats are better for storing more complex data, 
CSV files are supported by nearly all data upload interfaces.
In a xlsx we can save the formulas, graphs, pivots, etc in the file. 
A CSV is just a flat text file that uses a delimiter to separated the fields.


# # Que 2:What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# In[ ]:


call open() and pass it 'w' to open a file in write mode 
This will create the object you can then pass to csv.writer() to create a Writer object.
For Csv.reader
file = open('file name.csv')
type(file)
csvreader = csv.reader(file)


# # Que 3: What modes do File objects for reader and writer objects need to be opened in?

# In[ ]:


Answer 3:
<r> for reading, <w> for writing, <+> for both reading and writing


# # Que 4: What method takes a list argument and writes it to a CSV file?

# In[ ]:


Answer 4: 
writerow() method of writer and DictWriter class


# # Que 5: What do the keyword arguments delimiter and line terminator do?

# In[ ]:


Answer 5: 
delimeter='\t' and lineterminator='\n\n'


# # Que 6: What function takes a string of JSON data and returns a Python data structure?

# In[ ]:


dict


# # Que 7: What function takes a Python data structure and returns a string of JSON data?

# In[ ]:


Answer 7:
json.dumps() 

