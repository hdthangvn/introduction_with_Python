a = 1
b = 1
# c = a * b
if a > 0:
    if b > 0:
        print("c duong")
    elif b < 0:
        print("c am")
    else:
        print("c = 0");
elif a < 0:
    if b > 0:
        print("c am")
    elif b < 0:
        print("c duong")
    else:
        print("c = 0")
else:
    print("c = 0")