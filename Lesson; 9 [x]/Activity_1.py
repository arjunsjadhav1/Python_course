#Wriite a programm to check wheater a student is allowed to take an exam or not. Should the student be allowed, a condition  must be fuffiled:  they do not have a medical cause. (if yes then they would be accepted, and allowed to proceed to thee second examnation.) (if not, check the attendance (if the attendance is above 75, the exam will be taken, if not, the exam will not be taken.))
YN=input("do you have medical cause? [Y/N]")
att=float(input("Enter the attendence of the student"))
if YN is "Y":
    print("The student may proceed")
else:
    if att >= 75:
        print("The student may proceed")
    else:
        print("The student may not continue")



 