
print("hello world")

import sys

a = 1
print(type(a))
print(sys.getsizeof(a))

a = 100000000000000000000
print(sys.getsizeof(a))

a = 1000000000000000000000000000000
print(sys.getsizeof(a))

a = "Hoang Duc Thang"
print(a)
print(sys.getsizeof(a))

