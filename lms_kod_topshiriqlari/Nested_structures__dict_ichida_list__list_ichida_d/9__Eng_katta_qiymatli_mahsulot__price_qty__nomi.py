
n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

x = items[0]
v = x['price'] * x['qty']

for item in items:
    value = item['price'] * item['qty']
    if value > v:
        v = value
        x = item
        
print(x['name'])
