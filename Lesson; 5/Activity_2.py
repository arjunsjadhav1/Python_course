actual_cost=int(input("please enter the actual cost here:"))
#print(actual_cost)
sales_amount=int(input("Please enter the sales amount here:"))
if sales_amount>actual_cost:
    amount=sales_amount-actual_cost
    print("total profit amountage",{amount})
else:
    print("amount of money lost",{actual_cost-sales_amount})
     

