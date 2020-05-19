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

busten = []
for item in dataten:
    busten.append(item[1])

totten = []
for item in dataten:
    totten.append(item[1] + item[3])

trainten = [int(x) for x in trainten]
busten = [int(x) for x in busten]
totten = [int(x) for x in totten]


years = []
for item in dataten:
    years.append(item[0])

plt.figure(1, tight_layout=True, figsize=(15, 7.5))

plt.plot(years, trainten, color="Red", Label="Rail Passengers")
plt.plot(years, busten, color="Blue", Label="Bus Passengers")
plt.plot(years, totten, color="Green", Label="Total Passengers")
plt.xlabel("Years")
plt.ylabel("Passengers")
plt.legend(fancybox="True", shadow="True")



plt.show()

# I think that all of the passengers drop over time because people have become more inclined ot individually transit to
# work, wether that be through walking, biking or driving. I think that the rail passengers initially rise because rail
# transit is often quicker then bus. Bus transit starts off huge because buses are so convenient.

