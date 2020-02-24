'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re
from collections import Counter

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
file = open('dictionary.txt', 'r')
length = 0
big_man = 0
for word in file:
    if len(word) >= length:
        length = len(word)
        big_man = word

print(big_man)

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
alfile = open('AliceInWonderLand.txt', 'r')
totalwords = 0
avg = 0
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        totalwords += 1
        avg += len(word)

print(totalwords)
print(avg / totalwords)


# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alfile = open('AliceInWonderLand.txt', 'r')
alices = 0
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word == "alice".upper():
            alices += 1
print(alices)

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
alfile = open('AliceInWonderLand.txt', 'r')
sevens = []
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if len(word) == 7:
            sevens.append(word)


def most_common(List):
    times = Counter(List)
    return times.most_common(1)[0][0]


print(most_common(sevens))

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
alfile = open('AliceInWonderLand.txt', 'r')
cheshires = 0
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word == "cheshire".upper():
            cheshires += 1
print(cheshires)
# How many times does "Cat" occur?
alfile = open('AliceInWonderLand.txt', 'r')
cats = 0
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word == "cat".upper():
            cats += 1
print(cats)
# How many times does "Cheshire" immediately followed by "Cat" occur?
alfile = open('AliceInWonderLand.txt', 'r')
ccs = 0
wordrn = 0
allist = []
for line in alfile:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        allist.append(word)
        wordrn += 1
        if allist[wordrn - 2] == "cheshire".upper():
            if allist[wordrn - 1] == "cat".upper():
                ccs += 1

print(ccs)





