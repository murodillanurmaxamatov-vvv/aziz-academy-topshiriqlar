yashirin = 9

while True:
    try:
        taxmin = int(input())
    except:
        break
    if taxmin == yashirin:
        print("Correct")
        break
    else:
        print("Low")
    