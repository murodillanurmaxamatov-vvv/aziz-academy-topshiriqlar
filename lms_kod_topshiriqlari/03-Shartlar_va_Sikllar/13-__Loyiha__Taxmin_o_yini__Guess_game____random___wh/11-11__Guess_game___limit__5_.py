yashirin = 10
urunish = 5
for i in range(urunish):
    try:
        taxmin = int(input())
    except:
        break
    
    if taxmin  == yashirin :
        print("Correct")
        break
else:
    print("You lost")
       