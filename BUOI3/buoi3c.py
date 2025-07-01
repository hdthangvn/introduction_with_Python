n = 6
i = 1

while i <= n:
    if i % 2 == 1:
        j = (i - 1) * n + 1
        s = ""
        while j <= i * n:
            s += str(j) + " "
            j += 1
        print(s)
    else:
        j = i * n
        s = ""
        while j >= (i - 1) * n + 1:
            s += str(j) + " "
            j -= 1
        print(s)
    i += 1