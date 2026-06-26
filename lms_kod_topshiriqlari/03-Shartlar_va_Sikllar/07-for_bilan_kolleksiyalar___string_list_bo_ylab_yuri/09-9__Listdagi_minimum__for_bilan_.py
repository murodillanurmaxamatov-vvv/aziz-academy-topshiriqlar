n = int(input())
son = list(map(int,input().split()))
k = son[0]
for i in range(1,n):
    if son[i] < k:
        k = son[i]
print(k)
