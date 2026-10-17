def add(a, b):
    return a + b
def mul(a, b):
    return a * b
ops = {"add": add, "mul": mul}
a, b = map(int, input().split())
print(ops["add"](a, b))
print(ops["mul"](a, b))