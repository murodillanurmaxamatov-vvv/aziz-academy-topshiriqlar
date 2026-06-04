x = list(map(int,input().split()))

a = ['even' if n % 2 == 0 else 'odd' for n in x]

print(*a)