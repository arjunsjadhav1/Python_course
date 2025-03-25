v1=int(input())
v2 = (v1-(v1%2))
if v2 >= 1:
    if v2 >= 1:
        while v2 >= 1:
         print((v2%2),(v2-(v2%2)))
         v2 = (v2-v2%2)
    else: print((v1%2),v1-(v1%2))
elif (v1-(v1%2)) == 1:
    print("01")
else:
    print("00")

