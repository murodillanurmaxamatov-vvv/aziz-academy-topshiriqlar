a = float(input())

if a >= 100:
    if a >= 500:
        discount = a * 0.20
    else:
        discount = a * 0.10
    final_a = a - discount
else:
    final_a = a
print(final_a)