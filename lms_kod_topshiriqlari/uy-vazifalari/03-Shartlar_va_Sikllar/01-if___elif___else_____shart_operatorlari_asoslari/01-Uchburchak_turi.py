a = int(input())
b = int(input())
v = int(input())

if a < b < v:
    print("turli tomonli")
elif a == b < v:
    print("teng yonli")
else:
    print("teng tomonli")