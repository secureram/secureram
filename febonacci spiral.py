"""
"""

import random
def febo(n):
        if n < 3:
                return 1
        else:
                return febo(n - 1) + febo(n - 2)


from turtle import Turtle, colormode

t = Turtle()
colormode(255)

t.setheading(180)

def drawsquare(length):
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)

def main():
    for i in range(1, 20):
        length = febo(i)
        print(length)
        t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.begin_fill()
        drawsquare(length)
        t.end_fill()
        t.forward(length)
        t.left(90)
        t.forward(length)
        

main()
