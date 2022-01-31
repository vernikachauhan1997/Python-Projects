import turtle   # Draw a spikaling Star
import random

star = turtle.Turtle()
star.speed('fastest')
Colours = ['Red', 'Blue', 'Orange', 'Green', 'Pink','Yellow','Black','Purple']
star.fillcolor('Blue')
star.begin_fill()

for i in range(50):
    star.color(random.choices(Colours))
    star.forward(10*i)
    star.right(144)

star.end_fill()    
turtle.exitonclick()