a=int(input("enter year:"))
if (a%100==0)&(a%400==0):
    print("year is leap")
elif (a%4==0)&(a%100!=0):
    print("year is leap")
else:
    print("year is not leap")