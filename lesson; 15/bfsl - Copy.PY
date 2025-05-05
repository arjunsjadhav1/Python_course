l1=["apple","pineapple","apricot",]
l2=set()
for v1 in range (0,(len(l1))):
    v2=l1[v1]
    for v3 in range (0,(len(l1))):
     if "e" in v2:
        l2.add(v2)
print(l2)


