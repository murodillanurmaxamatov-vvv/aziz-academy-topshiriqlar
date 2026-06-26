yashirin = 15

while True:
    try:
        taxmin = int(input())
    except:
        break
        
    if taxmin == yashirin :
        print("Correct")
        break
    elif abs(taxmin - yashirin) > 5:
        print("Far")
    else:
        print("Close")