def c(x, lo=0, hi=100):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

s = list(map(int, input().split()))

if len(s) == 1:
    print(c(s[0]))
elif len(s) == 2:
    print(c(s[0], s[1]))
else:
    print(c(s[0], s[1], s[2]))