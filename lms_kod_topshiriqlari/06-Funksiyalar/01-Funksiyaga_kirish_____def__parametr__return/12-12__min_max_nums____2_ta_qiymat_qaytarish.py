def son(a):
    return (min(a), max(a))

a = list(map(int, input().split()))
x, c = son(a)
print(x)
print(c)
