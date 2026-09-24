def mm(a):
    if len(a) == 1:
        return a[0]
    s = mm(a[1:])
    
    if a[0] > s:
        return a[0]
    else:
        return s
    
a = list(map(int, input().split()))
print(mm(a))