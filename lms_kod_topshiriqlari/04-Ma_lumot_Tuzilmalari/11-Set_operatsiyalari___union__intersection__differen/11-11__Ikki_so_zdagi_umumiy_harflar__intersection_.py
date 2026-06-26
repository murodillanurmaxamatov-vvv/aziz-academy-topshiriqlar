a = input().strip()
b = input().strip()

c = sorted(set(a) & set(b))

if len(c) == 0:
    print("BO'SH")
else:
    print("".join(c))