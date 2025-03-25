lower=int(input("lower range: "))
upper=int(input("upper range: "))
print("prime numberes between",lower,"and",upper,"are: ")
for n in range(lower,upper+1):
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                break 
        else:
            print(n)



