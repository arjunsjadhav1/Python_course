import turtle
turtle.Screen().setup(360,480)
p = turtle.Turtle()
n = 4
n2 = 50
for i in range(n+1):
    p.forward(n2)
    p.right(90)
turtle.done()