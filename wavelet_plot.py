#!/bin/python
import numpy as np
import os
from matplotlib import colors



def wavelet_local_plot(data_min, data_max,histogram_length,period_min,period_max,width_min,width_max,hole_width_min,hole_width_max,plot_var,save_var,save_txt_var,local_width,local_width_hole,map_local_period_convolution,cwt,histogram,histogram_gaussian,sub_directory):
  
  os.chdir(sub_directory)
  
  if(save_txt_var == 1):
      print("Saving Local Plot into Text Files...")
      np.savetxt('Local_width_peak_width_min{0}_width_max{1}_data_min{2}_data_max{3}.txt'.format(width_min,width_max,data_min,data_max),local_width)
      np.savetxt('Local_width_hole_width_min{0}_width_max{1}_data_min{2}_data_max{3}.txt'.format(hole_width_min,hole_width_max,data_min,data_max),local_width_hole)
      np.savetxt('Local_period_period_min{0}_period_max{1}_data_min{2}_data_max{3}.txt'.format(period_min,period_max,data_min,data_max),map_local_period_convolution)
      print("SAVED!\n")
  
  if(save_var == 1 or plot_var == 1):
    print("Ploting Local Signal...")
    
    # make a color map of fixed colors
    cmap = colors.ListedColormap(['white','black'])
    bounds=[0,1,10000]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    cmap_2 = colors.ListedColormap(['white','blue','green','red'])
    bounds_2=[0,0.5,1.5,2.5,3.5]
    norm_2 = colors.BoundaryNorm(bounds_2, cmap_2.N)
    
    if(save_var==1):
      import matplotlib
      matplotlib.use('Agg')
      import matplotlib.pyplot as plt

    if(plot_var==1):
      import matplotlib.pyplot as plt

    fig2 = plt.figure(figsize=(15, 10))
    ax21 = fig2.add_subplot(511)
    ax22 = fig2.add_subplot(512)
    ax23 = fig2.add_subplot(513)
    ax24 = fig2.add_subplot(514)
    ax25 = fig2.add_subplot(515)
    
    ax21.plot(np.linspace(data_min,data_max, histogram_length),local_width_hole,'ro')
    ax21.set_title('Local Width Hole')
    ax21.set_xlabel('Position (bp)')
    ax21.set_ylabel('Width')
    ax21.tick_params(axis='x')
    ax21.tick_params(axis='y')
    ax21.grid()
    ax21.axis('tight')
    ax21.set_ylim([hole_width_min,hole_width_max])

    
    ax22.plot(np.linspace(data_min,data_max, histogram_length),local_width,'ro')
    ax22.set_title('Local Width Peak')
    ax22.set_xlabel('Position (bp)')
    ax22.set_ylabel('Width')
    ax22.tick_params(axis='x')
    ax22.tick_params(axis='y')
    ax22.grid()
    ax22.axis('tight')
    #ax22.set_ylim(bottom = 0)
    ax22.set_ylim([width_min,width_max])

    
    ax23.imshow(map_local_period_convolution,interpolation='nearest',cmap = cmap_2, norm = norm_2,extent=[data_min,data_max,period_min,period_max],aspect='auto')
    ax23.grid(True,color='black')
    ax23.set_title('Local Period')
    ax23.set_xlabel('Position (bp)')
    ax23.set_ylabel('Local Period (bp)')
    ax23.tick_params(axis='x')
    ax23.tick_params(axis='y')

    ax24.imshow(map_local_period_convolution,interpolation = 'nearest', cmap = cmap, norm = norm, extent = [data_min,data_max,period_min,period_max],aspect='auto')
    ax24.imshow(cwt,interpolation='nearest',extent=[data_min,data_max,period_min,period_max],aspect='auto',alpha = 0.85)
    ax24.grid(True,color='black')
    ax24.set_title('Morlet Wavelet Transform')
    ax24.set_xlabel('Position (bp)')
    ax24.set_ylabel('Local Period (bp)')
    ax24.tick_params(axis='x')
    ax24.tick_params(axis='y')

    
    #Normalizing before plotting
    histogram_sum = np.sum(histogram)
    histogram = histogram / histogram_sum
    
    histogram_gaussian_sum = np.sum(histogram_gaussian)
    histogram_gaussian = histogram_gaussian / histogram_gaussian_sum
    
    #ax25.plot(np.linspace(data_min,data_max, histogram_length),histogram,'g')
    ax25.plot(np.linspace(data_min,data_max, histogram_length),histogram_gaussian,'b')
    ax25.set_title('Nucleosom Position Histogram')
    ax25.set_xlim([0,histogram_length])
    ax25.set_xlabel('Position (bp)')
    ax25.set_ylabel('Frequency Normalized')
    ax25.tick_params(axis='x')
    ax25.tick_params(axis='y')
    ax25.grid()
    ax25.axis('tight')


    if(plot_var==1):
      print('Dispaying...')
      fig2.tight_layout()
      plt.show()
      print('PLOTED!\n')

    if(save_var==1):
      fig2.set_tight_layout(fig2)
      print('Saving...')
      
      ax21.set_title('Local Width Hole', fontsize=10)
      ax21.set_xlabel('Position (bp)', fontsize=8)
      ax21.set_ylabel('Width', fontsize=8)
      ax21.tick_params(axis='x', labelsize=8)
      ax21.tick_params(axis='y', labelsize=8)
      
      ax22.set_title('Local Width Peak', fontsize=10)
      ax22.set_xlabel('Position (bp)', fontsize=8)
      ax22.set_ylabel('Width', fontsize=8)
      ax22.tick_params(axis='x', labelsize=8)
      ax22.tick_params(axis='y', labelsize=8)

      ax23.set_title('Local Period', fontsize=10)
      ax23.set_xlabel('Position (bp)', fontsize=8)
      ax23.set_ylabel('Period', fontsize=8)
      ax23.tick_params(axis='x', labelsize=8)
      ax23.tick_params(axis='y', labelsize=8)

      ax24.set_title('Wavelet Convolution', fontsize=10)
      ax24.set_xlabel('Position (bp)', fontsize=8)
      ax24.set_ylabel('Period', fontsize=8)
      ax24.tick_params(axis='x', labelsize=8)
      ax24.tick_params(axis='y', labelsize=8)

      ax25.set_title('Nucleosom Position Histogram', fontsize=10)
      ax25.set_xlabel('Position (bp)', fontsize=8)
      ax25.set_ylabel('Frequency', fontsize=8)
      ax25.tick_params(axis='x', labelsize=8)
      ax25.tick_params(axis='y', labelsize=8)
      
      fig2.savefig('Signal_period_min{0}_period_max{1}_data_min{2}_data_max{3}.pdf'.format(period_min,period_max,data_min,data_max))

      plt.clf()
      print('SAVED!\n')

    plt.close()

def wavelet_histogram_plot(data_min,data_max,period_min,period_max,period_length,width_min,width_max,width_length,hole_width_min,hole_width_max,hole_width_length,plot_var,save_var,save_txt_var,histogram_period_1,histogram_period_2,histogram_period_3,histogram_width,histogram_width_hole,sub_directory):
  
  os.chdir(sub_directory)
  
  if(save_txt_var == 1):
      print("Saving Histograms into Text Files...")
      np.savetxt('Histograms_width_peak_width_min{0}_width_max{1}_data_min{2}_data_max{3}.txt'.format(width_min,width_max,data_min,data_max),histogram_width)
      np.savetxt('Histograms_width_hole_width_min{0}_width_max{1}_data_min{2}_data_max{3}.txt'.format(hole_width_min,hole_width_max,data_min,data_max),histogram_width_hole)
      np.savetxt('Histograms_period_MAX1_period_min{0}_period_max{1}_data_min{2}_data_max{3}.txt'.format(period_min,period_max,data_min,data_max),histogram_period_1)
      np.savetxt('Histograms_period_MAX2_period_min{0}_period_max{1}_data_min{2}_data_max{3}.txt'.format(period_min,period_max,data_min,data_max),histogram_period_2)
      np.savetxt('Histograms_period_MAX3_period_min{0}_period_max{1}_data_min{2}_data_max{3}.txt'.format(period_min,period_max,data_min,data_max),histogram_period_3)
      print("SAVED!\n")
  
  if(save_var==1 or plot_var==1):
    print("Ploting Histograms...")
    if(save_var==1):
      import matplotlib
      matplotlib.use('Agg')
      import matplotlib.pyplot as plt

    if(plot_var==1):
      import matplotlib.pyplot as plt

    fig1 = plt.figure()
    ax11 = fig1.add_subplot(311)
    ax12 = fig1.add_subplot(312)
    ax13 = fig1.add_subplot(313)

    #ax11.plot(np.linspace(period_min,period_max, period_length),histogram_period_3,'b')
    ax11.plot(np.linspace(period_min,period_max, period_length),histogram_period_2,'g')
    ax11.plot(np.linspace(period_min,period_max, period_length),histogram_period_1,'r')
    ax11.set_title('Local period histogram')
    ax11.set_xlabel('Period (bp)')
    ax11.set_ylabel('Frequency')
    ax11.tick_params(axis='x')
    ax11.tick_params(axis='y')
    ax11.grid() 
    ax11.axis('tight')
    ax11.set_xlim([period_min+5,period_max-5])


    ax12.plot(np.linspace(width_min,width_max, width_length),histogram_width)
    ax12.set_title('Local width peak histogram')
    ax12.set_xlabel('Width (bp)')
    ax12.set_ylabel('Frequency')
    ax12.tick_params(axis='x')
    ax12.tick_params(axis='y')
    ax12.grid()
    ax12.axis('tight')
    ax12.set_xlim([width_min+5,width_max-5])

    ax13.plot(np.linspace(hole_width_min,hole_width_max, hole_width_max - hole_width_min),histogram_width_hole)
    ax13.set_title('Local width hole histogram')
    ax13.set_xlabel('Width (bp)')
    ax13.set_ylabel('Frequency')
    ax13.tick_params(axis='x')
    ax13.tick_params(axis='y')
    ax13.grid()
    ax13.axis('tight')
    ax13.set_xlim([hole_width_min+5,hole_width_max-5])
    

    if(plot_var==1):
      print('Dispaying...')
      fig1.tight_layout()
      plt.show()
      print('PLOTED!\n')

    if(save_var==1):
      fig1.set_tight_layout(fig1)
      print('Saving...')

      ax11.set_title('Local period histogram', fontsize=10)
      ax11.set_xlabel('Period (bp)', fontsize=8)
      ax11.set_ylabel('Frequency', fontsize=8)
      ax11.tick_params(axis='x', labelsize=8)
      ax11.tick_params(axis='y', labelsize=8)

      ax12.set_title('Local width peak histogram', fontsize=10)
      ax12.set_xlabel('Width (bp)', fontsize=8)
      ax12.set_ylabel('Frequency', fontsize=8)
      ax12.tick_params(axis='x', labelsize=8)
      ax12.tick_params(axis='y', labelsize=8)
      
      ax13.set_title('Local width hole histogram', fontsize=10)
      ax13.set_xlabel('Width (bp)', fontsize=8)
      ax13.set_ylabel('Frequency', fontsize=8)
      ax13.tick_params(axis='x', labelsize=8)
      ax13.tick_params(axis='y', labelsize=8)
      
      fig1.savefig('Histograms_period_min{0}_period_max{1}_width_peak_min{2}_width_peak_max{3}_width_hole_min{4}_width_hole_max{5}.pdf'.format(period_min,period_max,width_min,width_max,hole_width_min,hole_width_max))

      plt.clf()
      print('SAVED!\n')

    plt.close()