def num(*args):
    return sum(args)

a = list(map(int, input().split()))

print(num(*a))