n = list(map(int, input().split()))

s = {x for x in n if x % 2 == 0}

if not s:
    print("BO'SH")
else:
    print(*sorted(s))