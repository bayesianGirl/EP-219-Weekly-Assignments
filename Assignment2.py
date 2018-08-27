import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#we define functions to find the mean and variance of the given data
def mean(array):
    array_mean=0
    for i in array:
        array_mean+=i/array.size
    
    return array_mean

def variance(array):
    var_sum=0
    array_mean=mean(array)
    for i in array:
        var_sum+=(i-array_mean)**2
    
    return var_sum/(array.size-1)

#import the data from the excel file into a pandas dataframe
data_frame=pd.read_excel('swachhbharat.xlsx')
#we define a numpy array to store the values stored in data_frame
data=data_frame.values

#this is the total number of blocks in India
n_blocks=np.arange(0,data.shape[0],1)

#we take only the data corresponding to Uttar Pradesh
up_data=[]
for i in n_blocks:
    if data[i][0]=='Uttar Pradesh':
        up_data=np.append(up_data,[data[i][5]/data[i][4]])

#Now, we find the mean, variance and standard deviation
up_mean=mean(up_data)
up_variance=variance(up_data)
up_std=variance(up_data)**0.5

#we move on to plotting the histogram
bins=np.linspace(up_data.min(),up_data.max(),num=21)
x_ticks=np.union1d(bins[0::2],[1.000])

plt.hist(up_data,bins=bins,ec='black',zorder=2,alpha=0.9)

plt.xticks(x_ticks)
plt.yticks(np.arange(0,120,10))

#line and label for mean
plt.vlines(x=up_mean,ymin=0,ymax=130,zorder=3)
plt.text(up_mean,131,'Mean='+str(round(up_mean,3)),ha='center')

#lines to mark standard deviation
plt.vlines(x=up_mean+up_std,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)
plt.vlines(x=up_mean-up_std,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)

#adding a grid for clarity, zorder orders the various plots from the background upwards
plt.grid(axis='y',zorder=0,ls='-.')

#adding the horizontal lines for standard deviation on each side and labelling them
plt.annotate(s='',xy=(up_mean-up_std,120),xytext=(up_mean,120),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.annotate(s='',xy=(up_mean+up_std,120),xytext=(up_mean,120),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.text(up_mean-up_std/2,121,'Standard Deviation='+str(round(up_std,3)),ha='center')
plt.text(up_mean+up_std/2,121,'Standard Deviation='+str(round(up_std,3)),ha='center')

#we are now ready to display the plot
plt.show()


