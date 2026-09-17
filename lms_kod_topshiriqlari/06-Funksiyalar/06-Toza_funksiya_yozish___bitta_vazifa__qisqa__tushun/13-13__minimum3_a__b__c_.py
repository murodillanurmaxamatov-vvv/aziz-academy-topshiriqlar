def gap(a, s, d):
    return min(a, s, d)

a, s, d = map(int, input().split())
print(gap(a, s, d))