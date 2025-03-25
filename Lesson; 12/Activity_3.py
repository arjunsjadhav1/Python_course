v1=int(input("enter a number: "))
t=v1
l=0
while t > 0:
    l = l+1
    t = int(t/10)
if l >= 4:
    l = int(l/2)
    check=0
    while 0 < v1:
        rem=v1%10
        if check == l:
            mid1=rem
        elif check == l-1:
            mid2=rem
        v1=int(v1/10)
        check = check+1
    prod=mid1*mid2
    print("prosuct of the midlle digits are: ",prod)
else:
    print("this number does not consist of enough digits.")
