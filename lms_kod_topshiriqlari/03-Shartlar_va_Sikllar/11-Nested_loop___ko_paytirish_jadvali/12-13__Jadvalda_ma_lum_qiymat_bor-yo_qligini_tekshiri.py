n, m = map(int,input().split())
x = int(input())
found = False
for i in range(1, n + 1):
    if x % i == 0:
        j = x // i
        if 1 <= j <= m:
            found = True
            break
if found:
    print("Yes")
else:
    print("No")