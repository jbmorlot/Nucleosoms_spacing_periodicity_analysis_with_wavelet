#!/bin/python
import numpy as np
import sys
from sys import stdout
import numpy as np
import os
import re
import gzip


#----------------------------------------------------
#PARTS TO CHANGE
#----------------------------------------------------


def Operation_on_column(column):
  return (float(column[1])+float(column[2]))/2.	# <--Need to change this line to do another opeartion on column
  
#----------------------------------------------------




#regexp_user = re.compile(r'(chr)|(\n)')		#<-- Replace here all the string you want to remove from the file
							#Warning: All line with a string won't be taken into account

							

print('Precompute Launched!')

#Repertoire dans lequel sont les donnes
directory = os.path.dirname(sys.argv[1])
os.chdir(directory)

#regexp_precompute = re.compile(r'precomputed')
regexpgz = re.compile(r'.gz')
regexp = re.compile(r'[A-Za-z]')


##Launch all files in the repertory
#if int(sys.argv[2]) == 1:
  #print ('List of files: '+ str(os.listdir(directory)))
  
  #for file_name in os.listdir(directory):
    ##We are careful to not compute a file already computed
    #if regexp_precompute.search(file_name) is None:
      #print ('Current file: ' + file_name)

      #file_name_split = file_name.split('.')[0]
      #save_file_name = file_name_split + '_precomputed.wig'
      
      #data_input_1 = []
      
      #sample_count = 0
      
      ##We check if the data are in a .gz file
      #if regexpgz.search(file_name) is not None:
	#with gzip.open(file_name) as f:
	  #for line in f:
	    ##We replace the wanted strings
	    #line = regexp_user.sub("", line)
	    ##We check that we are not computing a string
	    #if regexp.search(line) is None:
	      ##We split the line
	      #line_split = line.split("\t")
	      ##We do an operation with each column
	      #data_input_1.append(Operation_on_column(line_split))
	      ##We print the first line
	      #if sample_count == 0:
		#print "Sample : {0}".format(line_split)
		#print "Operation_result = {0}".format(Operation_on_column(line_split))
		#sample_count = 1
	
      #else:
	#with open(file_name) as f:
	  #for line in f:
	    ##We replace the wanted strings
	    #line = regexp_user.sub("", line)
	    ##We check that we are not computing a string
	    #if regexp.search(line) is None:
	      ##We split the line
	      #line_split = line.split("\t")
	      ##We do an operation with each column
	      #data_input_1.append(Operation_on_column(line_split))
	      ##We print the first line
	      #if sample_count == 0:
		#print "Sample : {0}".format(line_split)
		#print "Operation_result = {0}".format(Operation_on_column(line_split))
		#sample_count = 1

      ##We fill the histogram with this 1 column array
      #print("Filling histogram of Nucleosom position...")
      #data_input = np.asarray(data_input_1,dtype=np.float32)
      #data_length_tot = data_input.shape[0]
      #data_max = np.amax(data_input)
      #data_min = np.amin(data_input)
      #data_range = data_max - data_min
    
      #print "(data_length,data_range,data_max,data_min)={0}".format((data_length_tot,data_range,data_max,data_min))
 

      #histogram = np.zeros(data_range)

      #for i in xrange(data_length_tot):
	#if data_input[i] >= data_min and data_input[i] < data_max: 
	  #histogram[(data_input[i]-data_min)] += 1
	
	#if int(100*float(i+1)/float(data_length_tot))%(10) == 0:
	  #stdout.write("\r %d /100" % int(100*float(i+1)/float(data_length_tot)))
	  #stdout.flush()
      
      #print("Saving...")
      #np.savetxt(save_file_name,histogram,header='(Data_length,data_min,data_max)= {0},{1},{2}'.format(data_range,data_min,data_max))
      #f.close()

#launch One file
#if int(sys.argv[2]) == 0:   

file_name = sys.argv[1]
print ('Current file: ' + file_name)

file_name_split = file_name.split('.')[0]
save_file_name = file_name_split + '_precomputed.wig'

data_input_1 = []

sample_count = 0
not_taken_account = 0

#We check if the data are in a .gz file
if regexpgz.search(file_name) is not None:
  with gzip.open(file_name) as f:
    for line in f:
      line_split = line.split("\t")
      #We check that we are not computing a string
      if regexp.search(line_split[1]) is None and regexp.search(line_split[2]) is None:
	#We do an operation with each column
	data_input_1.append((int(line_split[1])+int(line_split[2]))/2.)	
      else:
	not_taken_account += 1
	
	#We print the first line
	if sample_count == 0:
	  print "Sample : {0}".format(line_split)
	  print "Operation_result = {0}".format((int(line_split[1])+int(line_split[2]))/2.)
	  sample_count = 1
	  
  
else:
  with open(file_name) as f:
    for line in f:
      line_split = line.split("\t")
      #We check that we are not computing a string
      if regexp.search(line_split[1]) is None and regexp.search(line_split[2]) is None:
	#We do an operation with each column
	data_input_1.append((int(line_split[1])+int(line_split[2]))/2.)	
      else:
	not_taken_account += 1
	#We print the first line
	if sample_count == 0:
	  print "Sample : {0}".format(line_split)
	  print "Operation_result = {0}".format((int(line_split[1])+int(line_split[2]))/2.)
	  sample_count = 1
	  

print ("Number of line not taken into account: {0}".format(not_taken_account))

#We fill the histogram with this 1 column array
data_input = np.asarray(data_input_1,dtype=np.float32)
data_length_tot = data_input.shape[0]
data_max = int(np.amax(data_input))
data_min = int(np.amin(data_input))
data_range = data_max - data_min
print "Number of points = {0}".format(data_length_tot)
print '(data_length,data_min,data_max)= {0} , {1} , {2} '.format( data_range ,data_min ,data_max )

histogram = np.zeros(data_range)

print_once = 0

print("Filling histogram of Nucleosom position...")

for i in xrange(data_length_tot):
  if data_input[i] >= data_min and data_input[i] < data_max: 
    histogram[int(data_input[i]-data_min)] += 1
  
  if int(100*float(i+1)/float(data_length_tot))%(10) == 0 and print_once < int(100*float(i+1)/float(data_length_tot)):
    print_once = int(100*float(i+1)/float(data_length_tot))
    stdout.write("\r %d /100" % int(100*float(i+1)/float(data_length_tot)))
    stdout.flush()
    
print("\nSaving...")
np.savetxt(save_file_name,histogram,header='(data_length,data_min,data_max)= {0},{1},{2}'.format(data_range,data_min,data_max))
print("\nDONE!")
    
    

