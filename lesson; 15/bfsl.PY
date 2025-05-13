import math as ma
v1=input("'r/d' : ")
if v1 == "r" or v1 == "R" or v1 == "radius" or v1 == "Radius":
    v2 = float(input("radius:"))
    v3=("area:",(ma.pi)*(v2**2))
    v4=("circumference:",((ma.pi)*2)*v2)
    print("area:",v3,"circumference:",v4)
elif v1 == "d" or v1 == "D" or v1 == "Diameter" or "diameter":
    v2 = float(input("diameter:"))
    v3 = ("area:",(ma.pi)*((v2/2)**2))
    v4 = ("circumference:",((ma.pi)*v2))
else:
    print("write either 'r' or 'd' for either radius or diameter respectufffly.")


