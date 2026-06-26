def m(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    return x

x, lo, hi = map(int, input().split())

print(m(x, lo, hi))
print(m(lo=lo, hi=hi, x=x))