def permutations(nums):
    """
    Tìm tất cả hoán vị của nums
    """
    result = []

    def backtrack(path, remaining):
        # Base case: Đã chọn đủ n số
        if len(path) == len(nums):
            result.append(path.copy()) # QUAN TRỌNG: phải copy!
            return  # SỬA Ở ĐÂY: Thụt lề vào TRONG lệnh if

        # Thử từng số còn lại
        # SỬA Ở ĐÂY: Toàn bộ vòng lặp này phải thụt lề vào TRONG hàm backtrack
        for i in range(len(remaining)):
            # CHOOSE: Chọn remaining[i]
            path.append(remaining[i])

            # EXPLORE: Đệ quy với các số còn lại (bỏ số vừa chọn)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)

            # UNCHOOSE: Quay lui
            path.pop()

    # Gọi hàm đệ quy lần đầu tiên
    backtrack([], nums)
    return result

# Test
print("=== Test Permutations ===")
result1 = permutations([1, 2, 3])
print(f"Hoán vị của [1,2,3]: {result1}")
print(f"Số hoán vị: {len(result1)}") # Kỳ vọng: 6 (= 3!)

result2 = permutations([1, 2])
print(f"\nHoán vị của [1,2]: {result2}")
print(f"Số hoán vị: {len(result2)}") # Kỳ vọng: 2 (= 2!)


def combinations(nums, k):
    """
    Tìm tất cả tổ hợp k phần tử từ nums
    """
    result = []

    def backtrack(start, path):
        # Base case: Đã chọn đủ k phần tử
        if len(path) == k:
            result.append(path.copy())
            return

        # Thử các số từ vị trí start trở đi
        for i in range(start, len(nums)):
            # CHOOSE
            path.append(nums[i])
            
            # EXPLORE: Chỉ xét các số sau i (i+1)
            backtrack(i + 1, path)

            # UNCHOOSE: Quay lui
            path.pop()

    # Khởi chạy thuật toán với vị trí bắt đầu là 0 và danh sách rỗng
    backtrack(0, [])
    return result

# Test
print("\n=== Test Combinations ===")
result1 = combinations([1, 2, 3, 4], 2)
print(f"Tổ hợp 2 từ [1,2,3,4]: {result1}")
print(f"Số tổ hợp: {len(result1)}") # Kỳ vọng: 6 (C(4,2) = 6)

result2 = combinations([1, 2, 3], 2)
print(f"\nTổ hợp 2 từ [1,2,3]: {result2}")
print(f"Số tổ hợp: {len(result2)}") # Kỳ vọng: 3 (C(3,2) = 3)


def subsets(nums):
    """
    Tìm tất cả tập con của nums
    """
    result = []

    def backtrack(start, path):
        # Lưu tất cả tập con (không có điều kiện dừng cụ thể)
        result.append(path.copy())

        # Thử thêm các phần tử từ start
        for i in range(start, len(nums)):
            # CHOOSE
            path.append(nums[i])

            # EXPLORE
            backtrack(i + 1, path)

            # UNCHOOSE
            path.pop()

    backtrack(0, [])
    return result

# Test
print("\n=== Test Subsets ===")
result1 = subsets([1, 2, 3])
print(f"Tập con của [1,2,3]: {result1}")
print(f"Số tập con: {len(result1)}") # Kỳ vọng: 8 (= 2^3)

result2 = subsets([1, 2])
print(f"\nTập con của [1,2]: {result2}")
print(f"Số tập con: {len(result2)}") # Kỳ vọng: 4 (= 2^2)



def binary_strings(n):
    """
    Tìm tất cả chuỗi nhị phân độ dài n
    """
    result = []

    def backtrack(path):
        # Base case: Đủ n ký tự
        if len(path) == n:
            result.append(''.join(path))
            return  # CHÚ Ý: Lệnh return phải thụt vào trong lệnh if

        # Thử cả '0' và '1'
        for choice in ['0', '1']:
            # CHOOSE
            path.append(choice)

            # EXPLORE
            backtrack(path)

            # UNCHOOSE
            path.pop()

    backtrack([])
    return result

# Test
print("\n=== Test Binary Strings ===")
result1 = binary_strings(3)
print(f"Chuỗi nhị phân độ dài 3: {result1}")
print(f"Số chuỗi: {len(result1)}") # Kỳ vọng: 8 (= 2^3)

result2 = binary_strings(2)
print(f"\nChuỗi nhị phân độ dài 2: {result2}")
print(f"Số chuỗi: {len(result2)}") # Kỳ vọng: 4 (= 2^2)