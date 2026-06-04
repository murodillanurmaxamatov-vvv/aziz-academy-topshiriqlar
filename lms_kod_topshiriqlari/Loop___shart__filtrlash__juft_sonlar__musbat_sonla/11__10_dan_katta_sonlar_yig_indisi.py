n = int(input())
son = list(map(int,input().split()))
yigindi = 0
for i in son:
    if i > 10:
        yigindi += i
print(yigindi)
            