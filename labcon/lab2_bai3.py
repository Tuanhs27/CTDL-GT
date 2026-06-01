import time
import random

def merge_sort(arr):
    """
    Sắp xếp mảng bằng Merge Sort
    Độ phức tạp: O(n log n)
    """
# Base case: mảng 0 hoặc 1 phần tử
    if len(arr) <= 1:
        return arr

    # TODO: Divide - chia đôi mảng
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

# TODO: Conquer - đệ quy sắp xếp 2 nửa

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # TODO: Combine - trộn 2 nửa đã sắp xếp
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Trộn 2 mảng đã sắp xếp thành 1 mảng sắp xếp
    """
    result = []
    i = j = 0
# TODO: So sánh và chọn phần tử nhỏ hơn
# while i < len(left) and j < len(right):
# if left[i] <= right[j]:
# ...
# else:
# ...

# TODO: Thêm các phần tử còn lại
# result.extend(...)

    return result

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)

print(f"Mảng sau khi sắp xếp: {sorted_arr}")
# Kết quả: [11, 12, 22, 25, 34, 64, 90]


# Tạo mảng ngẫu nhiên
arr_small = [random.randint(1, 1000) for _ in range(100)]
arr_large = [random.randint(1, 10000) for _ in range(5000)]

# Đo thời gian với mảng nhỏ
start = time.time()
sorted_small = merge_sort(arr_small.copy()) # hoặc quick_sort
time_small = time.time() - start
print(f"Thời gian sắp xếp 100 phần tử: {time_small:.6f}s")

# Đo thời gian với mảng lớn
start = time.time()
sorted_large = merge_sort(arr_large.copy())
time_large = time.time() - start
print(f"Thời gian sắp xếp 5000 phần tử: {time_large:.6f}s")

start = time.time()
sorted_builtin = sorted(arr_large)
time_builtin = time.time() - start
print(f"Thời gian Python sorted(): {time_builtin:.6f}s")