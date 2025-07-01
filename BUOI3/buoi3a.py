a = 1234
sum = 0
while a > 0:
    sum += a % 10
    a = int(a / 10)

print(sum)