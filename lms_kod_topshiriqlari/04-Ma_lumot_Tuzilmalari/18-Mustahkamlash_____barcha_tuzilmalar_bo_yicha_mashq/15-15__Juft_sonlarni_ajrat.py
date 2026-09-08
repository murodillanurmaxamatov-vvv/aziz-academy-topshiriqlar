v = list(map(int, input().split()))
q = [x for x in v if x % 2 == 0]

if q:
    print(*q)
else:
    print("yo'q")