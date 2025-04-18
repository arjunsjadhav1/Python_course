print("1 for age in months & yrs")
print("2 for age in decimal of 10")
try:
 v1=int(input("1,2"))
 if v1 == 1:
   v6=int(input("yrs: "))
   v3=int(input("months(inp/12): "))
   v2 = 0
 elif v1 == 2:
   v3=float(input("DECIMAL OF out of 10: "))
   v2 = 1
 else:
   print("EITHER 1 OR 2. NO OTHER NUMBER!!!!!!!")
 if v2 == 0:
   print("yrs:",v6,"months:",v3)
 else:
   v7=(12/(10/(v3*10)))
   v8=int(v7/12)
   v9=(v7-(v8*12))
   print("yrs:",v8,"months:",v9)
except ValueError:
   print("EITHER 1 OR 2. THAT IS'INT EVEN A NUMBER!!!!!!")


  




