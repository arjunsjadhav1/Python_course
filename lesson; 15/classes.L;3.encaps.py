class h:
    def H(self,__v1):
        return (__v1)
v2=h.H(1)
try:
    v2 = (v2*2)
except AttributeError:
    print("privite variables cannot be changed.")



    