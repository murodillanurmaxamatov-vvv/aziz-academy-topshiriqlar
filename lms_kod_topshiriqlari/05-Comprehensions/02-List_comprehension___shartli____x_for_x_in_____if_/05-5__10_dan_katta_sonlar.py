a = list(map(int, input().split()))

x = [i for i in a if i > 10]

if x:
    print(*x)
else:
    print("BO'SH")