w = input().split()

s = {i.lower() for i in w if i.lower() == i.lower()[::-1]}
if not s:
    print("BO'SH")
else:
    print(*sorted(s))