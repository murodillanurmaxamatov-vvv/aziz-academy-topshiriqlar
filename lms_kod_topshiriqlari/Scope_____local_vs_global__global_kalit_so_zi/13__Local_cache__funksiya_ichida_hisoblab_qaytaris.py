def s(n):
    r = []
    for i in range(1, n + 1):
        r.append(i * i)
    return r    
    
n = int(input())

l = s(n)
print(*l)