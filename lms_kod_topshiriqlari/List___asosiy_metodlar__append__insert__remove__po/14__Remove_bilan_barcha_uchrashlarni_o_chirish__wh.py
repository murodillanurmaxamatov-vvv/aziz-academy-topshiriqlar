n = int(input())
lst = list(map(int,input().split()))
x = int(input())

lst = [i for i in lst if i != x]

print(lst)