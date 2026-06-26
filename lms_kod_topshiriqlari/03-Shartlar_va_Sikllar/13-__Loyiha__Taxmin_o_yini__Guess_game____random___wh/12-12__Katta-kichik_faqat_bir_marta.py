yashirin = 8
birinchi = True
while True:
    try:
        taxmin = int(input())
    except:
        break
    
    if birinchi:
        print("Low")
        birinchi = False
        continue
    
    if taxmin == yashirin :
        print("Correct")
        break
    else:
        print("Wrong")