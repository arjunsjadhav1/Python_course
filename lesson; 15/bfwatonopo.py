print("would you like to start the shutdown sequence?")
v1=input("[Y/N]: ")
def shutdown():
    if v1 == "Y":
        return("shutting down...")
    elif v1 == "N":
        return("shutdown aborted.")
    elif v1 == "y":
        return("shutting down...")
    elif v1 == "n":
        return("shutdown aborted.")
    else:
        return("Please enter a valid input. should you like to shutdown, run this code again and enter 'Y'")
v2 = shutdown()
print(v2)
