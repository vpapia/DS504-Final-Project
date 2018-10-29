# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:14:26 2018

@author: Vincent Papia
"""

# Import os and re packages to interact with the OS and use regular
# expression functions, respectively
import os
import re

# Set input and output directories and open write_file to write results
my_dir = "C:\\Users\\Vin\\Desktop\\Masters Degree\\WPI - Data Science\\05 - Big Data Analytics\\Final Project\\Documentation\\Spark Results\\3dresults\\"

output_dir = "G:\\"

write_file = open(output_dir + "spark_3d_results.txt", 'w')

# Scan through Spark result files, searching for ordered pairs (principal 
# components) within square brackets, and usefulness classification label to 
# write to write_file
for filename in os.listdir(my_dir):
    
    with open(my_dir + filename, 'r') as f:
        
        string = ''
        
        for line in f:
            
            string += str(re.search('\[(.*?)\]', line).group(1)) + ',' + str(line.split("useful_bin=")[1][0]) + '\n'
            
        write_file.write(string)
        
write_file.close()