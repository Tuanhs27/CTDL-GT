#Hàm 1 – Tính tổng từ 1 đến n
def sum_to_n(n):
#Tính tổng 1 + 2 + ... + n bằng đệ quy
# Base case: n = 0 hoặc n = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
# Recursive case: n + sum(1..n-1)
    return n + sum_to_n(n - 1)
print(sum_to_n(5)) 
print(sum_to_n(10)) 
# Độ phức tạp: O(n)
# Giải thích: Hàm gọi đệ quy n lần, mỗi lần thực hiện 1 phép cộng

#Hàm 2 – Tính n mũ k (power)
def power(n, k):
#Tính n^k bằng đệ quy
# Base case 1: mũ 0
    if k == 0:
        return 1

    # Base case 2: cơ số 0
    if n == 0:
        return 0

    # Recursive case: n × n^(k-1)
    return n * power(n, k - 1)
print(power(2, 5))
print(power(3, 4)) 
print(power(5, 0)) 
# Độ phức tạp: O(k)
# Giải thích: Hàm gọi đệ quy k lần

#Hàm 3 – Đảo chuỗi (reverse string)
def reverse_string(s):
#Đảo ngược chuỗi bằng đệ quy
# Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return s
    # Recursive case: đảo phần còn lại + ký tự đầu
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello")) # Kết quả: "olleh"
print(reverse_string("python")) # Kết quả: "nohtyp"
print(reverse_string("a")) # Kết quả: "a"
print(reverse_string("")) # Kết quả: ""
# Độ phức tạp: O(n)
# Giải thích: n lần gọi đệ quy với n = len(s)

#Hàm 4 – Kiểm tra palindrome (đọc xuôi ngược như nhau)
def is_palindrome(s):
#Kiểm tra chuỗi có phải palindrome bằng đệ quy
# Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return True
    # So sánh ký tự đầu và cuối
    if s[0] != s[-1]:
        return False
# Recursive case: kiểm tra phần giữa
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar")) # True
print(is_palindrome("madam")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("a")) # True
print(is_palindrome("")) # True
# Độ phức tạp: O(n)
# Giải thích: Tối đa n/2 lần so sánh, vẫn là O(n)