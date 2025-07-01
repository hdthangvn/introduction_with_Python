def greet(name):
    print("hello", name)
    if name == "Thang":
        return 100

    return "failed"

def Greet(name):
    print("hello", name)

a = greet("Thang")
print(a)
a = greet("else")
print(a)


