a=([1,2,3,4],5,6,7,8,9)
try:
        a[0].append(1)
except:
        a.append(1)
print(a)
print(a[0:6:1])
