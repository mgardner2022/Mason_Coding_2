# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41) if x % 2 == 0]
print(my_list)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(101)]
print(my_list)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_positives = [x for x in my_list if x > 0]
print(my_positives)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
from Problems.number_list import *
# Print the last 5 numbers in num_list
print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))
# Find and print the lowest number in num_list (1pt)
print(min(num_list))
# Find and print the average of num_list (2pts)
my_average = sum(num_list)/len(num_list)
print(my_average)
# Remove the lowest number from num_list (2pt)
num_list.sort()
num_list.pop(0)
print(num_list)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
from collections import Counter
mode = Counter(num_list)
print(mode.most_common(1))  # I had to google this one but I guess I found out about a cool library

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS
# I cant figure out how to do these
# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
for num in num_list:
    if num % 2 == 0:
        del num
    elif num % 3 == 0:
        del num
    elif num % 4 == 0:
        del num
    elif num % 5 == 0:
        del num
    elif num % 6 == 0:
        del num
    elif num % 7 == 0:
        del num
    elif num % 8 == 0:
        del num
    elif num % 9 == 0:
        del num

print(num_list)  # this was my best idea

# Find the number of palindromes
# Hint: This may be easier to do with strings




