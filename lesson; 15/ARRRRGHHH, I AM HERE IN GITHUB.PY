import math as ma
v1=input("'r/d' : ")
if v1 == "r":
    v2 = float(input("radius:"))
    v3=("area:",(ma.pi)*(v2*v2))
    v4=("circumference:",((ma.pi)*2)*v2)
    print("area:",v3,"circumference:",v4)
elif v1 == "d":
    v2 = float(input("diameter:"))
    v3 = ("area:",(ma.pi)*((v2/2)**2))
    v4 = ("circumference:",((ma.pi)*v2))
    print("area:",v3,"circumference:",v4)
else:
    while (v1 != "d") and (v1 != "r"):
     print("write either 'r' or 'd' for either radius or diameter respectufuly.")
     v1=input("'r/d' : ")

