def g(k, d=None, **kwargs):
    return kwargs.get(k, d)

k = input()
n = int(input())

data = {}

for _ in range(n):
    x, v = input().split()
    data[x] = int(v)
    
print(g(k, d=0, **data))