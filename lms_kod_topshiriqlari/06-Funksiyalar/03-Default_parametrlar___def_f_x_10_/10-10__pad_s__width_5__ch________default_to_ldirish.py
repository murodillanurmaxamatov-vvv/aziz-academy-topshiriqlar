def x(s, c=5, ch='.'):
    if len(s) >= c:
        return s
    return s + ch * (c - len(s))

s = input()
t = input().split()

if len(t) == 0:
    print(x(s))
elif len(t) == 1:
    print(x(s, int(t[0])))
else:
    print(x(s, int(t[0]), t[1]))