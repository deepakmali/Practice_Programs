#This is an attempt to create a flower using turtle.

import turtle

flow = turtle.Turtle()
flow.color('white')
flow.shape('classic')
window = turtle.Screen()
window.bgcolor('black')
#flow.right(90)
#flow.forward(300)
#flow.backward(300)
flow.begin_fill()
for i in range(36):
  flow.forward(200)
  flow.right(180-10)
flow.end_fill()
#flow.right(180-10)
flow.forward(100)
flow.setheading(270)
flow.forward(200)
window.exitonclick()
