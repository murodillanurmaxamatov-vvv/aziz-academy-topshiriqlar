n = int(input())



for i in range(1, n + 1):
    name, score = input().split()
    score = int(score)
    
    print(f"{i}|{name}|{score}")