# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:08:37 2018

@author: Vincent Papia
"""

# Imported the os package to interact with Windows

import os

# Set my input directory to 'my_dir' which is where I have placed the HOLStep
# dataset, split between training and test sets as provided by the authors

# I modified the script to work for both the test and training sets by 
# altering the 'my_dir' and 'write_file' variables accordingly

# Also set my output directory to a larger, but slower volume for storage

my_dir = "C:\\Users\\Vin\\Desktop\\Masters Degree\\WPI - Data Science\\05 - Big Data Analytics\\Final Project\\holstep\\test\\"
output_dir = "G:\\"

# Initialize the 'useful' string for use in creating a binary indicator
# variable for the eventual dataset

# Also opened up a new file for generating a single file all conjectures in a 
# given directory

useful = ''
write_file = open(output_dir + 'test.txt', 'w')

# A for loop that scans each file in a directory, opens the file, and scans
# it line by line, generating a ;-separated string for each row including 
# Conjecture Name (conj_name), Dependency Name (dep_name), Dependency
# Indicator, the tokenization of the Dependency by calling readline() twice
# for Dependencies and once for Intermediate Proof Steps, and whether the 
# step was useful in the eventual proof of the conjecture or not (useful)

# Write 'string' to 'write_file', re-initilize 'string', then move on to the 
# next file

for filename in os.listdir(my_dir):

    with open(my_dir + filename, "r") as f:
        
        string = ''
        
        for line in f:
                        
            if line[:1] == 'N':
                
                conj_name = line[2:-1]
                
            elif line[:1] == 'D':
                
                dep_name = line[2:-1]
                useful = '1'
                line = f.readline()
                line = f.readline()
                string += (conj_name + ';' + dep_name + ';' + '1' + ';' + 
                           line[2:-1] + ';' + useful + '\n')
            
            elif line[:1] == '+':
                
                useful = '1';
                line = f.readline()
                string += (conj_name + ';' + '' + ';' + '0' + ';' + line[2:-1] + 
                           ';' + useful + '\n')
            
            elif line[:1] == '-':
                
                useful = '0';
                line = f.readline()
                string += (conj_name + ';' + '' + ';' + '0' + ';' + line[2:-1] + 
                           ';' + useful + '\n')
    
            else:
                
                line = f.readline()
    
        write_file.write(string)
    
    f.close()
    
write_file.close()
