ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()

res = sorted(ids - banned)

if len(res) == 0:
    print("BO'SH")
else:
    print(*res)