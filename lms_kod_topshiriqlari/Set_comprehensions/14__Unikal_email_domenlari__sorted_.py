e = input().split()

s = {i.split('@')[1].lower() for i in e if '@' in i}
if not s:
    print("BO'SH")
else:
    print(*sorted(s))