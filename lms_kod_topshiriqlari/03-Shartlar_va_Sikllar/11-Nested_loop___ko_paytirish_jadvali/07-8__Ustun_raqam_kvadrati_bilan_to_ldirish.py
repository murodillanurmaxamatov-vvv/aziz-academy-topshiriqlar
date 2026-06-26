n, m = map(int,input().split())
print(" ".join(str(j*j) for j in range(2, m + 2)[:m-1]))