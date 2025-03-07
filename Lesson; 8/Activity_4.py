# Question:  Three cyclists are riding at a speed of [], [] and [] km an hour. find the average and find which cyclist is cycling below average speed.
fc1=input()
fc2=input()
fc3=input()
cyclist_1=float(fc1)
cyclist_2=float(fc2)
cyclist_3=float(fc3)
avg=(((cyclist_1+cyclist_2)+cyclist_3)/3)
print("avg is:",avg)
if cyclist_1 < avg:
    print("Cyclist 1 is below average speed.")
elif cyclist_2 < avg:
    print("cyclist 2 is below average speed.")
elif cyclist_3 < avg:
    print("cyclist 3 is below average speed.")
else:
    print("All cyclists are travveling at an equal speed.")





