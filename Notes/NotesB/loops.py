# Basic for loop
for i in range(5, 51, 5):
    print(i, end="  ")

# Range function (alternative for comprehension)
my_list = [x for x in range(1, 101)]
print(my_list)

my_list = list(range(1, 101))
print(my_list)

# Breaks
for number in my_list:
    print(number)
    if number > 10:
        break  # forces out of nearest loop

# continue
for number in my_list:
    if number % 7 == 0:
        continue  # skips the rest of this iteration
    print(number)

# For else
for number in my_list:
    if number == 80:
        print("You unaturally finished the loop")
        break
    print(number)
else:
    print("You naturally finished the loop")

# Grabbing a random word from a list
import random
my_list = ["Apple", "Banana", "Cherry", "Dragonfruit"]
my_word = my_list.pop(random.randrange(len(my_list)))
print(my_word, my_list)

random.shuffle(my_list)
my_word = my_list.pop()
print(my_word, my_list)





