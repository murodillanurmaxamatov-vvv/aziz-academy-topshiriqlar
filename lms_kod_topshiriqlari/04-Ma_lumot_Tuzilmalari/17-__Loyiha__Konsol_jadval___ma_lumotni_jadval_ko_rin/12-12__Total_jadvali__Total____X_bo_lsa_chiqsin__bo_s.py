n = int(input())

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

r = []
g = 0

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price
    r.append((product, qty, price, total))
    
x = int(input())

printed = False

for product, qty, price, total in r:
    if total >= x:
        print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
        printed = True
        
if not printed:
    print("EMPTY")