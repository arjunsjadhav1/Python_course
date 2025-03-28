V1=int(input())
V2=V1
V3=0
while V2 > 0:
    V4=V2%10
    V3=V3+(V4**3)
    V2=V2//10
if V2 == V1:
    print("THIS IS AN 'ARMSTRONG NUMBER'.")
else:
    print("THIS IS NOT AN 'ARMSTRONG NUMBER'.")