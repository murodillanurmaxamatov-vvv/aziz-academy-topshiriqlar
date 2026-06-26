n = int(input())
son = list(map(int,input().split()))
maks = son[0]
for i in range(1, n):
    if son[i] > maks:
        maks = son[i]
print(maks)
