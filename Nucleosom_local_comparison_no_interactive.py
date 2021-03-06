#!/bin/python

import numpy as np
import os
import re
import sys

from local_comparison import *



data_file_1 = sys.argv[1]
data_file_2 = sys.argv[2]
name_data_1 = sys.argv[3]
name_data_2 = sys.argv[4]
data_min = int(sys.argv[5])
data_max = int(sys.argv[6])
save_txt_var = int(sys.argv[7])
local_signal_var = int(sys.argv[8])
global_signal_var = int(sys.argv[9])
reverse_var = int(sys.argv[10])

print('\n------------------ Data file -----------------------\n')

#Repertoire dans lequel sont les donnes
directory = os.path.dirname(data_file_2)
  
#Creating new directory and executing the program in it if saving
filename_1 = os.path.split(data_file_1)[1]
filename_2 = os.path.split(data_file_2)[1]

print ('Data File 1: '+ filename_1 +'\nData File 2: '+ filename_2)
filename_split_1 = filename_1.split('.')[0]
filename_split_2 = filename_2.split('.')[0]
sub_directory = directory +'/'+ filename_split_1 + '_' + filename_split_2

if not os.path.exists(sub_directory):
  os.mkdir(sub_directory)
  
#Changing Current directory
os.chdir(sub_directory)

print ( 'Directory Path: ' + directory )
print('\n-----------------------------------------------------\n')

nucleosom_match_pieces(data_file_1,data_file_2,name_data_1,name_data_2,data_min,data_max,save_txt_var,local_signal_var,global_signal_var,reverse_var,sub_directory)

print ('Analysis Finished !')
