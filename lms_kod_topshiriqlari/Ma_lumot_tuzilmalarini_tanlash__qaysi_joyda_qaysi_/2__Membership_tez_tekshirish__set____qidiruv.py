n = int(input())
x = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    z = int(input())
    if z in x:
        print('YES')
    else:
        print('NO')