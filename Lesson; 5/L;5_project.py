t=int(input("Please enter the current air temperature in Celcius:"))
if t>30 and t<45:
    print("The wheater is quite hot today, at a whopping",(t),"C.")
elif t>=45:
    print("The weather is absolutely scorching today, at a immense temperature of",(t),"C!")
elif t<30 and t>0:
    print("The weather is cold today, at a chilly",(t),"C.")
elif t<=0:
    print("The weather is absolutely freezing today, at a very low temperature of",(t),"C!")
else:
    print("the weather is perfectly normal today, at a stable temperature of",(t),"C.")