n = 6
i = 1
while i <= n:
    s = ""
    j = 1
    while j <= n - i:
        s += " "
        j += 1
    j = 1
    while j <= i * 2 - 1:
        s += "*"
        j += 1

    print(s)
    i += 1

