son = 8
harakat = 3
for b in range(harakat):
    a = int(input())
    
    if a == son:
        print("Correct")
        break
else:
    print("Game Over")