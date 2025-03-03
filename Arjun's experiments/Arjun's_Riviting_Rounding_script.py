import math

v1 = input("Enter the number ")

try:
    # Convert it into integer
    val = int(v1)
    print(val)
except ValueError:
    try:
        # Convert it into float
        val = float(v1)
        if val-math.floor(val) >= 0.5:
            print(math.floor(val)+1)
        else:print(math.floor(val))

            
    except ValueError:
        print("please enter a numerical input")
        