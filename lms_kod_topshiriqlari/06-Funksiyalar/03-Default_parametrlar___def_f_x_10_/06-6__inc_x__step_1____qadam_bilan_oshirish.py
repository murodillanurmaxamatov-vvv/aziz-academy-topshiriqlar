def son(x, s=1):
    return x + s

c = list(map(int, input().split()))

if len(c) == 1:
    print(son(c[0]))
else:
    print(son(c[0], c[1]))