def r(p='', **kwargs):
    return {p + k: v for k, v in kwargs.items()}

p = input()
n = int(input())

d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)
    
print(r(p=p, **d))