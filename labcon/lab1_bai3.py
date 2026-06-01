def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
# Độ phức tạp: O(n^2) 
# Giải thích: Thuật toán sử dụng 2 vòng lặp lồng nhau 

def two_sum_linear(arr, target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i
    return None
# Độ phức tạp: O(n)
# Giải thích: Chỉ sử dụng một vòng lặp duy nhất chạy n lần.

import time
import random
arr = list(range(10000))
random.shuffle(arr)
target = arr[100] + arr[500]
start = time.time()
two_sum_quadratic(arr, target)
print(f"Thời gian O(n^2): {time.time() - start:.4f} giây")
start = time.time()
two_sum_linear(arr, target)
print(f"Thời gian O(n): {time.time() - start:.4f} giây")