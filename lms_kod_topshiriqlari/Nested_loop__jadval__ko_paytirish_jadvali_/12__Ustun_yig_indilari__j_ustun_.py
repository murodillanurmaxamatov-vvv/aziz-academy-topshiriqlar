n, m = map(int,input().split())
for j in range(1,m + 1):
    col_sum = 0
    for i in range(1, n + 1):
        col_sum += i * j
    print(col_sum)