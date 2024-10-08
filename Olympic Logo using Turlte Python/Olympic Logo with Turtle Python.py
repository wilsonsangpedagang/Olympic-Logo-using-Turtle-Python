import tkinter.messagebox
import turtle # import turtle library
import random # import random for chessboard colors
# olympic logo

# colors
blue = (0,129/255,200/255)
yellow = (252/255,177/255,49/255)
black = (0,0,0)
green = (0,166/255,81/255)
red = (238/255,51/255,78/255)
circlesize = 50

# Random Colored Chessboard Prompt
row = int(turtle.numinput("rows", "How many rows for the chessboard", 0, 2,25 )) # input the number of row of chessboard
size = int(turtle.numinput("size", "Input the size of the chessboard",0,5,50))  # input the size of the chessboard

turtle.shape("turtle")
turtle.pensize(8)
turtle.speed(11)
turtle.hideturtle()

turtle.penup()
turtle.goto(-120,170) # now the position is (-120, 170)
turtle.pendown()

# The Blue Circle
turtle.color(blue)
turtle.circle(circlesize)

# Move to the next position
turtle.penup()
turtle.forward(120) # now the position is (0,170)

# Start drawing again
turtle.pendown()

# The Black Circle
turtle.color(black)
turtle.circle(circlesize)

# Move to the next position
turtle.penup()
turtle.forward(120) #now the position is (120,170)

# Start Drawing again
turtle.pendown()

# The red circle
turtle.color(red)
turtle.circle(circlesize)

# Move to the next position
turtle.penup()
turtle.goto(-60,120) # now the position is (-60,120)

# Start drawing again
turtle.pendown()

# The yellow circle
turtle.color(yellow)
turtle.circle(circlesize)

# Move to the next position
turtle.penup()
turtle.forward(120) # now the position is (60,120)

# Start drawing again
turtle.pendown()

# The green circle
turtle.color(green)
turtle.circle(circlesize)

turtle.penup()

turtle.goto(-120,170)

turtle.pendown()

# to make the interlocking effect we need to draw the lines again
# we are making the blue lines overlapping the yellow lines
turtle.color(blue)
turtle.circle(circlesize, -300) # so turtle.circle has a property called extent. This property is used to draw parts of circle by the angle.

turtle.penup()
turtle.goto(0, 170)
turtle.right(60) # because the angle is modified in the extent property inside turtle.circle, we make it right by turning it into 0 angle.

turtle.pendown()

turtle.color(black) # circle color black
turtle.circle(circlesize,-30) # circle radius 50 for just 30 deg

turtle.penup()
turtle.goto(0,170) # moving to the next location

turtle.pendown()
turtle.right(330) # adjusting the angles
turtle.circle(circlesize,110) # circle radius 50 for 110 deg

turtle.penup()
turtle.goto(-60,120) # moving to the next location

turtle.right(-250) # adjusting the angles

turtle.pendown()
turtle.color(yellow) # circle color
turtle.circle(circlesize, -110) # circle radius 50 for -110 deg

turtle.penup()
turtle.goto(60,120) # moving to next location

turtle.right(250) # adjusting the angles

turtle.pendown()
turtle.color(green) # circle color green
turtle.circle(circlesize,-110) # circle radius 50 for -110 deg

turtle.penup()
turtle.goto(60,120) # moving to next location
turtle.right(250) # adjusting the angle

turtle.pendown()
turtle.color(green) # circle color green
turtle.circle(circlesize,180) # circle radius 50 for 180 deg

turtle.penup()
turtle.goto(120,170) # moving to the next location
turtle.right(180) # adjusting the angle

turtle.pendown()
turtle.color(red) # circle color red
turtle.circle(circlesize,-60) # circle radius 50 for 60 deg




# the straight olympic circle

turtle.penup()
turtle.goto(-120,0) # the initial postion of the circle
turtle.right(300) # adujusting the angle

turtle.pendown()
turtle.color(blue)
turtle.circle(circlesize) # make a circle with the size of circle size

turtle.penup()
turtle.goto(-60,0) # going to the next position

turtle.pendown()
turtle.color(yellow)
turtle.circle(circlesize)

turtle.penup()
turtle.goto(0,0)

turtle.pendown()
turtle.color(black)
turtle.circle(circlesize)

turtle.penup()
turtle.goto(60,0)

turtle.pendown()
turtle.color(green)
turtle.circle(circlesize)

turtle.penup()
turtle.goto(120,0)

turtle.pendown()
turtle.color(red)
turtle.circle(circlesize) # the last circle

turtle.penup()
turtle.goto(-120,0) # to interlock the rings, we need to overlap the circles

turtle.pendown()
turtle.color(blue)
turtle.circle(circlesize,-300) # make a circle with the size of circle size for 300 degrees clockwise

turtle.penup()
turtle.goto(-60,0)
turtle.right(60) # adjusting the angle

turtle.pendown()
turtle.color(yellow)
turtle.circle(circlesize,180)

turtle.penup()
turtle.goto(0,0)
turtle.right(-180)

turtle.pendown()
turtle.color(black)
turtle.circle(circlesize, -60)

turtle.penup()
turtle.goto(0,0)
turtle.right(300)

turtle.pendown()
turtle.color(black)
turtle.circle(circlesize, 180)

turtle.penup()
turtle.goto(60,0)
turtle.right(-180)

turtle.pendown()
turtle.color(green)
turtle.circle(circlesize, -60)

turtle.penup()
turtle.goto(60,0)
turtle.right(300)

turtle.pendown()
turtle.color(green)
turtle.circle(circlesize, 180)

turtle.penup()
turtle.goto(120,0)
turtle.right(-180)

turtle.pendown()
turtle.color(red)
turtle.circle(circlesize, -60)

turtle.penup()
turtle.right(300)

turtle.goto(-60,-50)
turtle.pensize(1)
turtle.pendown()


# loop for one square block
angle = 90 # The corners in a square is 90 degrees

for i in range(row): # loop for each row
    for j in range(row): # loop for each column
        red = random.randint(0, 255) # outputs a random integer from 0 - 255
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        turtle.color(red / 255, green / 255, blue / 255) # common rgb color values

        turtle.begin_fill() # to color the squares, we need the begin_fill and end_fill function
        for k in range(4): # the square has 4 sides,
            turtle.forward(size) # line of code for 1 side of the square
            turtle.left(angle) # for turning in the corners of the square
        turtle.end_fill()
        turtle.forward(size)

    turtle.penup()
    turtle.goto(-60,-50 - (size * (i + 1))) #
    turtle.pendown() # the turtle is back the first x position of that row , the y value will be decreased according to i (the row counts) so it goes down 1 square vertically

turtle.penup()
turtle.goto(0,-190)
turtle.pendown()
turtle.write("Olympic Logo and Coloerful Chessboard of Squares" ,"False", "Center", "Arial")


turtle.exitonclick()