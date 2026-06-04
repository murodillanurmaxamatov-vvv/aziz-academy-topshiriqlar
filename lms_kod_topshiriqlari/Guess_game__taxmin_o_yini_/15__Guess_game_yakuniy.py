yashirin = 20
count = 0
while True:
    taxmin = int(input())
    count += 1
    
    if taxmin == yashirin:
        print("Correct")
        break
    elif taxmin > yashirin:
        print("Invalid")
    else:
        print("Low")
print(count)