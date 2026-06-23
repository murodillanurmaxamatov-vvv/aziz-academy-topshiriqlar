def s(f, *args):
    return [f * x for x in args]

f = int(input())
a = list(map(int, input().split()))

print(*s(f, *a))