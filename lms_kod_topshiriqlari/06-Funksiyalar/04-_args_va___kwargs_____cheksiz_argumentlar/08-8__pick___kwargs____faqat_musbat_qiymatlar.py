def p(**kwargs):
    d = {}
    for k, v in kwargs.items():
        if v > 0:
            d[k] = v
    return d

n = int(input())
data = {}

for _ in range(n):
    x, y = input().split()
    data[x] = int(y)
    
print(p(**data))