def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
choice=int(input("enter choice"))
n1=int(input("enter no1"))
n2=int(input("enter no2"))
if choice==1:
    print(sum(n1,n2))
elif choice==2:
    print(diff(n1,n2))
else:
    print("invalid")
    
