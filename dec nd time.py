def a(func):
    def b():
        print("Executing")
        func()
        print("Executed")
    return b
@ a
def who_is_dipti():
    print("uu")
who_is_dipti()
    
import time
for i in range(4):
    print("this")
a=time.time()
print(a)