s = {i for i in input() if i.isdigit()}

if not s:
    print("BO'SH")
else:
    print(*sorted(s))