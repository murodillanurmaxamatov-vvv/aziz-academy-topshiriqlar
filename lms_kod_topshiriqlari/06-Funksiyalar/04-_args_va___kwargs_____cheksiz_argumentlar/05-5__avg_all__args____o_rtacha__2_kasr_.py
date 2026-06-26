def son(*args):
    return sum(*args) / len(*args)

a = list(map(int, input().split()))
print(f"{son(a):.2f}")