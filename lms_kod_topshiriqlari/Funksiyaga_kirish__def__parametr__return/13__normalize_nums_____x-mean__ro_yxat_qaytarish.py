def n(a):
    mean = sum(a) / len(a)
    return [x - mean for x in a]

a = list(map(int, input().split()))

r = n(a)
print(*[f"{x:.2f}" for x in r])