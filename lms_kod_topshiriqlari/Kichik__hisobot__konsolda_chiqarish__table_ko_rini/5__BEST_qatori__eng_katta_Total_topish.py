n = int(input())

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

p = ""
t = -1

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price
    
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
    if total > t or (total == t and  product < p):
        t = total
        p = product
        
print(f"BEST: {p} {t}")
        
          