"""
Data processing assignment
Description: Takes input (unixdatetime and rainfall values) from a local csv file, performs the necessary transaformations on the data and plots it in a interactive time series graph.
~Mansih Patel~
"""
#Imports all the libraries used.
#!!! Please make sure that the matplotlib library is installed before executing. !!!
import csv
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

#Opens and reads the data from the local csv file (accumRainfall.csv).
#Changes may need to be made to the script if other csv files are not consistent with the one provided.
#These changes could be the file name, character encoding, delimiter, etc...
with open("accumRainfall.csv", 'r', encoding = "utf-16") as csvfile:
    rainData = csv.reader(csvfile, delimiter = "\t")
    unix_Date_Time = []
    rain_Fall_Height = []
    for i in rainData:
        unix_Date_Time.append(i[0])
        rain_Fall_Height.append(i[1])
        
#This block will stirp the column titles from both of the lists.
unix_Date_Time = unix_Date_Time[1:]
rain_Fall_Height = rain_Fall_Height[1:]

#Transforms the rainfall strings into floats and then appends them to a new list.
y = []
for height in rain_Fall_Height:
    height = float(height)
    y.append(height)

#Firstly transforms the unixdatetime strings into integers, which are then converted from its epoch format to a readable format (based on UTC timezone).
#Four hours are then subtracted from the converted times as the measurement site is located in Pennsylvania.
#The times are finally appended to a new list.
x = []
for unixdate in unix_Date_Time:
    unixdate = int(unixdate)
    date = datetime.datetime.utcfromtimestamp(unixdate).replace(tzinfo=datetime.timezone.utc)
    date = date - timedelta(hours=4)
    x.append(date)

#Finds the peak rainfall value and calculates a thirty minute period centered around this peak.
max_Y = max(y)
max_X = x[y.index(max_Y)]
min_Period = max_X - timedelta(minutes=15)
max_Period = max_X + timedelta(minutes=15)

#Plots the x and y lists and shades in the peak thity minute period.
plt.plot(x,y)
plt.axvspan(min_Period, max_Period, alpha=0.5, color='red')

#Labels the axes and displays the interactive plot.
plt.xlabel('Time (Year-Month-Day HH-MM-SS)')
plt.ylabel('Rainfall (inches ")')
plt.title("Rainfall over time")
plt.show()
