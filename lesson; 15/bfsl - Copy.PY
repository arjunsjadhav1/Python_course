import random
v38=0
v37=0
v24=0
v23=0
v17=0
v10=input("1/2/3/4 -- easy / medium / hard / blind  modes: ")
if v10 == "1":
  v11=100
  v12=10
  print("")
  print("easy mode selected.")
  print("the maximum possible number is 100")
  print("the maximum guesses is 10")
elif v10 == "2":
  v11=150
  v12=7
  print("")
  print("medium mode selected")
  print("the maximum number possible is 150")
  print("the maximum guessses is 7")
elif v10 == "3":
  v11=200
  v12=7
  print("")
  print("hard mode selected.")
  print("the maximum namber possible is 200")
  print("the maximum guesses is 7")
elif v10 == "4":
  print("")
  print("blind mode selected")
  print("the messages such as 'no, the number is greater,' will not mean anything(besides the first round in which it will have some level of meaning to allow you to ease into this mode.) during blind rounds, they will be completly obsolete.")
  print("the rounds will progressivly increase their maximum possible number.")
  print("the maximum number of guesses is 100/round.")
  v11=100
  v12=100
  v17=1
else:
  v31=random.randint(1,4)
  if v31 == 1:
    v32 = "1"
  elif v31 == 2:
    v32 = "2"
  elif v31 == 3:
    v32 = "3"
  else:
    v32 = "4"
  if v32 == "1":
   v11=100
   v12=10
   print("")
   print("easy mode selected.")
   print("the maximum possible number is 100")
   print("the maximum guesses is 10")
  elif v32 == "2":
   v11=150
   print("")
   print("medium mode selected")
   print("the maximum number possible is 150")
   print("the maximum guessses is 7")
  elif v32 == "3":
   v11=200
   v12=7
   print("")
   print("hard mode selected.")
   print("the maximum namber possible is 200")
   print("the maximum guesses is 7")
  elif v32 == "4":
   print("")
   print("blind mode selected")
   print("the messages such as 'no, the number is greater,' will not mean anything during blind rounds(besides the first round in which it will have some level of meaning to allow you to ease into this mode.), they will be completly obsolete.")
   print("the rounds will progressivly increase their maximum possible number.")
   print("the maximum number of guesses is 100/round.")
   print()
   v11=100
   v12=99999999999
   v17=1
v1=random.randint(0,v11)
for v15 in range(0,v12):
  if v24 == 1:
    v1=random.randint(0,v23)
    v11=v23
  else:
    pass
  try:
   v2=int(input("ur guess:"))
   print(v15+1)
  except:
    print("enter a whole number")
    v2=int(input("ur guess:"))
    print(v15+1)
  while v2 > v11:
   print("enter a number below",v11)
   v2=int(input("ur guess:"))
   print(v15+1)
  while v2 < 0:
    print("enter a number above -1")
    v2=int(input("ur guess:"))
    print(v15+1)
  if v2 == v1:
    print("")
    print("---------------YOU WON!-----------------")
    v38=1
    if v17 == 1:
     z=input("           [y/n]      start a new game?-")
     print("")
     if z == "y" or z == "Y":
       v37=(v37+1)
       v23=(v11+20)
       v24=1
       pass
     elif z == "n" or z == "N":
       break
     else:
       print("YOU WERE SUPPOSED TO WRITE EITHER 'y' OR 'n'!")
       break
    else:
      print("")
      print("Run the code again to play again!")
      print("...")
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
if v38 == 1:
 pass
else:
 if v17 == 1:
   print("")
   print("Game Ended.")
   print("")
   print("your blind wins: [",(v37-1),"] .")
   print("")
 else:
   print("")
   print("")
   print("MAX attempts reached [",v12,"] .")
   print("Game Over")
   print("")
   print("The number was...",v1)
   print("")