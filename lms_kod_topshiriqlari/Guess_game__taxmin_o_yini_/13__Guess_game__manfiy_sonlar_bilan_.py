yashirin = -4

for _ in range(2):
    taxmin = int(input())
    if taxmin == yashirin:
        print("Correct")
        break
    elif taxmin > yashirin:
        print("High")
    else:
        print("Low")