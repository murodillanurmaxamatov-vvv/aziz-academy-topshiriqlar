def t(s, r=0, e=None):
    return s[r:e]

s = input()
x = input().split()

if len(x) == 0:
    print(t(s))
elif len(x) == 1:
    print(t(s, int(x[0])))
else:
    print(t(s, int(x[0]), int(x[1])))