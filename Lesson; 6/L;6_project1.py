v1 = input("DO *NOT* ENTER A CHARACTER WHICH IS NOT AN INTEGER, FLOAT OR STRING. please Enter a integer, float or string here:  ")
try:
    # input is integer
    val = int(v1)
    print("this is not a string, this is a integer")
except ValueError:
    try:
        # input is float
        val = float(v1)
        print("This is not a string, this is a float.")
              
           #input is .str 
    except ValueError:
        val = str(v1)
        print("This is infact a string!")


