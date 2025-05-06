import random
v1=random.randint(0,100)
v3=1
while v3 == 1:
  try:
   v2=int(input("ur guess:"))
  except:
    print("enter a whole number")
    v2=int(input("ur guess:"))
  while v2 > 100:
   print("enter a number below 100")
   v2=int(input("ur guess:"))
  while v2 < 0:
    print("enter a number above -1")
    v2=int(input("ur guess:"))
  if v2 == v1:
    print("---------------YOU WON!-----------------")
    print("-run the code again to start a new game-")
    break
  elif v2 < v1:
    print("no, the number is greater,")
    if (v1-5) <= v2:
      print("you are close")
    else:
      pass
  elif v2 > v1:
    print("no, the number is smaller, try again")
    if (v1+5) >= v2:
      print("you are close")
    else:
      pass



  









