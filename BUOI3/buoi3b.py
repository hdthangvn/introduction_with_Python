a = 1
b = 10
while a < b:
    sum = 0
    i = 1
    while i < a:
        if a % i == 0:
            sum += i
        i += 1
    if sum == a:
        print(a)
    a += 1


