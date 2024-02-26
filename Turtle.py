#CS175
#Jared Mishen
#Turtle graphics STOP sign

import math
import turtle


screen = turtle.Screen()
screen.bgcolor('black')


t = turtle.Turtle()
t.color('white', 'red')

def draw_stopsign(t, x, y, length):
    t.penup()
    t.setpos(x - length/2, y + length/2 / (math.pi/8))
    t.pendown()
    t.color('white', 'red')
    t.pensize(length // 10)
    t.begin_fill()

    for i in range (8):
        t.forward(length)
        t.right(45)
    t.end_fill()

    fontsize = int(length /2)
    t.penup()
    t.setpos(x, y - fontsize/2)
    t.pendown()
    t.write('STOP', move=False, align='center', font=('Arial', fontsize, 'normal'))
    t.hideturtle()

draw_stopsign(t, 0, 0, 100)


turtle.mainloop()
