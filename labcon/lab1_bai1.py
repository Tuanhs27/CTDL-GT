def snippet_1(n):
    total = 0 
    for i in range(n): 
        total = total + 1
    return total
# Độ phức tạp: O(n)
# Giải thích: vòng for chạy n lần, mỗi lần chỉ có 1 phép gán/cộng.

def snippet_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
# Độ phức tạp: O(n^2)
# Giải thích: có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước.

def snippet_3(n):
    steps = 0
    while n > 0:
        n = n // 2
        steps += 1
    return steps
# Độ phức tạp: O(log n)
# Giải thích: mỗi vòng while chia n cho 2, nên số vòng ≈ số lần chia đôi n về 1 là log2(n).

def constant_work():
    x = 1
    y = 2
    z = x + y
    return z
def snippet_4(n):
    for i in range(n):
        constant_work()
# Độ phức tạp: O(n)
# Giải thích: vòng for chạy n lần, mỗi lần gọi hàm O(1), nên tổng thời gian tỉ lệ tuyến tính với n.