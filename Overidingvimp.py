class A:
    v1 = "im"
    def __init__(self):
        self.v2="yo"
        self.v1="ins"
        self.special="ssss"
class B(A):
    v="Imm"
    def __init__(self):
       # super().__init__()
        self.v2="pp"
        self.v1="ooo"
        super().__init__()
a=A()
b=B()
print(b.v2 ,b.special)