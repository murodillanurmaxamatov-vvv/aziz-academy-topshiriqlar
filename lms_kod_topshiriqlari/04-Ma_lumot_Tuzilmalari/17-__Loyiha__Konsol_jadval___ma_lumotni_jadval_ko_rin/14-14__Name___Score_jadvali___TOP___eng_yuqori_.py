n = int(input())

data = []

for _ in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))
    

print(f"{'Name':<10} | {'Score':>5}")
print('-'*10 + "+" + "-"*5)

for name, score in data:
    print(f"{name:<10} | {score:>5}")
    
n, s = min(data, key=lambda x: (-x[1], x[0]))

print(f"TOP: {n} {s}")
    