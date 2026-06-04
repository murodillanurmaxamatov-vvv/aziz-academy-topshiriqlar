n = int(input())
son = list(map(int,input().split()))

t = []
for i in son:
    if i % 2 != 0:
        t.append(i)
        
print(t)