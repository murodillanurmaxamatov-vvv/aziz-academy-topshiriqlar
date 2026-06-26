n = int(input())
yigindi = 0
i = 1
while i <= n:
    if i % 2 != 0:
        yigindi += i
    i += 1
print(yigindi)