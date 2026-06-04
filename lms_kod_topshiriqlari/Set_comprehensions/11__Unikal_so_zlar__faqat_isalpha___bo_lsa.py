t = input().split()

s = {i.lower() for i in  t if i.isalpha()}
if not s:
    print("BO'SH")
else:
    print(*sorted(s))