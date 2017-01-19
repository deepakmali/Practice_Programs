#This program is like intro to use turtle to 
#draw a square.
#we use different window bgcolors and different 
#turtle size and the speed at which it moves.

import turtle

def draw_square():
	tort = turtle.Turtle()
	window.bgcolor('aqua')
	tort.shape('turtle')
	tort.color('red','green')
	tort.speed(1)
	tort.begin_fill()
	for i in range(4):
		tort.forward(100)
		tort.right(90)
	tort.fill(True)
	tort.end_fill()
def draw_circle():
	tort2 = turtle.Turtle()
	tort2.color('blue')
	tort2.circle(100)
def draw_triangle():
	tort3 = turtle.Turtle()
	tort3.color('black')
	for i in range(3):
		tort3.forward(150)
		tort3.right(180 - 60)
window = turtle.Screen()
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()
