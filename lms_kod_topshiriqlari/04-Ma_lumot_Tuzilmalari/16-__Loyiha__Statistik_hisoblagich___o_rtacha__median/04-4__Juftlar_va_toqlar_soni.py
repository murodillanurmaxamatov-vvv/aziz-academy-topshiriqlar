x = list(map(int,input().split()))

juft = 0
toq = 0

for i in x:
    if i % 2 == 0:
        juft += 1
    else:
        toq += 1
        
print(juft)
print(toq)