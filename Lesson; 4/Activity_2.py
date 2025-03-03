amount=int(input("please enter amount of withdrawl"))
notes=amount//100
notes_2=(amount%100)//50
notes_3=((amount%100)%50)//10
notes_4=(((amount%100)%50)%10)//1
print("notes of hundred rupees:",notes)
print("notes of 50 rupees:",notes_2)
print("notes of 10 rupees:",notes_3)
print("1 rupee coins:",notes_4)