A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))

res = sorted((A - B - C) | (B - A - C) | (C - A - B))

if len(res) == 0:
    print("BO'SH")
else:
    print(*res)
