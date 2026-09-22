def i(a):
    if not a:
        return 0
    return a[0] + i(a[1::])

e = list(map(int, input().split()))
print(i(e))