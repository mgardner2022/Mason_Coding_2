'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''
import csv
import matplotlib.pyplot as plt

with open("CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)

dataten = (data[-11:])

trainten = []
for item in dataten:
    trainten.append(item[3])
print(trainten)

years = []
for item in dataten:
    years.append(item[0])

plt.figure(1, tight_layout=True)


plt.plot(years, trainten)





plt.show()


