# list
import random
my_names = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo"]
my_numbers = [5, 9, 12, 6, -3, 6]

# Indexing lists
print(my_names)
print(my_names[2])
print(my_names[-1])
print(my_names[:3])
print(my_names[3:5])
print(my_names[:])

# Copying lists
my_copy = my_names
my_copy.append("Gus")
print(my_copy)
print(my_names)
my_copy = my_names[:]
my_copy.append("Hal")
print(my_copy)
print(my_names)

# 2d list
my_2d = [["PB", "J"], [8, "Hello"], ["Spam", "Eggs"]]
print(my_2d[1])
print(my_2d[1][1])
my_2d[1].append("Bye")
print(my_2d)

# if in
if "Gus" in my_names:
    print("Gus is in my_names")

# List Functions
print(len(my_names))
print(min(my_numbers))
print(max(my_numbers))
print(sum(my_numbers))

print(min(my_names))

# List Methods
print(my_names.index("Cam"))
my_names.append("Cam")
print(my_names.index("Cam"))
print(my_names.count("Cam"))

my_names.append("Deb")
print(my_names)
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)

# Modifying lists
del my_names[6]
print(my_names)

my_names.append("Ryder")
print(my_names)

end_of_list = my_names.pop()
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0)
print(front_of_list)
print(my_names)

# concatenation
first = "Francis"
last = "Parker"
print(first + last)

print(my_names + my_numbers)

my_nums = []
for i in range(10):
    my_nums.append(i)

print(my_nums)

# for each only makes a copy
for num in my_nums:
    num += 1
    print(num)

print(my_nums)

# add one to every item in a list
for i in range(len(my_nums)):
    my_nums[i] += 1

print(my_nums)


my_nums = [x for x in range(10)]
print(my_nums)


# LIST COMPREHENSION
my_list = []
for i in range(100):
    my_list.append(i)

print(my_list)

# using list comprehension
my_list = [x for x in range(101)]  # [output for item in loop]
print(my_list)

# make a list 0 to 100 squared

my_squares = [x ** 2 for x in range(101)]
print(my_squares)

# make a list of 0 to 100 sqaured but filter out odd numbers
my_list = []

for i in range(101):
    if (i ** 2) % 2 == 0:
        my_list.append(i ** 2)

print(my_list)

# list comprehension way

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]
print(my_list)


# roll a single die 100 times and add it to a list

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)  # Hweenk


# roll two die and add them to a list

my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)

# go back through list and make a new list of sums of two die
my_sums = [sum(x) for x in my_list]
print(my_sums)


# make a list from the 100 rolls that shows only the doubles
my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)


# all at once
# roll 100 pairs and only put in doubles

my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]
print(my_list)


# working with strings a lot like lists
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

for letter in first:
    print(letter)

if "N" in first:
    print("YES")




