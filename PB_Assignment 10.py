#!/usr/bin/env python
# coding: utf-8

# # Que 1: How do you distinguish between shutil.copy() and shutil.copytree()?
Answer 1:
shutil.copy() will copy only one file
shutil.copytree() will copy entire folder.
# # Que 2: What function is used to rename files??
Answer 2:
to remname the file we can use the os.rename() function. 
# # Que 3:What is the difference between the delete functions in the send2trash and shutil modules?

# In[ ]:


send2trash just send file to recycle bin where shutil functions will permanently delete files and folders. 


# # Que 4:ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

# In[ ]:


Answer 4:
The zipfile.ZipFile() function is equivalent to the open() function; 
the first argument is the filename, and the second argument is the mode to open the 
ZIP file in (read, write, or append).


# # Que 5: Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

# In[ ]:


Answer 5:
import os, shutil
    sourcePath = input(‘Enter the absolute path of the source folder: ‘)
     fileExtType = input(‘Enter the type of file to copy (such as .pdf or .jpg): ‘).lower()
         destPath = input(‘Enter the absolute path of the destination folder: ‘)

for foldername, subfolders, filenames in os.walk(sourcePath):
     for filename in filenames:
             if filename.lower().endswith(fileExtType):
 #print(foldername + ‘\\’ + filename)
 copySourcePath = os.path.join(foldername, filename)
 #print(copySourcePath)
shutil.copy(copySourcePath, destPath)
     else:
         continue

