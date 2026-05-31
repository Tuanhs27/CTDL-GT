#Hàm 1
def activity_selection(activities):
    """
    Chọn số lượng hoạt động tối đa không chồng lấp
    Chiến lược: Chọn kết thúc sớm nhất (earliest finish time)
    """
    if not activities:
        return []

    # Bước 1: Sort theo finish time (index 1)
    activities.sort(key=lambda x: x[1])

    # Bước 2: Chọn hoạt động đầu tiên
    selected = [activities[0]]
    last_finish = activities[0][1]

    # Bước 3: Duyệt các hoạt động còn lại
    for i in range(1, len(activities)):
        start, finish = activities[i]
        
        # Nếu start time >= thời gian kết thúc của hoạt động trước đó → Chọn
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
            
    return selected

# Test case 1
print("=== Test Activity Selection ===")
activities1 = [
    (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), 
    (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)
]
result1 = activity_selection(activities1)
print(f"Hoạt động được chọn: {result1}")
print(f"Số lượng: {len(result1)}") 

# Test case 2
activities2 = [(1, 3), (2, 4), (3, 5), (4, 6)]
result2 = activity_selection(activities2)
print(f"\nHoạt động được chọn: {result2}")
print(f"Số lượng: {len(result2)}")

#hàm 2
def coin_change_greedy(amount, coins):
    """
    Đổi tiền bằng số xu ít nhất (Greedy approach)
    """
    # Bước 1: Sort giảm dần
    coins.sort(reverse=True)
    count = 0
    result = []
    
    # Bước 2: Duyệt từng mệnh giá
    for coin in coins:
        if amount == 0:
            break
        # Dùng phép chia lấy nguyên để lấy số lượng xu nhanh hơn thay vì while loop
        num_coins = amount // coin
        if num_coins > 0:
            count += num_coins
            amount %= coin
            result.extend([coin] * num_coins)
            
    # Bước 3: Kiểm tra kết quả
    if amount == 0:
        return count, result
    else:
        return -1, []

# Test
print("\n=== Test Coin Change Greedy ===")
print("Test 1: Hệ chuẩn [25, 10, 5, 1] - amount 63")
print(coin_change_greedy(63, [25, 10, 5, 1]))

print("\nTest 3: Hệ mệnh giá lạ [25, 10, 1] - amount 30")
count, res = coin_change_greedy(30, [25, 10, 1])
print(f"Greedy chọn: {res} (Tổng: {count} xu)")
print("⚠️ Kết quả tối ưu phải là: [10, 10, 10] (3 xu)")

#hàm 3
def fractional_knapsack(capacity, items):
    """
    Bài toán Ba lô phân số (Fractional Knapsack)
    """
    # Bước 1: Tính ratio (value/weight) cho mỗi vật
    items_with_ratio = []
    for weight, value in items:
        ratio = value / weight
        items_with_ratio.append((weight, value, ratio))
    
    # Sort theo ratio giảm dần (index 2 là ratio)
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    # Bước 2: Duyệt và chọn
    total_value = 0.0
    remaining_capacity = capacity
    result = []
    
    for weight, value, ratio in items_with_ratio:
        if remaining_capacity <= 0:
            break
            
        if weight <= remaining_capacity:
            # Lấy hết vật phẩm
            total_value += value
            remaining_capacity -= weight
            result.append((weight, value, 1.0))
        else:
            # Lấy một phần của vật phẩm
            fraction = remaining_capacity / weight
            total_value += value * fraction
            result.append((weight, value, fraction))
            remaining_capacity = 0
            
    return total_value, result

# Test
print("\n=== Test Fractional Knapsack ===")
capacity1 = 50
items1 = [(10, 60), (20, 100), (30, 120)]
total1, result1 = fractional_knapsack(capacity1, items1)
print(f"Giá trị tối đa: {total1}")
for w, v, f in result1:
    print(f" Vật (w={w}, v={v}): Lấy {f*100:.1f}%")

#hàm 4
# Giả sử bạn đã có hàm activity_selection từ bài trước
def min_intervals_remove(intervals):
    """
    Tìm số khoảng thời gian ít nhất cần xóa 
    để các khoảng còn lại không chồng lấp.
    """
    if not intervals:
        return 0
        
    # Tính số lượng khoảng giữ lại tối đa bằng thuật toán Greedy
    max_keep = activity_selection(intervals)
    
    # Số cần xóa chính là phần bù
    num_remove = len(intervals) - len(max_keep)
    return num_remove

# Test
intervals1 = [(1, 2), (2, 3), (3, 4), (1, 3)]
print(f"Số khoảng cần xóa (Test 1): {min_intervals_remove(intervals1)}")

intervals2 = [(1, 2), (1, 2), (1, 2)]
print(f"Số khoảng cần xóa (Test 2): {min_intervals_remove(intervals2)}")

intervals3 = [(1, 100), (11, 22), (1, 11), (2, 12)]
print(f"Số khoảng cần xóa (Test 3): {min_intervals_remove(intervals3)}")


