V1=input("enter word here: ")
V2=input("enter character to be searched: ")
V3=0
V4=0
while V3 < len(V1):
    if V1[V3]==V2:
        V4=V4+1
    V3=V3+1
print(V4)
