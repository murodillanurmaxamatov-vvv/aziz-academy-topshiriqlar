a = list(map(int, input().split()))

x = [i for i in a if i % 2 == 0]

if x:
    print(*x)
else:
    print("BO'SH")