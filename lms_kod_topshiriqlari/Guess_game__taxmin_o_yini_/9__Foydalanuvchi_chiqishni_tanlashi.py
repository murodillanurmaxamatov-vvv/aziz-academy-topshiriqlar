yashirin = 3
while True:
    try:
        taxmin = int(input())
    except:
        break
    
    if taxmin == 0:
        print("Exit")
        break
    elif taxmin == yashirin:
        print("Correct")
        break
    else:
        print("Wrong")