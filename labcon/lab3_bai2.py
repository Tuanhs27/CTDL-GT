def is_safe(board, row, col, n):
    """
    Kiểm tra đặt quân hậu ở (row, col) có hợp lệ không
    board: list lưu cột của quân hậu ở mỗi hàng
    """
    # Kiểm tra tất cả các hàng trước đó
    for prev_row in range(row):
        prev_col = board[prev_row]
        # Kiểm tra cùng cột
        if prev_col == col:
            return False
        # Kiểm tra đường chéo
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def print_board(solution, n):
    """
    In bàn cờ N×N với quân hậu
    """
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_n_queens(n):
    """
    Hàm chính giải bài toán N-Queens
    """
    board = [-1] * n
    
    def backtrack(row):
        if row == n:
            print_board(board, n)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1 # Reset

    backtrack(0)

# Test với bàn cờ 4x4
print("=== Bàn cờ 4x4 ===")
solve_n_queens(4)

class Counter:
    """Class để đếm số lần gọi hàm"""
    def __init__(self):
        self.total_calls = 0
        self.solutions = 0

    def report(self):
        print(f"Tổng số lần gọi: {self.total_calls}")
        print(f"Số giải pháp tìm được: {self.solutions}")

def is_valid(board):
    """Kiểm tra xem cấu hình bàn cờ hiện tại có hợp lệ không"""
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Kiểm tra cùng cột hoặc cùng đường chéo
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def solve_n_queens_no_pruning(n):
    """
    N-Queens KHÔNG có pruning (kiểm tra sau)
    """
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        # Base case: Đã đặt đủ n quân hậu
        if row == n:
            if is_valid(board):
                result.append(board.copy())
                counter.solutions += 1
            return

        # Thử tất cả cột (0 đến n-1)
        for col in range(n):
            board.append(col)
            backtrack(row + 1)
            board.pop()

    backtrack(0)
    counter.report()
    return result

# Test với bàn cờ 4x4
print("=== Kết quả 4x4 (No Pruning) ===")
solve_n_queens_no_pruning(4)


def solve_n_queens_with_pruning(n):
    """
    N-Queens CÓ pruning (kiểm tra trước)
    """
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        # Base case
        if row == n:
            result.append(board.copy())
            counter.solutions += 1
            return

        # Thử từng cột
        for col in range(n):
            # PRUNING: Kiểm tra is_safe TRƯỚC khi đệ quy
            if is_safe(board, row, col, n):
                # CHOOSE
                board.append(col)

                # EXPLORE
                backtrack(row + 1)

                # UNCHOOSE
                board.pop()

    backtrack(0)
    counter.report()
    return result

# Test thử với 4x4
print("\n=== Kết quả 4x4 (Có Pruning) ===")
solve_n_queens_with_pruning(4)

import time

def compare_n_queens(n):
    print(f"\n{'='*50}")
    print(f"So sánh N-Queens với N={n}")
    print(f"{'='*50}")

    # 1. Test không có pruning
    print("\n[1] KHÔNG có pruning:")
    start = time.time()
    result1 = solve_n_queens_no_pruning(n)
    time1 = time.time() - start
    print(f"Thời gian chạy: {time1:.6f} giây")

    # 2. Test có pruning
    print("\n[2] CÓ pruning:")
    start = time.time()
    result2 = solve_n_queens_with_pruning(n)
    time2 = time.time() - start
    print(f"Thời gian chạy: {time2:.6f} giây")
    
    # 3. In kết quả so sánh
    if time2 > 0:
        print(f"\nTốc độ nhanh hơn: {time1/time2:.2f} lần")
    else:
        print("\nPruning quá nhanh, thời gian đo được gần bằng 0!")

    # In một giải pháp mẫu
    if len(result2) > 0:
        print(f"\nMột giải pháp mẫu cho {n}-Queens:")
        print_board(result2[0], n)

# Chạy thử
compare_n_queens(4)
compare_n_queens(6)