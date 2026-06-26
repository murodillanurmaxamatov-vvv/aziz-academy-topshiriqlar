n = int(input())
son = list(map(int,input().split()))
m = son[0]
for i in range(1, n):
    if son[i] < m:
        m = son[i]
print(m)