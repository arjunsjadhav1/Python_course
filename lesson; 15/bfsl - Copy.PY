import random
v1=random.randint(1,100)
try:
 v2=int(input("ur guess:"))
except:
 print("enter a whole number")
 v1=int(input("ur guess:"))
while v2 > 100:
    print("Maximum number is 100")
    v2=int(input("ur guess:"))
v3=1
while v3 == 1:
  if v2 == v1:
    print("-------------YOU WON!-------------------")
    print("-run the code again to start a new game-")









