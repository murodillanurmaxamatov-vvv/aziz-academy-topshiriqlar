yashirin = 1
count = 0
while True:
    try:
        taxmin = int(input())
    except:
        break
        
    count += 1
    
    if taxmin == yashirin :
        print("Correct")
        print(count)
        break
    else:
        print("Try again")