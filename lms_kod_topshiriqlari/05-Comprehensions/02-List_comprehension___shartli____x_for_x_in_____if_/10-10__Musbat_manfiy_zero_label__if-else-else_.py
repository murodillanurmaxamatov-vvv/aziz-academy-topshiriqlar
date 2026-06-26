x = list(map(int,input().split()))

a = ['pos' if i > 0 else 'neg' if i < 0 else 'zero' for i in x]

print(*a)