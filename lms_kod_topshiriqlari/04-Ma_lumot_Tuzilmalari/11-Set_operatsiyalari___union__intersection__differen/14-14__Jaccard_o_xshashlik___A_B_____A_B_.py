A = set(map(int, input().split()))
B = set(map(int, input().split()))

inter = len(A & B)
uni = len(A | B)

res = inter / uni

print("{:.3f}".format(res))