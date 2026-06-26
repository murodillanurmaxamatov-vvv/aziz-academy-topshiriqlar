n = int(input())

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

r = []
g = 0
s = 0

for _ in range(n):
    p, q, pr = input().split()
    q = int(q)
    pr = int(pr)
    total = q * pr
    
    r.append((p, q, pr, total))
    
    g += total
    s += pr
    
    print(f"{p:<12} | {q:>5} | {pr:>7} | {total:>9}")
    
    
b, t, e, l = min(r, key=lambda x: (-x[3], x[0]))

avg = s / n

print(f"BEST: {b} {l}")
print(f"GRAND: {g}")
print(f"AVG_PRICE: {avg:.2f}")