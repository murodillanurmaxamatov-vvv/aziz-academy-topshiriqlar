x = list(map(int, input().split()))

a = [i for i in x if i % 2 != 0]

if a:
    print(*a)
else:
    print("BO'SH")