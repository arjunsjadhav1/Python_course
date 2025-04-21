from datetime import datetime,time
import pytz
v1=pytz.timezone("Asia/Singapore")
t=datetime.now(v1)
b=t.minute
c=t.hour
if (c == 7) and (b == 0):
    print("IT IS TIME TO WAKE UP!")
    print("WAKE UP!!!!")
    time.sleep(2)
    d=input("Snooze? [Y/N]")
    if d == "Y":
        if (c == 7) and (b == 5):
          print("IT IS TIME TO WAKE UP!")
          print("WAKE UP!!!!")
          time.sleep(2)
          e=input("Snooze? [Y/N]")
          if e == "Y":
            print("ONLY ONCE!")
            print("shutting down...")
          elif e == "N":
             print("shutting down...")
          else:
             print("either Y or N!")
        else:
           print("Only once!")
           print("shutting down...")
    elif d == "N":
       print("shutting down...")
    else:
       print("either Y or N!")
else:
   print("shutting down...")