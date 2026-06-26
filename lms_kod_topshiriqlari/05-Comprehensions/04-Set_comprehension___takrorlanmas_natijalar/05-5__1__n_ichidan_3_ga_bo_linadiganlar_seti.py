n = int(input())

s = {x for x in range(1, n + 1) if x % 3 == 0}

if not s:
    print("BO'SH")
else:
    print(*sorted(s))