# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 18:02:39 2018

@author: Vincent Papia
"""

# Set 'my_dir' to location of train.txt and test.txt files that result from
# fileConvertScript.py

my_dir = 'G:\\'

files = ['train.txt', 'test.txt']

# Create and open the master.txt file which contains all training and test
# observations, write the schema to the very first line, then the contents of 
# train.txt and test.txt to master.txt

with open(my_dir + 'master.txt', 'w') as write_file:
    
    write_file.write('conj_name;dep_name;depen_bin;step_token;useful_bin\n')
    
    for file in files:
            
        with open(my_dir + file) as f:
            
            for line in f:
                
                write_file.write(line)