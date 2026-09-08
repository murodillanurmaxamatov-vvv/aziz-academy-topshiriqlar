n = input()
s = list(map(int, input().split()))

d = {n: s}
print(sum(d[n]))