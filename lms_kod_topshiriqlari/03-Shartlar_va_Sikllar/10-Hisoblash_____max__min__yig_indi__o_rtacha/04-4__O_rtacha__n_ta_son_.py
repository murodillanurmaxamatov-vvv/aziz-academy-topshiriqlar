n = int(input())
son = list(map(int,input().split()))
yigindi = 0
count = 0
for i in son:
    yigindi += i
    count += 1
orta = yigindi / count
print(orta)