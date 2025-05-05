
a={"1":1,"2":2,"3":3,"4":4}
c=input("ting to ad")
b=a.copy()
a.clear()
a[c]=c
a[""]=b
print(a)