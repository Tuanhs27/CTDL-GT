def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
# Độ phức tạp: O(n^2)
# Giải thích: vòng j chạy n lần , Khi i = 1 → chạy 1 lần, i = 2 → 2 lần, ..., i = n-1 → n-1 lần. Tổng số lần lặp là 0 + 1 + 2 + ... + (n-1) = n(n-1)/2.

def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
            k = k * 2
    return total
# Độ phức tạp:O(n log n)
# Giải thích: vòng for bên trong chạy n lần , mỗi lần nhân k với 2 → số lần lặp của while

def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr: 
            count += 1
    return count
# Độ phức tạp:O(n^2)
# Giải thích:Vòng for chạy n lần , mỗi lần, phép x in arr phải duyệt cả list

def snippet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count
# Độ phức tạp:O(n)
# Giải thích: số phần tử = n → O(n) vòng for chạy n lần, mỗi lần x in s là O(1) trung bình, tổng thời gian: O(n) + n × O(1).