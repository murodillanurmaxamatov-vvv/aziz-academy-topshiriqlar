n = int(input())

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

grand = 0

r = []

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price
    grand += total
    
    r.append((product, qty, price, total))
    
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
print("------------+-----+-------+---------")

print(f"{'SUM':<12} | {'':>5} | {'':>7} | {grand:>9}")