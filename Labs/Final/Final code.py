import csv
import matplotlib.pyplot as plt

topgamesna = []
topgameseu = []
topgamesjp =[]
salesna = []
saleseu = []
salesjp = []
pos = [1, 2, 3, 4, 5]

with open("vgsalesGlobale.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

basedataeu = data
basedatajp = data

headers = data.pop(0)

data.sort(key=lambda x: float(x[6]), reverse=True)
print(data)
datana = [float(x[6]) for x in data]
print(datana)
nameslistna = [x[1] for x in data]
print(nameslistna)

for i in range(5):
    newnames = nameslistna.pop(0)
    newdata = datana.pop(0)
    salesna.append(newdata)
    topgamesna.append(newnames)

plt.figure(1)

plt.bar(pos, salesna, color='cyan')
plt.xticks(pos[0:], topgamesna, fontsize='5')
plt.title("Top 5 highest selling video games in north america")
plt.xlabel('Titles')
plt.ylabel('Sales in millions')
plt.show()

basedataeu.sort(key=lambda x: float(x[7]), reverse=True)
dataeu = [float(x[7]) for x in basedataeu]
nameslisteu = [x[1] for x in basedataeu]

for i in range(5):
    newnameseu = nameslisteu.pop(0)
    newdataeu = dataeu.pop(0)
    saleseu.append(newdataeu)
    topgameseu.append(newnameseu)

plt.figure(2)

plt.bar(pos, saleseu, color='green')
plt.xticks(pos[0:], topgameseu, fontsize='4.5')
plt.title("Top 5 highest selling video games in Europe")
plt.xlabel('Titles')
plt.ylabel('Sales in millions')
plt.show()

basedatajp.sort(key=lambda x: float(x[8]), reverse=True)
datajp = [float(x[8]) for x in basedatajp]
nameslistjp = [x[1] for x in basedatajp]

for i in range(5):
    newnamesjp = nameslistjp.pop(0)
    newdatajp = datajp.pop(0)
    salesjp.append(newdatajp)
    topgamesjp.append(newnamesjp)

plt.figure(3)

plt.bar(pos, salesjp, color='Red')
plt.xticks(pos[0:], topgamesjp, fontsize='4.3')
plt.title("Top 5 highest selling video games in Japan")
plt.xlabel('Titles')
plt.ylabel('Sales in millions')
plt.show()

