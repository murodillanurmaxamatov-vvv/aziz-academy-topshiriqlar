x = list(map(int,input().split()))

m = sum(x) / len(x)

r = [(i - m) for i in x]
print(" ".join(f"{i:.2f}" for i in r))