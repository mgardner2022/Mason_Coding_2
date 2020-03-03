# Formatting Numbers

import random

# round function round(n, digits)
print(round(3.1415926535, 2))


# format mehtod (string method)
a = 3814014719784
b = 1374123847123470
print("My number is {}".format(a))
print("My number is {:.3f}".format(b))
print("My numbers are {} and {}".format(a, b))
print("My numbers are {0} and {1}".format(a, b))  # reverse order
print("My numbers are {:,} and {:,}".format(a, b))

# fixed width
for i in range(20):
    c = random.randrange(10000)
    print("${:4}".format(c))

# justification ^ center <left >right and commas
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:<12,}".format(c))

# precision (f float, d dec/int, b binary
for i in range(20):
    c = random.randrange(10000)
    print("{:b}".format(c))

# scientific notation
for i in range(20):
    c = random.random()
    print("{:.2e}".format(c))






