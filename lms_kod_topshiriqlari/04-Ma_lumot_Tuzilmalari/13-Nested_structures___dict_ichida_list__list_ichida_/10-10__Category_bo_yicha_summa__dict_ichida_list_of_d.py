n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

totals = {}

for item in items:
    cat = item['cat']
    value = item['price'] * item['qty']
    
    if cat not in totals:
        totals[cat] = 0
        
    totals[cat] += value
    
for cat in sorted(totals.keys()):
    print(cat, totals[cat])
