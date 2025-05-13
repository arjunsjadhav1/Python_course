class vehicles:
 def vehicle_1(self,v1,v2,v3):
     v4=v1*v2
     v3=v4/v3
     v1=v2
     v2=v2*2
     return (v1,v2,v3,v4)
 def vehicle_2(self,v5,v6,v7):
     v5=v7/(v6**2)
     v6=v5*v7
     v7=v5
     return (v5,v6,v7)
class vehicle1(vehicles):
  pass
v10=vehicle1()
v11=v10.vehicle_1(1,2,1)
print(v11)

