n = int(input())
son = list(map(int,input().split()))
for i in range(n):
    if son[i] % 2 == 0:
        print(son[i])