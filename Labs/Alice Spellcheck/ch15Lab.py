'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('dictionary.txt') as f:
    dictionary_list = [x.strip().upper() for x in f]

alice200 = open("AliceInWonderLand200.txt")

print("---LINEAR SEARCH---")
line_num = 0
for line in alice200:
    line_num += 1
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        if word.upper() == word.upper() in dictionary_list:
            break
        else:
            print(word, "not found in line:", line_num)
alice200.close()


print("---BINARY SEARCH---")
word_list = []
line_num = 0

found = False
middle_pos = 0

with open('AliceInWonderLand.txt') as f:
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        line_num += 1
        for word in words:
            found = False
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            while lower_bound <= upper_bound and not found:
                middle_pos = (upper_bound + lower_bound) // 2
                if dictionary_list[middle_pos] < word:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print(word, "not found at line number", line_num)
            else:
                pass


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
'''
with open('AliceInWonderLand.txt') as f:
    glass_list = [x.strip().upper() for x in f]
    for word in glass_list:
        split_line(word)

found = False
middle_pos = 0

with open('AliceThroughTheLookingGlass.txt') as f:
    for line in f:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            found = False
            lower_bound = 0
            upper_bound = len(glass_list) - 1
            while lower_bound <= upper_bound and not found:
                middle_pos = (upper_bound + lower_bound) // 2
                if glass_list[middle_pos] < word:
                    lower_bound = middle_pos + 1
                elif glass_list[middle_pos] > word:
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print(word, "not found")
            else:
                pass
'''
