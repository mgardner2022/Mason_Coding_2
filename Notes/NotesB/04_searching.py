# Searching and read/write files

# forward slash goes into a directory. ".." goes "up" a directory.
# by default, open() opens a file to read ('r')
file = open('../resources/super_villians.txt', 'r')
print(file)
file.close()

# open a file with w
# overwrites entire file

# open file to append with 'a'
file = open('../resources/super_villains.txt', 'a')
file.write("Mia the Horrible\n")
file.close()

# Go through the info in the file line by line
file = open('../resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())

file.close()

# .strip() method strips out spaces, tabs, returns etc...
print("Hi\n".strip())
print("     Hello".strip())

# Better way to open files (Syntactic sugar)
with open('../resources/super_villains.txt', 'r') as f:
    for line in f:
        print("Hello", line)


# read data into a list
with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)


# linear search

# python way
print("VARVARA TEMPEST" in villains) # in keyword

# Brute force way
i = 0
key = "VARVARA TEMPEST"

while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < len(villains) - 1:
    print("Found", key, "at position", i)
else:
    print(key, "noy found.")


# make a function
def linear_search(key, list):
    i = 0

    while i < (len(list) - 1) and key.upper() != list[i]:
        i += 1

    if i < len(list) - 1:
        return True
    else:
        return False


print(linear_search("Lavina Nyx", villains))



