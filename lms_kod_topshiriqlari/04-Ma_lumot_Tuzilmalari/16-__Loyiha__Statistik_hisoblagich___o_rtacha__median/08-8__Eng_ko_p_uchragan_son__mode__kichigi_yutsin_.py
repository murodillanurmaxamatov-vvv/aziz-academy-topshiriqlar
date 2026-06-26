x = list(map(int, input().split()))

c = {}

for i in x:
    c[i] = c.get(i, 0) + 1
z = max(c.values())

a = []
for key, val in c.items():
    if val == z:
        a.append(key)
        
print(min(a))