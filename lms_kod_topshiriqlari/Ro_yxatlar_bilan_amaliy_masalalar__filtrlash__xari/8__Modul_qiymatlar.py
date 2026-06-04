n = int(input())
son = list(map(int,input().split()))

m = []

for i in son:
    m.append(abs(i))
    
print(m)