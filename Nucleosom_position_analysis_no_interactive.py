#!/bin/python

import numpy as np
import os
import re
import sys

from wavelet import *
from wavelet_plot import *
from input_file_analysis import *
from restart import *



data_file = sys.argv[1]
launch_all = int(sys.argv[2])
data_min = int(sys.argv[3])
data_max = int(sys.argv[4])
period_min = int(sys.argv[5])
period_max = int(sys.argv[6])
width_min = int(sys.argv[7])
width_max = int(sys.argv[8])
hole_width_min = int(sys.argv[9])
hole_width_max = int(sys.argv[10])
bin_period = int(sys.argv[11])
plot = int(sys.argv[12])
save = int(sys.argv[13])
save_txt_var = int(sys.argv[14])
local_var = int(sys.argv[15])
global_var = int(sys.argv[16])
restart_var = int(sys.argv[17])




print('\n------------------ Data file -----------------------\n')



#In case we want to restart the program to the last checkpoint
if restart_var == 1:
  file_input = load_restart_input(data_file)
  
  launch_all = int(file_input[0])
  data_min = int(file_input[1])
  data_max = int(file_input[2])
  period_min = int(file_input[3])
  period_max = int(file_input[4])
  width_min = int(file_input[5])
  width_max = int(file_input[6])
  hole_width_min = int(file_input[7])
  hole_width_max = int(file_input[8])
  bin_period = int(file_input[9])
  plot = int(file_input[10])
  save = int(file_input[11])
  save_txt_var = int(file_input[12])
  local_var = int(file_input[13])
  global_var = int(file_input[14])
  
  
  #Load Histograms
  period_length = int((period_max - period_min)/bin_period)
  width_length = int(width_max - width_min)
  hole_width_length = int(hole_width_max - hole_width_min)
  
  histogram_period_1 = np.zeros(period_length)
  histogram_period_2 = np.zeros(period_length)
  histogram_period_3 = np.zeros(period_length)
  histogram_width = np.zeros(width_length)
  histogram_width_hole = np.zeros(hole_width_length)
  
  histogram_period_1,histogram_period_2,histogram_period_3,histogram_width,histogram_width_hole = load_restart_histograms(data_file)
  
if restart_var == 0:
  #We set the histogram to zero per default
  period_length = int((period_max - period_min)/bin_period)
  width_length = int(width_max - width_min)
  
  histogram_period_1 = np.zeros(period_length)
  histogram_period_2 = np.zeros(period_length)
  histogram_period_3 = np.zeros(period_length)
  histogram_width = np.zeros(width_length)
  histogram_width_hole = np.zeros(width_length)
  
#Repertoire dans lequel sont les donnes
directory = os.path.dirname(data_file)
  
if int(launch_all) == 0:
  
  #Creating new directory and executing the program in it if saving
  filename = os.path.split(data_file)[1]
  print ('Data File: '+ filename)
  filename_split = filename.split('.')[0]
  sub_directory = directory +'/'+ filename_split
  
  if not os.path.exists(sub_directory) and save == 1:
    os.mkdir(sub_directory)
    #Changing Current directory
  os.chdir(sub_directory)
  
  print ( 'Directory Path: ' + directory )
  print('\n-----------------------------------------------------\n')
  
  wavelet_analysis_pieces(data_file,launch_all,data_min,data_max,period_min,period_max,width_min,width_max,hole_width_min,hole_width_max,bin_period,plot,save,save_txt_var,local_var,global_var,restart_var,histogram_period_1,histogram_period_2,histogram_period_3,histogram_width,sub_directory)

if int(launch_all) == 1:
  
  for filename in os.listdir(directory):
    
    regexp = re.compile(r'.wig')
    if regexp.search(filename) is not None:
      print ('Data File: '+ filename)
      
      #Creating new directory and executing the program in it if saving
      filename_split = filename.split('.')[0]
      sub_directory = directory +'/'+ filename_split
      if not os.path.exists(sub_directory) and save == 1:
	os.mkdir(sub_directory)
	#Changing Current directory
      os.chdir(sub_directory)
	
      print ( 'Directory Path: ' + directory )
      print('\n-----------------------------------------------------\n')
      
      #The analysis need the absolute path in order to open data file
      filename_absolute_path = directory + '/'+ filename
    
      wavelet_analysis_pieces(filename_absolute_path,launch_all,data_min,data_max,period_min,period_max,width_min,width_max,hole_width_min,hole_width_max,bin_period,plot,save,save_txt_var,local_var,global_var,restart_var,histogram_period_1,histogram_period_2,histogram_period_3,histogram_width,sub_directory)
	  
    else:
      print (filename + ' : Not taken into account')  
      
print ('Analysis Finished !')
