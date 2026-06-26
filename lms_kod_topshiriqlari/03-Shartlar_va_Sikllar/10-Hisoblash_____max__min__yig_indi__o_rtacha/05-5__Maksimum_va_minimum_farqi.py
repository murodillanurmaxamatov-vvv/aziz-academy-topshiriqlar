n = int(input())
son = list(map(int,input().split()))
maks = son[0]
m = son[0]
for i in son:
    if i > maks:
        maks = i
    if i < m:
        m = i
natija = maks - m
print(natija)