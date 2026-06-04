n = int(input())
son = list(map(int,input().split()))

juft = []

for i in son:
    if i % 2 == 0:
        juft.append(i)
  
print(juft)