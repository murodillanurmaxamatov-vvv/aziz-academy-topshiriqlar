n = list(map(int, input().split()))

if not n:
    print(0)
else:
    a = sum(n) / len(n)
    print(int(a) if a.is_integer() else a)
 