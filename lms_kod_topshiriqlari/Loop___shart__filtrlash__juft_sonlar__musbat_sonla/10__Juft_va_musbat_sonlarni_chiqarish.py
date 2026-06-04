n = int(input())
son = list(map(int,input().split()))
for i in son:
    if i > 0 and i % 2 == 0:
        print(i)