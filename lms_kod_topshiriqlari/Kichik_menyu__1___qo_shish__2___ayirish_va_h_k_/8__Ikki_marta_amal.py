for i in range(2):
    a, b  = map(int,input().split())
    tanlov = int(input())
    
    if  tanlov == 1:
        print(a + b) 
    elif tanlov == 2:
        print(a - b)
else:
     print("Exit")