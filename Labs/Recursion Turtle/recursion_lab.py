'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursiveh(x, y, length, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x,y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.left(180)
        my_turtle.forward(length*2)
        my_turtle.right(180)
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length*2)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.left(180)
        my_turtle.forward(length * 2)
        my_turtle.up()
        my_turtle.left(90)
        recursiveh(x + length, y + length, length // 2, depth - 1)
        recursiveh(x +length, y - length, length // 2, depth - 1)
        recursiveh(x - length, y + length, length // 2, depth - 1)
        recursiveh(x - length, y - length, length // 2, depth - 1)


recursiveh(0, 0, 100, 3)


my_screen.clear()
# first square does not draw when it is after the h drawing

def recurisvesq(x, y, length, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(length)
        [pos1x, pos1y] = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(length)
        [pos2x, pos2y] = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(length)
        [pos3x, pos3y] = my_turtle.pos()
        my_turtle.right(90)
        my_turtle.forward(length)
        [pos4x, pos4y] = my_turtle.pos()

        recurisvesq(pos1x - (length // 4), pos1y + (length // 4), length // 2, depth - 1)
        recurisvesq(pos2x - (length // 4), pos2y + (length // 4), length // 2, depth - 1)
        recurisvesq(pos3x - (length // 4), pos3y + (length // 4), length // 2, depth - 1)
        recurisvesq(pos4x - (length // 4), pos4y + (length // 4), length // 2, depth - 1)


recurisvesq(-100, 100, 200, 4)

my_screen.clear()


def turningsq(x, y, length, turn, depth):
    if depth > 0:
        for i in range(8):
            my_turtle.up()
            my_turtle.goto(x, y)
            my_turtle.down()
            my_turtle.right(turn)
            my_turtle.forward(length)
            my_turtle.right(90)
            my_turtle.forward(length)
            my_turtle.right(90)
            my_turtle.forward(length)
            my_turtle.right(90)
            my_turtle.forward(length)
        turningsq(x, y, length // 1.5, turn, depth - 1)


turningsq(0, 0, 250, 45, 7)


















my_screen.exitonclick()