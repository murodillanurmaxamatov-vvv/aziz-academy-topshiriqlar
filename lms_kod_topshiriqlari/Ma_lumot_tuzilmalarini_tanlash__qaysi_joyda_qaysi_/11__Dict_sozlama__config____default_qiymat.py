k = int(input())

c = {}

for _ in range(k):
    key, value = input().split()
    c[key] = int(value)
    
q = int(input())

for _ in range(q):
    key = input().strip()
    print(c.get(key, 0))