from turtle import Turtle

# setup: creates a turtle
def setup():
    my_turtle = Turtle()
    return my_turtle

turtle = setup()
turtle.speed(1)
turtle.circle(100)
turtle.color("green")
for i in range(100):
    turtle.forward(i+5)
    turtle.right(10)