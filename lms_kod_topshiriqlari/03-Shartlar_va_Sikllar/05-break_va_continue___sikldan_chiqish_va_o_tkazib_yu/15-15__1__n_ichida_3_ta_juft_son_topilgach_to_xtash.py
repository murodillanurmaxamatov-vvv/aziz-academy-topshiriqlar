n = int(input())
juft = 0
i = 1
while i <= n:
    if i % 2 == 0:
        juft += 1
        if juft == 3:
            print(i)
            break
    i += 1
    
if juft < 3:
    print("No")