n = int(input())

print(f"{'Name':<10} | {'Score':>5}")
print("-" * 10 + "+" + "-" * 5)

for _ in range(n):
    name, score = input().split()
    print(f"{name:<10} | {int(score):>5}")