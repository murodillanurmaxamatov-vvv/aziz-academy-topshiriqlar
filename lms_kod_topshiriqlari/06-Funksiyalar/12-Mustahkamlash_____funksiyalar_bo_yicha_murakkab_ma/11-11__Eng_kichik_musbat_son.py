a = list(map(int, input().split()))
p = [x for x in a if x > 0]
print(min(p))