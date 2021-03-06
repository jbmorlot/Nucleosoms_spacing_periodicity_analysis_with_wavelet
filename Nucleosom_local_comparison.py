#!/bin/python

import Tkinter as tk
import tkFileDialog
import numpy as np
import os
import re


from local_comparison import *

  
class Window(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.master.title("Nucleosom Analysis")
    self.master.columnconfigure(0, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    self.grid(sticky="NSEW")
    self.createWidgets()
    

  def createWidgets(self):
    #creation des objets variables
    self.data_file_1_var = tk.StringVar()
    self.data_file_1_var.set("")
    self.data_file_2_var = tk.StringVar()
    self.data_file_2_var.set("")
    
    self.name_data_1_var = tk.StringVar()
    self.name_data_1_var.set("")
    self.name_data_2_var = tk.StringVar()
    self.name_data_2_var.set("")
    
    self.data_min_var = tk.StringVar()
    self.data_min_var.set("0")
    
    self.data_max_var = tk.StringVar()
    self.data_max_var.set("0")
    
    self.save_txt_var = tk.StringVar()
    self.reverse_var = tk.StringVar()
    self.local_signal_var = tk.StringVar()
    self.global_signal_var = tk.StringVar()
    
    
    #creation des widgets
    mainFrame = tk.Frame(self, borderwidth=2, relief="groove")
    
    name_data_1_label = tk.Label(mainFrame, text="Name of the Data File 1")
    name_data_2_label = tk.Label(mainFrame, text="Name of the Data File 2")
    data_min_label = tk.Label(mainFrame, text="Data Min (in bp)\n(if 0->min) ")
    data_max_label = tk.Label(mainFrame, text="Data Max (in bp)\n(if 0->max) ")
    save_txt_label = tk.Label(mainFrame, text="Save data into text files")
    reverse_label = tk.Label(mainFrame, text="Analyse the histogram Backward (time x2)")
    local_label = tk.Label(mainFrame, text="Local Analysis") 
    global_label = tk.Label(mainFrame, text="Global Analysis") 
    
    data_file_1_entry = tk.Button(mainFrame, text='Data File 1', command=self.askopenfilename_1)
    data_file_2_entry = tk.Button(mainFrame, text='Data File 2', command=self.askopenfilename_2)
    name_data_1_entry = tk.Entry(mainFrame, textvariable=self.name_data_1_var)
    name_data_2_entry = tk.Entry(mainFrame, textvariable=self.name_data_2_var)
    data_min_entry = tk.Entry(mainFrame, textvariable=self.data_min_var)
    data_max_entry = tk.Entry(mainFrame, textvariable=self.data_max_var)
    
    save_txt_checkbutton = tk.Checkbutton(mainFrame, text=" ",variable = self.save_txt_var)
    reverse_checkbutton = tk.Checkbutton(mainFrame, text=" ",variable = self.reverse_var)
    local_checkbutton = tk.Checkbutton(mainFrame, text=" ",variable = self.local_signal_var)
    global_checkbutton = tk.Checkbutton(mainFrame,text=" ",variable = self.global_signal_var)
    
    button = tk.Button(mainFrame, text="Launch", command=self.action)
    
    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '.wig'
    options['filetypes'] = [('all files', '.*'), ('wig files', '.wig')]    

    #position des widgets
    mainFrame.grid(column=0, columnspan=2, row=0, sticky="NSEW")
    
    data_file_1_entry.grid(column=0,row=1, sticky="EW")
    data_file_2_entry.grid(column=1,row=1, sticky="EW")
    
    name_data_1_label.grid(column=0, row=2, sticky="EW")
    name_data_1_entry.grid(column=1, row=2, sticky="EW")
    
    name_data_2_label.grid(column=0, row=3, sticky="EW")
    name_data_2_entry.grid(column=1, row=3, sticky="EW")
    
    data_min_label.grid(column=0, row=4, sticky="EW")
    data_min_entry.grid(column=1, row=4, sticky="EW")
    
    data_max_label.grid(column=0, row=5, sticky="EW")
    data_max_entry.grid(column=1, row=5, sticky="EW")
    
    save_txt_label.grid(column=0, row=6, sticky="EW")
    save_txt_checkbutton.grid(column=1, row=6, sticky="EW")
    
    reverse_label.grid(column=0, row=7, sticky="EW")
    reverse_checkbutton.grid(column=1, row=7, sticky="EW")
    
    local_label.grid(column=0, row=8, sticky="EW")
    local_checkbutton.grid(column=1, row=8, sticky="EW")
    
    global_label.grid(column=0, row=9, sticky="EW")
    global_checkbutton.grid(column=1, row=9, sticky="EW")
    
    button.grid(column=0,columnspan=2, row=10, sticky="NSEW")
    
  def action(self):
    data_file_1 = self.data_file_1_var.get()
    data_file_2 = self.data_file_2_var.get()
    name_data_1 = self.name_data_1_var.get()
    name_data_2 = self.name_data_2_var.get()
    data_min = int(self.data_min_var.get())
    data_max = int(self.data_max_var.get())
    save_txt = int(self.save_txt_var.get())
    local_signal = int(self.local_signal_var.get())
    global_signal = int(self.global_signal_var.get())
    reverse = int(self.reverse_var.get())

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

    nucleosom_match_pieces(data_file_1,data_file_2,name_data_1,name_data_2,data_min,data_max,save_txt,local_signal,global_signal,reverse,sub_directory)

    print ('Analysis Finished !')
    

  #Browser for input data file
  def askopenfilename_1(self):
    filename = tkFileDialog.askopenfilename(**self.file_opt)
    self.data_file_1_var.set(filename)
  
  def askopenfilename_2(self):
    filename = tkFileDialog.askopenfilename(**self.file_opt)
    self.data_file_2_var.set(filename)
    
    
    
if __name__ =='__main__':
  Window().mainloop()
   
