def i(a):
    if len(a) <= 1:
        return a
    
    return [a[-1]] + i(a[:-1])

a = list(map(int, input().split()))
print(*(i(a)))