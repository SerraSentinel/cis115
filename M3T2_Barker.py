# CIS 115
# Barker Jacob
# M3T2
# 3 October 2018

# Turtle Python example 2

import turtle

def main():
    alex = turtle.Turtle()
    bob = turtle.Turtle()
    christine = turtle.Turtle()

    # customize the turtles
    alex.pensize(3)
    bob.pensize(4)
    christine.pensize(2)
    alex.pencolor("red")
    bob.pencolor("green")
    christine.pencolor("blue")

    sides = int(input("Number of sides? "))
    size = int(input("Size of polygon? "))

    # space the turtles
    alex.backward(size*2)
    bob.forward(0)
    christine.forward(size*2)

    for Turtle in (alex, bob, christine):
        drawPolygon(sides, size)

    #drawPolygon (alex, sides, size)
    #drawPolygon (bob, sides, size)
    #drawPolygon (christine, sides, size)

def drawPolygon (t, sides, size):
    """uses turtles to draw a n sided polygon
        input: t - a turtle
                  sides - number of sides
                  size - length of one side

    """
    for side in range(sides):
        t.forward(size)
        t.right(360/sides) # angle depends on polygon


# run program
main()
