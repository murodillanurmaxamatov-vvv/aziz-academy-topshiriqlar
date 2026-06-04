n = int(input())
son = list(map(int,input().split()))

l = []
for i in son:
    if i % 2 == 0:
        l.append(i * 10)
print(l)