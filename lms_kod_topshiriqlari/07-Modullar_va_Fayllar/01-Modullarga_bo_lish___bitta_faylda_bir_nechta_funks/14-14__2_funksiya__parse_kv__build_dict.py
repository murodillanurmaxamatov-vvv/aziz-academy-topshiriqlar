def pa(l):
    k, v = l.split("=")
    return (k, int(v))

def buld(p):
    d = {}
    for k, v in p:
        d[k] = v
    return d

n = int(input())
p = []
for _ in range(n):
    p.append(pa(input()))
print(buld(p))