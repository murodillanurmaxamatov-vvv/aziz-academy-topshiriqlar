n = int(input())

print(f"{'Key':<12} | {'Value':>12}")
print("-"*12 + '+' + '-'*12)

for _ in range(n):
    key, value = input().split()
    value = int(value)
    print(f"{key:<12} | {value:>11}")