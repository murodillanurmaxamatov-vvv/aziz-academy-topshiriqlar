n = int(input())

d = {}

for i in range(n):
    k, v = input().split()
    v = int(v)
    
    if abs(v) >= 2:
        if v % 2 == 0:
            d[k] = v * 2
        else:
            d[k] = v * 3
            
print(d)