try:
 v1=input("----->") #name
 v2=input("----->") #grade
 class innit():
  def __init__(self,v1,v2):
   self.v1 = v1
   self.v2 = v2
   return print("hello. my name is, ",v1," .","I am in grade ",v2," .")
 a = innit(v1,v2)
 print(a)
except:
 print("THERE IS AN ERROR!!!!!")
 



