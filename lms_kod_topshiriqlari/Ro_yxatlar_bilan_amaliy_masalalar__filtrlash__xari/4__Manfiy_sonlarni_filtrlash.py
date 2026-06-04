n = int(input())
son = list(map(int,input().split()))

m = []
for i in son:
    if i < 0:
        m.append(i)
print(m)
            