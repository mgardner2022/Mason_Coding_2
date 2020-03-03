# Exceptions (use sparingly)

# Exception - a condition that results in abnormal program flow

x = 2
y = 0

# Divide by 0 error
try:
    print(x / y)
except:
    print("Infinity")


# conversion error
try:
    int("T")
except:
    print("Number was not vaild")


# handle with a loop
done = False

while not done:
    try:
        user_input = int(input("Enter an integer: "))
        done = True
    except:
        print("Number is not valid")


# file opening (IOError, FileNOtFoundError)
try:
    file = open("AliceInWonderland.txt")
except:
    print("Could not open file")


# Use built in error types for python to check what error occurred
try:
    my_file = open("myfile.txt")
except FileNotFoundError:
    print("File not found")





