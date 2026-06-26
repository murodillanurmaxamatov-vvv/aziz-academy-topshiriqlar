n = int(input())

for _ in range(n):
    name, flag = input().split()
    
    status = "present" if flag == "1" else "absent"
    
    print(f"{name}|{status}")