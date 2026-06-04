n = int(input())

z = [str(i) for i in range(1, n + 1) if i % 3 == 0]

print(*z if z else ["BO'SH"])