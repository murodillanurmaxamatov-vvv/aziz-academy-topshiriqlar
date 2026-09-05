a = list(map(int, input().split()))
if len(a) != len(set(a)):
    print("bor")
else:
    print("yo'q")