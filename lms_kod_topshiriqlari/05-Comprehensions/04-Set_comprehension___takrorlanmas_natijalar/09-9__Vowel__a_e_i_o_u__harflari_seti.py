s = {i.lower() for i in input() if i.lower() in "aeiou"}
if not s:
    print("BO'SH")
else:
    print(*sorted(s))