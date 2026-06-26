n = int(input())
son = list(map(int,input().split()))
yigindi = 0
for i in son:
    if i % 2 == 0:
        yigindi += i
print(yigindi)