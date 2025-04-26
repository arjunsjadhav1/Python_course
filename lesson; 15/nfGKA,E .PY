v1=[1,2,3,4]
v3=0
while v3 <= len(v1):
    if v3 != v1[3]:
     v4=(v1[v3])*(v1[v3+1])
    else:
       v4=(v3)
    print(v4)
    v3=(v3+1)