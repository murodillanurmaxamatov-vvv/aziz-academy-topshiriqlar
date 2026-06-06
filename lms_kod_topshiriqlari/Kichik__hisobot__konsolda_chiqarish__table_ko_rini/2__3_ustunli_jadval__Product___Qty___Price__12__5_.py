n = int(input())

print(f"{'Product':12} | {'Qty':>5} | {'Price':>7}")
print("-" * 12 + "+" + "-" * 5 + "+" + '-' * 7)

for _ in range(n):
    product, qty, price = input().split()
    print(f"{product:<12} | {int(qty):>5} | {int(price): >7}")