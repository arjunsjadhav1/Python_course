n=int(input("enter a number..: "))
sum=0
tamp=n
while tamp > 0:
    d=tamp%10
    sum+=d**3
    tamp//=10
if n == sum:
    print(n,"is an armstrong number.")
else:
    print(n,"is a non-armstrong number.")