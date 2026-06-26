
n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
a = min(products, key=lambda p: p['price'])
print(a['name'])
