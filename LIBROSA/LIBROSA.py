#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import modules and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr


# In[2]:


# Set directory for source files
data_dir = 'heartbeat_sounds/set_a'
audio_files = glob(data_dir + '/*.wav')

len(audio_files)


# In[3]:


# Read the first audio files , create the time array (timeline)
audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq
time


# In[5]:


# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time(s)' , ylabel= 'Sound Amplitude')
plt.show()


# In[ ]:


get_ipython().run_cell_magic('time', '', "\n# Perform the reading through all the audio files\nfor file in range(0, len(audio_files), 1):\n\n    # read the first audio files , create the time array (timeline)\n    audio, sfreq = lr.load(audio_files[0])\n    time = np.arange(0, len(audio)) / sfreq\t\n\n    #Plot audio over time\n    fig, ax = plt.subplots()\n    ax.plot(time, audio)\n    ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')\n    plt.show()")


# In[ ]:




