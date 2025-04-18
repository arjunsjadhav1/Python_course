import random
a=["try again.","no","incorrect","wrong","nope"]
v2=str(random.randint(0,50))
while True:
    g=input()
    if v2 == g:
        print("VICTORY!")
    else:
        print(random.choice(a))

