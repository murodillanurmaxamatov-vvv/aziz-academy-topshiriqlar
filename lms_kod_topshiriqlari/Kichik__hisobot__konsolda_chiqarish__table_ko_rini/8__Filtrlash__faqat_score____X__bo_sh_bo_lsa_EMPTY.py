n = int(input())

data = []

for _ in range(n):
    name, score = input().split()
    data.append((name, int(score)))
    
x = int(input())


a = [(name, score) for name, score in data if  score >= x]

if not a:
    print("EMPTY")
else:
    for name, score in a:
        print(f"{name}={score}")