a=int(input("enter lower range :)"))
b=int(input("enter upper range :)"))
l2=[]
l3=[]
l4=[]
v3=0
v1=0
for v2 in range (a,(b+1)):
   l2.append(v2**2)
   if (l2[v3])%2 == 0:
      l3.append(l2[v3])
   else:
      l4.append(l2[v3])
   v3 = (v3+1)
print("even:",l3)
print("odd: ",l4)

