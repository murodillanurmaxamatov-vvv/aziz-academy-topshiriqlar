a = input().split()

x = [i for i in a if len(i) >= 5]
if x:
    print(*x)
else:
    print("BO'SH")