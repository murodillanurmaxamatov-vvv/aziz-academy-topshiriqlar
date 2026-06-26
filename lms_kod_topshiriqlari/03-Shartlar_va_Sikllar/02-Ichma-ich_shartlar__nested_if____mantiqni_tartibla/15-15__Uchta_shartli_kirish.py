x = input()
a, b = x.split()
if a == "admin":
    print("Admin active")
elif b == 1:
    print("Admin inactive")
else:
    print("User")