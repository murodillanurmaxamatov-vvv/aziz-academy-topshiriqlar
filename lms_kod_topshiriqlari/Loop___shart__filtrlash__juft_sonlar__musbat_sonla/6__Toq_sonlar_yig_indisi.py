n = int(input())
son = list(map(int,input().split()))
qosh = 0
for i in son:
    if i % 2 != 0:
        qosh += i
print(qosh)