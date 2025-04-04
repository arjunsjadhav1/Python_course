import turtle
turtle.Screen().setup(360,480)
p = turtle.Turtle()
n = (input("sides: "))
n2 = float(input("size:"))
if n < 3:
    print("this is an invalid amount of sides.")
elif n == 3:
    l = 360
else:
    l = 360
for i in range(n+1):
    p.forward(n2)
    p.right(l/n)
turtle.done()
