# from math import pi
# import turtle

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# def polygon(t, length, n):
#     degrees = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(degrees)

# def circle(t,r):
#     circunference = 2 * pi * r
#     n = int(circunference)
#     length = circunference / n
#     polygon(t,length,n)

# def arc(t,r,angle):
#     arc_length = 2 * pi * r * angle / 360
#     n = int(arc_length)
#     length = arc_length / n
#     arc_angle = angle / n
#     for i in range (n):
#         t.fd(length)
#         t.lt(arc_angle)

# bob = turtle.Turtle()
# print(bob)

# arc(bob,100,180)

# turtle.mainloop()

# import math
# import turtle

# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 4) + 3
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, length=step_length, angle=step_angle)

# def petala(t, r, angle):
#     for i in range(2):
#         arc(t, r, angle)
#         t.lt(180-angle)

# def flower(t, r, n, angle):
#     for i in range(n):
#         petala(t, r, angle)
#         t.lt(360 / n)

# def move(t, length):
#     t.pu()
#     t.fd(length)
#     t.pd()

# bob = turtle.Turtle()

# move(bob, -200)
# flower(bob, 60, 7, 60)

# move(bob, 200)
# flower(bob, 40, 10, 80)

# move(bob, 200)
# flower(bob, 140, 20, 20)

# bob.hideturtle()

# turtle.mainloop()

# import math
# import turtle

# def isoceles(t, r, angle):
#     y = r * math.sin(angle * math.pi / 180)
#     t.rt(angle)
#     t.fd(r)
#     t.lt(90 + angle)
#     t.fd(2 * y)
#     t.lt(90 + angle)
#     t.fd(r)
#     t.lt(180 - angle)

# def pedaco(t, n, r):
#     angle = 360 / n
#     for i in range(n):
#         isoceles(t, r, angle / 2)
#         t.lt(angle)

# def pizza(t, r, n):
#     pedaco(t, n, r)
#     t.pu()
#     t.fd(r * 2 + 10)
#     t.pd()

# def move(t, length):
#     t.pu()
#     t.fd(length)
#     t.pd()

# bob = turtle.Turtle()

# tamanho = 60

# move(bob, -200)
# pizza(bob, tamanho, 8)

# move(bob, 200)
# pizza(bob, tamanho, 9)

# move(bob, 200)
# pizza(bob, tamanho, 10)

# bob.hideturtle()

# turtle.mainloop()

import turtle
import math

def arquimediana(t, n, a=1, b=3):

    for i in range(n):
        theta = i / 20 * math.pi
        x = (a + b * theta) * math.cos(theta)
        y = (a + b * theta) * math.sin(theta)
        t.goto(x, y)
        

bob = turtle.Turtle()

arquimediana(bob, n=1000)

turtle.mainloop()