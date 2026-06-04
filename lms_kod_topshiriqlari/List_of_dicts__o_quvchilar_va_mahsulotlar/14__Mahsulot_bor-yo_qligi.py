n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
if any(p['name'] == x for p in products):
    print('YES')
else:
    print("NO")
