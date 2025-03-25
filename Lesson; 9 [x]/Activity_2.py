#  Write a programm to calculate the electricity bill. The bill should be calculated by checking the number of electrical units consumed. Suppose the user is consuming less than 50 units, thee per unit cost will be $2.60 nd the tax on the bill will be $25
Units=int(input("Please enter the number of units of electricity you have consumed here:  "))
if (Units > 50):
    amount=Units * 2.60
    tax=25
elif (Units < 100):
    amount=130 + ((Units-50)*3.25)
    tax=35
elif (Units < 200):
    amount=(130 + (162.5)) + ((Units-100)*5.26)
    tax=45
else:
    amount=(656+15.50)+(Units-200)*8.45
    tax=75

total=(amount+tax)
print("Electricity bill is: ",total)
