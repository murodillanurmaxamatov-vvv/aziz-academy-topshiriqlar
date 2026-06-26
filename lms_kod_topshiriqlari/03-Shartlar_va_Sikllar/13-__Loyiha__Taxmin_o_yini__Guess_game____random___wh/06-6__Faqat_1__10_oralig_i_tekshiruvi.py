x = 6

while True:
    try:
        b = int(input())
    except:
        break
        
    if b < 1 or b > 10:
        print("Invalid")
        continue
        
    if b == x:
        print("Correct")
        break
        