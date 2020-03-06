#  Recursion - function calling itself

def f():
    print("f")
    #  f()  # similar to an infinte loop, but different.  RecursionDepthError
    print("END")


f()  # calling itself


def g():
    print("g")
    f()

g()


# Controlling recursion with depth
def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed.")

controlled(0, 10)









