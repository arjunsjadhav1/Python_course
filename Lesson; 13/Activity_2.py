V1=float(input("enter out of 500 marks: "))
V2=float(input("enter attendance: "))
V3=V1
if V1-(int(V3)) >= 0.5:
    V1 = (int(V3)+1)
if V1 < 300 and V2 < 74.5:
    print("this student is not eligible for the partaking of the examnation.")
else:
    print("this student is eligible for the partaking of this examnation.")
