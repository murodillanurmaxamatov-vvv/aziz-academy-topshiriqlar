def s(**kwargs):
    return sum(kwargs.values())

n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
    
print(s(**d))