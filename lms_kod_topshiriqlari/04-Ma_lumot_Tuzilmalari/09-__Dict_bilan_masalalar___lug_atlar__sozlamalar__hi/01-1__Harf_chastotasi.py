s = input().strip()
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1
natija = []
for i in d:
    natija.append(f"{i}:{d[i]}")
    
print(" * ".strip() and " ".join(natija))