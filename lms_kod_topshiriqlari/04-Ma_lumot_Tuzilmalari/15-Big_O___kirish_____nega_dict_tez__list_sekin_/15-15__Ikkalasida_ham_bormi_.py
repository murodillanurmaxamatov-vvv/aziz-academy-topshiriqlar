a = set(map(int, input().split()))
b = set(map(int, input().split()))
t = int(input())

if t in a and t in b:
    print("Ha")
else:
    print("Yo'q")