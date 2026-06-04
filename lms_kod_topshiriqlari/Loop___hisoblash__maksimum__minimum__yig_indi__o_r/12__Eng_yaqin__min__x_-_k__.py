n = int(input())
son = list(map(int,input().split()))
k = int(input())

yaqin = min(son, key=lambda x: (abs(x - k), x))
print(yaqin)