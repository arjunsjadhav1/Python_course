bill = float(input("bill:"))
tip = float(input("tip %:"))
def a(b,t):
    sf = (b+((b/100)*t))
    st = round(sf,2)
    return(st)
print("pls pay $",a(bill,tip))

