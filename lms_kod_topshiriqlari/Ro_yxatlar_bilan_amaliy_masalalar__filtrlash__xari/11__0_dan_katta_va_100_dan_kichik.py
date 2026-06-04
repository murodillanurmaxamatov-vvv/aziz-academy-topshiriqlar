n = int(input())
son = list(map(int,input().split()))

l = []
for i in son:
    if 0 < i < 100:
        l.append(i)
        
print(l)