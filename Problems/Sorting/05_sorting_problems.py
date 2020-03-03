'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import data


#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)

poppedoff = data.pop(0)
print(poppedoff)

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

topscores = sorted(data, key=lambda a: a[-1])
scorereslist = []
for item in topscores:
    namepoint = [item[1], item[2], item[-1]]
    scorereslist.append(namepoint)

print(scorereslist[-10:])
#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
kobes = []
for item in data:
    if item[2].upper() == "KOBE BRYANT":
        kobes.append(item)
    else:
        pass

totpts = []
for item in kobes:
    pts = item[-1]
    totpts.append(pts)

print("Kobe scored a total of:", sum(totpts), "points.")

#4  What player has the most 3point field goals in a single season. (3pts)
# item 34

topthrees = sorted(data, key=lambda a: a[34])
threelist = []
for item in topthrees:
    threenames = [item[1], item[2], item[34]]
    threelist.append(threenames)

print(threelist[-1])
#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
topws = sorted(data, key=lambda a: a[25])
wslist = []
for item in topws:
    wsnames = [item[1], item[2], item[25]]
    wslist.append(wsnames)

print(wslist[-1])
#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
# WHo has the highest average of their 3p%, 2p% and FT%?
toptot = sorted(data, key=lambda a: (a[36] + a[39] + a[43]) / 3)
totlist = []
for item in toptot:
    totnames = [item[1], item[2], (item[36] + item[39] + item[43]) / 3]
    totlist.append(totnames)

print(totlist[-1])
#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
toppts = sorted(data, key=lambda a: a[-1])

top100 = toppts[-100:]

freepts = sorted(top100, key=lambda a: a[43])
freelist = []
for item in freepts:
    namefree = [item[1], item[2], item[43]]
    freelist.append(namefree)

print("The best FT% was:", freelist[-1])
print("The worst FT% was", freelist[0])










