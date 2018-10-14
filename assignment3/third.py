import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Calculating mean
def mean(arr):
	sum= np.sum(arr)
	mean= sum/arr.shape[0]
	return mean

#Calculating standard deviation
def std_dev(arr):
	var=  np.sum(np.subtract(arr, mean(arr))**2, axis=0)/(arr.shape[0]-1)
	std_dev= np.sqrt(var)
	return std_dev

#Calculating covariance
def correlation(arr1, arr2):
	diff1= np.subtract(arr1, mean(arr1))
	diff2= np.subtract(arr2, mean(arr2))
	d= np.dot(diff2, diff1)
	covar= d/(arr1.shape[0]-1)
	return covar

# Variable names:
# unemp_data-> Dataframe corresponding to unemployementrate.csv
# crime_data-> Dataframe corresponding to crimerate.csv
#crime_data1-> Dataframe containing crime rates of All STates
#crime_data2-> Dataframe containing crime rates of All UTs
#crime_data_-> Dataframe containing the concatenation of crime_data1 and crime_data2
#u-> Dataframe of unemployement rates converted to numpy array
#c-> Dataframe of crime rates converted to numpy array

#reading data from csv files
unemp_data= pd.read_csv('unemploymentrate.csv')
crime_data= pd.read_csv('crimerate.csv')

unemp_data= unemp_data.iloc[0:36] # to ignore the last entry in the csv file corresponding to all India
crime_data1= crime_data.iloc[0:29] # to ignore  the 29th entry in the csv file corresponding to all States
crime_data2= crime_data.iloc[30:37] # data in the csv file corresponding to all UTs
frames= [crime_data1, crime_data2] 
result= pd.concat(frames) #concatenating the two data frames
crime_data_= result.reset_index() #resetting index number 30 to 29 as we had skipped one index by ignoring All states data in the crimerate.csv
unemp_data=unemp_data.sort_values(by='State/UTs', ascending='True') #Sorting states/UTs alphabetically
crime_data_=crime_data_.sort_values(by='State/UT (Col.3)', ascending='True') #Sorting states/UTs alphabetically

u=unemp_data['2015-16'].values  #Converting dataframe into numpy array
c=crime_data_['Rate of Cognizable Crimes (IPC) (2016)++ (Col.10)'].values #Converting dataframe into numpy array

mean_u= mean(u)
mean_c= mean(c)
std_dev_u= std_dev(u)
std_dev_c= std_dev(c)

corr=correlation(u,c)
print(corr)
coeff= np.sqrt(corr)/(std_dev_u*std_dev_c)
print(coeff)
#Plotting histograms of unemployement rates
bins=np.linspace(u.min(),u.max(),num=21)
x_ticks=np.union1d(bins[0::2],[1.000])
plt.hist(u, bins=bins,ec='black',zorder=2,alpha=0.9)
plt.xticks(x_ticks)
plt.yticks(np.arange(0,10,1))
plt.ylim(0,15)
#line and label for mean
plt.vlines(x=mean_u,ymin=0,ymax=130,zorder=3)
plt.text(mean_u,13,'Mean='+str(round(mean_u,3)),ha='center')
#lines to mark standard deviation
plt.vlines(x=mean_u-std_dev_u,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)
plt.vlines(x=mean_u+std_dev_u,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)
#adding a grid for clarity, zorder orders the various plots from the background upwards
plt.grid(axis='y',zorder=0,ls='-.')
#adding the horizontal lines for standard deviation on each side and labelling them
plt.annotate(s='',xy=(mean_u-std_dev_u,9),xytext=(mean_u, 9),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.annotate(s='',xy=(mean_u+std_dev_u,9),xytext=(mean_u,9),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.text(mean_u,10,'Standard Deviation='+str(round(std_dev_u,2)),ha='center')
plt.xlabel('Unemployement rate (in percentage)')

#Plotting histograms of crime rates
bins=np.linspace(c.min(),c.max(),num=21)
x_ticks=np.union1d(bins[0::2],[1.000])
plt.hist(c, bins=bins,ec='black',zorder=2,alpha=0.9)
plt.xticks(x_ticks)
plt.yticks(np.arange(0,10,1))
plt.ylim(0,15)
#line and label for mean
plt.vlines(x=mean_c,ymin=0,ymax=130,zorder=3)
plt.text(mean_c,13,'Mean='+str(round(mean_c,3)),ha='center')
#lines to mark standard deviation
plt.vlines(x=mean_c-std_dev_c,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)
plt.vlines(x=mean_c+std_dev_c,ymin=0,ymax=120,linestyle='dotted', color='green', alpha=0.8,zorder=3)
#adding a grid for clarity, zorder orders the various plots from the background upwards
plt.grid(axis='y',zorder=0,ls='-.')
#adding the horizontal lines for standard deviation on each side and labelling them
plt.annotate(s='',xy=(mean_c-std_dev_c,9),xytext=(mean_c, 9),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.annotate(s='',xy=(mean_c+std_dev_c,9),xytext=(mean_c,9),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.text(mean_c,10,'Standard Deviation='+str(round(std_dev_c,2)),ha='center')
plt.xlabel('Crime rate (per 1,00,000)')

#Plotting the 2D histogram
plt.hist2d(u,c, bins=40)
plt.xlabel('Unemployement rate (in percentage)')
plt.ylabel('Crime rate (per 1,00,000)')

#Plotting the scatter plot
plt.scatter(u,c)
plt.xlabel('Unemployement rate (in percentage)')
plt.ylabel('Crime rate (per 1,00,000)')

plt.show()
