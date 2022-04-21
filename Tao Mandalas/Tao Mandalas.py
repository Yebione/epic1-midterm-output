import turtle

turtle.bgcolor("Black")
turtle.title("Tao Mandalas")
turtle.setup(1162,654)

t = turtle.Turtle()
t.pencolor("orange")
t.speed(10)

# Function to reposition pen without drawing a line
def repos(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()

#6-sided Star
repos(0,-55)
t.left(70)
for i in range(8):
    t.forward(100)
    t.left(135)

#Central Diamond
repos(-2,-23)
t.left(335)
for i in range(4):
    t.forward(31)
    t.left(90)
t.right(45)

#Inner Circles
repos(0,-55)
t.width(3)
t.circle(55)

repos(0,-75)
t.width(1)
t.circle(75)

repos(0,-90)
t.width(3)
t.circle(90)

#Double Diamond
def dia (b):
    for i in range(4):
        t.forward(225)
        if b == 1:
            t.left(90)
        else:
            t.right(90)

t.width(1)

repos(-70,-143)
t.left(20)
dia(1)

repos(70,-143)
t.right(220)
dia(0)

#Outer Circle 1
repos(0,-160)
t.width(3)
t.left(200)
t.circle(160)

#Octa-Pentagon
repos(5,-160)
t.width(2)
for i in range(8):
    t.left(25)
    t.forward(42)
    t.left(415)
    t.forward(34)
    t.right(115)
    t.forward(34)
    t.left(60)
    t.forward(42)
    t.left(20)

#Outer Circle 2-4
repos(0,-180)
t.width(3)
t.circle(180)

repos(0,-170)
t.width(1)
t.circle(170)

repos(0,-225)
t.width(3)
t.circle(225)

#Runic Characters
char = ["‡","ƒ","¤","±","o","µ","¿","æ","ø","ß"]
repos(10,-217)
for i in range(4):
    for j in char:
        t.pendown()
        t.write(j,font=("calibri", 20))
        t.penup()
        t.left(9)
        t.forward(32)

#Outermost Dodecagon
repos(76,-285)
t.width(1)
for i in range(12):
    t.left(30)
    t.forward(152)

#Triangles Inside Dodecagon
t.left(67)
for i in range(12):
    t.forward(95)
    t.right(74)
    t.forward(95)
    t.left(104)

#Final Circle
repos(0, -260)
t.right(67)
t.circle(260)

#A Strange Background (Pun intended lol)
turtle.bgpic("Strange.gif")

# Prevent turtle from closing
t.screen.mainloop()