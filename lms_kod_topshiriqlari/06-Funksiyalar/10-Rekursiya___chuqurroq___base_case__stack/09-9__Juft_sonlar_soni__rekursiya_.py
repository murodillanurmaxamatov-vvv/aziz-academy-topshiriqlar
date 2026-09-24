def s(a):
    if len(a) == 0:
        return 0
    
    i = 1 if a[0] % 2 == 0 else 0
    
    return i + s(a[1:])

a = list(map(int, input().split()))
print(s(a))