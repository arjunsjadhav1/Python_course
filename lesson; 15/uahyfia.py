print("items")
print("apple 1.20")
print("orange 0.90")
print("pineapple 1.80")
v1=(input("choose an item: "))
v2=float(input("payment: "))
if v1 == "apple":
    v3 = 1.2
elif v1 == "orange":
    v3 = 0.9
elif v1 == "pineapple":
    v3 = 1.8
else:
    print("this is not a currently valid item.")
def alg():
    return((v2-v3))
v4 = alg()
print("change: ","$",(float(v4)))