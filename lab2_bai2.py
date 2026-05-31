def fibonacci_naive(n):
    """
    Fibonacci đệ quy đơn giản - CHẬM
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# Test
print("Fibonacci naive:")
print(fibonacci_naive(10)) # 55
print(fibonacci_naive(20)) # 6765 (chậm rồi)
# print(fibonacci_naive(35)) # Rất chậm! Mất vài giây
# Độ phức tạp: O(2^n) - rất chậm

def fibonacci_memo(n, memo=None):
    """
    Fibonacci với memoization - NHANH
    """
    # Khởi tạo memo nếu chưa có
    if memo is None:
        memo = {}
    # TODO: Kiểm tra n đã có trong memo chưa
    # Nếu có → trả về ngay memo[n]
    if n in memo:
        return memo[n]
    # TODO: Base case
    # Nếu n <= 1 → lưu vào memo và trả về
    if n <= 1:
        memo[n] = n
        return n
    # TODO: Recursive case
    # Tính fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# TODO: Recursive case
# Tính fibonacci_memo(n-1) + fibonacci_memo(n-2)
# Lưu kết quả vào memo[n]
# Trả về memo[n]

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    # Kiểm tra memo
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        memo[n] = n
    return memo[n]

# Recursive case: sinh viên tự viết
# memo[n] = ...
# return memo[n]

import time

# Test với n = 35
print("\n--- So sánh hiệu suất ---")

start = time.time()
result1 = fibonacci_naive(30) # Chỉ test n=30 vì 35 quá chậm
time1 = time.time() - start
print(f"Naive F(30) = {result1}, thời gian: {time1:.4f}s")

start = time.time()
result2 = fibonacci_memo(100) # Có thể test với 100!
time2 = time.time() - start
print(f"Memo F(100) = {result2}, thời gian: {time2:.6f}s")