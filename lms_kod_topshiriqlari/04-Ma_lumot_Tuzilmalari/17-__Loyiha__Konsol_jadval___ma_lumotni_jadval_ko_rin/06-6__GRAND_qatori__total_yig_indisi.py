n = int(input())

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

grand = 0

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    
    total = qty * price
    grand += total
    
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
print("GRAND:", grand)