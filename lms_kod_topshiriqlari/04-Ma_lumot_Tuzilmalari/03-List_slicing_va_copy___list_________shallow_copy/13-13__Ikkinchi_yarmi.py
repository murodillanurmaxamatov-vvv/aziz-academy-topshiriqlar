n = int(input())
son = list(map(int,input().split()))

if n % 2 == 0:
    print(son[n//2:])
else:
    print(son[n // 2 + 1:])
