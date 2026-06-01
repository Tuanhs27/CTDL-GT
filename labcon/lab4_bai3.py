def find_content_children(greed, cookies):
    """
    Assign Cookies - LeetCode 455
    Chiến lược: Sort cả 2 mảng + Two Pointers
    """
    # TODO: Sort cả greed và cookies
    greed.sort()
    cookies.sort()
    
    # TODO: Dùng 2 con trỏ duyệt
    i, j = 0, 0
    content_children = 0
    
    while i < len(greed) and j < len(cookies):
        if cookies[j] >= greed[i]:
            content_children += 1
            i += 1
        j += 1
    
    # TODO: Trả về số trẻ đã thỏa mãn
    return content_children
pass

#Phần C
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_bikes(workers, bikes):
    """
    Ghép worker với bike bằng chiến lược Greedy
    """
    # 1. Tính tất cả khoảng cách Manhattan
    distances = []
    for i, w in enumerate(workers):
        for j, b in enumerate(bikes):
            dist = manhattan_distance(w, b)
            distances.append((dist, i, j)) # (khoảng cách, worker_idx, bike_idx)
    
    # 2. Sort theo khoảng cách tăng dần
    distances.sort(key=lambda x: x[0])
    
    # 3. Greedy chọn cặp gần nhất chưa dùng
    worker_used = [False] * len(workers)
    bike_used = [False] * len(bikes)
    assignments = []
    total_distance = 0
    
    for dist, w_idx, b_idx in distances:
        if not worker_used[w_idx] and not bike_used[b_idx]:
            worker_used[w_idx] = True
            bike_used[b_idx] = True
            assignments.append((w_idx, b_idx, dist))
            total_distance += dist
            
    return total_distance, assignments

# Test
workers = [(0, 0), (2, 1)]
bikes = [(1, 2), (3, 3)]
total, results = assign_bikes(workers, bikes)

print(f"Tổng khoảng cách nhỏ nhất (Greedy): {total}")
for w, b, dist in results:
    print(f"Worker {w} ghép với Bike {b} (Khoảng cách: {dist})")

#Phần C
import random
import time
import matplotlib.pyplot as plt

def activity_selection(activities):
    """
    Chọn tập hoạt động tối đa không giao nhau bằng chiến lược Greedy.
    activities: list of (start, end)
    Trả về list các hoạt động đã chọn (start, end), sắp theo thời gian kết thúc.
    """
    if not activities:
        return []
    # Sort activities by end time
    activities_sorted = sorted(activities, key=lambda x: x[1])
    selected = [activities_sorted[0]]
    last_end = activities_sorted[0][1]
    for s, e in activities_sorted[1:]:
        if s >= last_end:
            selected.append((s, e))
            last_end = e
    return selected

# Giả sử hàm activity_selection đã được định nghĩa ở bước trước
def generate_test_data(n):
    """Tạo dữ liệu test ngẫu nhiên"""
    activities = []
    for i in range(n):
        start = random.randint(0, 1000)
        duration = random.randint(1, 50)
        end = start + duration
        activities.append((start, end))
    return activities

def benchmark_activity_selection(sizes):
    """Đo thời gian với các kích thước input khác nhau"""
    times = []
    print(f"{'Kích thước (n)':<15} | {'Thời gian (s)':<15}")
    print("-" * 35)
    
    for size in sizes:
        activities = generate_test_data(size)

        start = time.time()
        activity_selection(activities)
        elapsed = time.time() - start
        
        times.append(elapsed)
        print(f"{size:<15} | {elapsed:.6f}s")
    return times

# Chạy benchmark
sizes = [1000, 5000, 10000, 50000, 100000]
times = benchmark_activity_selection(sizes)

# Vẽ biểu đồ để thấy rõ độ phức tạp O(n log n)
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.title("Hiệu năng thuật toán Activity Selection (O(n log n))")
plt.xlabel("Số lượng hoạt động (n)")
plt.ylabel("Thời gian chạy (giây)")
plt.grid(True)
plt.show()