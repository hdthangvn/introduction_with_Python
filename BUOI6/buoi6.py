s = "hello world"
s2 = "HELLO WORLD"
s3 = "Hello Python Programming"

# 1. islower()
print(s.islower())       # True - vì tất cả ký tự đều viết thường
print(s2.islower())      # False - vì có chữ viết hoa

# 2. lower()
print(s2.lower())        # "hello world" - chuyển toàn bộ thành chữ thường

# 3. upper()
print(s.upper())         # "HELLO WORLD" - chuyển thành chữ hoa

# 4. split(separator)
print(s3.split())        # ['Hello', 'Python', 'Programming'] - mặc định tách bằng dấu cách
print(s3.split("o"))     # ['Hell', ' Pyth', 'n Pr', 'gramming'] - tách theo ký tự 'o'

# 5. find(string)
print(s.find("world"))   # 6 - vị trí bắt đầu của "world"
print(s.find("Python"))  # -1 - không tìm thấy

# 6. endswith(string)
print(s.endswith("world"))  # True - chuỗi kết thúc bằng "world"
print(s.endswith("hello"))  # False - không kết thúc bằng "hello"

# 7. replace(old_value, new_value)
print(s.replace("hello", "hi"))        # "hi world" - thay "hello" bằng "hi"
print(s3.replace("Python", "Java"))    # "Hello Java Programming"
