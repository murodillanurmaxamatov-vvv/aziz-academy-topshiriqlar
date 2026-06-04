a = input().split()

x = [i for i in a if i.isalpha()]

if x:
    print(*x)
else:
    print("BO'SH")