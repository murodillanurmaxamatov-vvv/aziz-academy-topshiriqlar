w = input().split()

t = len(w)

f = {}

for i in w:
    i = i.lower()
    f[i] = f.get(i, 0) + 1
    
u = len(f)

d = None
c = -1

for z, y in f.items():
    if y > c:
        d = z
        c = y
    elif y == c and z < d:
        d = z
        
print(f"total: {t}")
print(f"unique: {u}")
print(f"top: {d} {c}")