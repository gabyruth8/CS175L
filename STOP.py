import turtle
import math

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
INNER_LENGTH = LENGTH - 20  
TEXT_X = -20
TEXT_Y = -140  

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()


turtle.pencolor('red')
turtle.pensize(10)

for _ in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(360 / NUM_SIDES)

turtle.penup()
turtle.goto(10, -20)
turtle.pendown()
turtle.pencolor('red')
turtle.pensize(10)

for _ in range(NUM_SIDES):
    turtle.forward(INNER_LENGTH)
    turtle.right(360 / NUM_SIDES)


turtle.fillcolor('red')
turtle.begin_fill()

for _ in range(NUM_SIDES):
    turtle.forward(INNER_LENGTH)
    turtle.right(360 / NUM_SIDES)

turtle.end_fill()

turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.pendown()

turtle.color("white")
turtle.write("STOP", font=("Arial", 40, "bold"))

turtle.hideturtle()

turtle.done()

