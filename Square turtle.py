import turtle # Draw a square

t = turtle.Turtle()
t.fillcolor('Green')
t.begin_fill()

def draw_square():

    for i in range(4):
        t.forward(150)
        t.write('150 cm')
        t.left(90)

Squ = draw_square()
t.end_fill()
turtle.done()