arr =  [9,3,5,6,4,8,7]
sum = 0
min = max = arr[0]
for i in arr:
    sum += i
print("average:",sum/len(arr))

for num in arr:
    if num < min:
        min = num
    if num > max:
        max = num

print("Min:",min)
print("Max:",max)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_arr(arr):
    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
    return primes

print("Số nguyên tố trong mảng:", find_primes_in_arr(arr))






