n = int(input())
son = list(map(int,input().split()))
count = 0
for i in son:
    if i % 3 == 0:
        count += 1
print(count)