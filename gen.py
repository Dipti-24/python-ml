def gm(n):
    for i in range(n):
        yield i
g=gm(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
