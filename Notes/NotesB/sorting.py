# Sorting
import random

# swap values
a = 1
b = 2

temp = a
a = b
b = temp

# pythonic way
a, b = b, a  # works in python

my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)

my_list2 = my_list[:]
my_list3 = my_list[:]


for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

print(my_list)


# Insertion Sort

for key_pos in range(1, len(my_list2)):
    key_val = my_list2[key_pos]
    scan_pos = key_pos - 1
    while scan_pos >= 0 and key_val < my_list2[scan_pos]:
        my_list2[scan_pos + 1] = my_list2[scan_pos]
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val

print(my_list2)

my_list3.sort()


# Optional function paramaters
print("Hello", end=" ")
print("World", end="!\n")
print("Hello", "World", sep="Big", end="!!!\n")


def hello(name, tod="morning"):
    print("Hello", name, "good", tod)


hello("Ryan Jaden Surn", "afternoon")
hello("Ryan Jaden Surn")
hello("Ryan Jaden Surn", tod="evening")


# lambda functions
# when you need a function but don't want to make a function
# also called anonymous functions

# lambda parameter: returned
doubleme = lambda x: x * 2
print(doubleme(5))

product = lambda a, b: a * b
print(product(4, 6))


# real world sorting with python
my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)

my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)


# sort method (changes list in place)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_2dlist.sort(key=lambda a: a[0])
print(my_2dlist)
my_2dlist.sort(key=lambda a: a[1])
print(my_2dlist)
my_2dlist.sort(reverse=True, key=lambda a: sum(a))
print(my_2dlist)


# sorted function

new_list = sorted(my_2dlist, reverse=True, key=lambda x: abs(x[0] - x[1]))
print(new_list)












