# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:02:30 2023

@author: User
"""

from datetime import datetime
import os
  
def write_file(filename, data):
    if os.path.isfile(filename):
        with open(filename, 'a') as f:          
            f.write('\n' + data)   
    else:
        with open(filename, 'w') as f:                   
            f.write(data)
  
def print_time():   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = "Current Time = " + current_time
    return data
  
write_file('C:/Users/User/Documents/Python/test.txt' , print_time())