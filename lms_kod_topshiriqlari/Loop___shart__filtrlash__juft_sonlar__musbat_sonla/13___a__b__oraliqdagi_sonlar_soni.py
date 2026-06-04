n = int(input())
son = list(map(int,input().split()))
a, b = map(int,input().split())
count = 0
for i in son:
    if a <= i <= b:
        count += 1
print(count)