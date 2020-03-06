# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.
done = False
donetwo = False
donethree = False
while not done:
    try:
        massone = float(input("Input mass 1: "))
        done = True
        while not donetwo:
            try:
                masstwo = float(input("Input mass 2: "))
                donetwo = True
                while not donethree:
                    try:
                        distance = float(input("Input distance between bodies: "))
                        donethree = True
                    except:
                        print("Not a valid integer")
            except:
                print("Not a valid integer")

    except:
        print("Not a valid integer")


donefour = False
while not donefour:
    try:
        x = (6.67 ** -11) * (massone * masstwo) / distance ** 2
        print("The force of gravity is: ", "{:.3}".format(x), "newtons")
        donefour = True
    except ZeroDivisionError as h:
        print(h, "error in calculation")
        donefour = True




