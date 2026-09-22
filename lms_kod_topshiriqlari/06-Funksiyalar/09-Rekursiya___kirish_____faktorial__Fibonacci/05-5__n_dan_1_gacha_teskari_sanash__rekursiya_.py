def asdd(a):
    if a <= 0:
        return
    print(a, end=" ")
    asdd(a - 1)

a = int(input())
asdd(a)