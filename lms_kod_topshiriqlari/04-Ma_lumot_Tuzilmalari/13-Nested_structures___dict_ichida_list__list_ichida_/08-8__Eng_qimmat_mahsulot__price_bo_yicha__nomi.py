

n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

x = items[0]

for item in items:
    if item['price'] > x['price']:
        x = item
print(x['name'])