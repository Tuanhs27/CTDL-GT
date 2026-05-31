import heapq
import time
import heapq

from lab4_bai1 import coin_change_greedy

def min_meeting_rooms(meetings):
    """
    Tìm số phòng họp tối thiểu cần thiết
    Chiến lược: Sort theo start time + dùng Heap theo dõi end time
    """
    if not meetings:
        return 0
    
    # 1. Sort meetings theo start time
    meetings.sort(key=lambda x: x[0])
    
    # Heap lưu end time của các phòng đang dùng
    heap = []
    
    # 2. Thêm end time của meeting đầu tiên vào heap
    heapq.heappush(heap, meetings[0][1])
    
    # 3. Duyệt các meetings còn lại
    for i in range(1, len(meetings)):
        start, end = meetings[i]
        
        # Nếu phòng sớm nhất đã trống (start >= end time cũ)
        # → Tái sử dụng phòng đó (cập nhật bằng cách pop và push)
        if start >= heap[0]:
            heapq.heappop(heap)
            
        # Thêm end time của meeting hiện tại vào heap
        heapq.heappush(heap, end)
        
    # Số phòng = số phần tử trong heap
    return len(heap)

# Test
meetings = [(0, 30), (5, 10), (15, 20)]
print(f"Số phòng tối thiểu cần thiết: {min_meeting_rooms(meetings)}")
# Kỳ vọng: 2

#Phần B
def coin_change_dp(amount, coins):
    """
    Coin Change với Dynamic Programming
    Luôn cho lời giải tối ưu
    """
    # Khởi tạo dp array với giá trị vô cùng lớn
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 xu để đổi số tiền 0
    dp[0] = 0 
    
    # Tính dp[i] cho i từ 1 đến amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # Công thức truy hồi: chọn giá trị nhỏ nhất giữa việc 
                # giữ nguyên hiện tại hoặc thêm 1 đồng xu vào cách đổi cũ
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # Trả về kết quả
    return dp[amount] if dp[amount] != float('inf') else -1

# Test với hệ mệnh giá lạ (Greedy đã thất bại ở đây)
coins = [25, 10, 1]
amount = 30
result = coin_change_dp(amount, coins)
print(f"Số xu ít nhất để đổi {amount} là: {result}") 
# Kết quả: 3 (tương ứng với 10+10+10)

#PHần C
import time

def compare_coin_change(amount, coins):
    print(f"\n{'='*60}")
    print(f"So sánh Coin Change: amount={amount}, coins={coins}")
    print(f"{'='*60}")
    
    # 1. Test Greedy
    print("\n[1] GREEDY:")
    start = time.time()
    greedy_result, greedy_detail = coin_change_greedy(amount, coins)
    greedy_time = time.time() - start
    print(f"Kết quả: {greedy_result} xu")
    print(f"Chi tiết: {greedy_detail}")
    print(f"Thời gian: {greedy_time:.6f}s")
    
    # 2. Test DP
    print("\n[2] DYNAMIC PROGRAMMING:")
    start = time.time()
    dp_result = coin_change_dp(amount, coins)
    dp_time = time.time() - start
    print(f"Kết quả: {dp_result} xu")
    print(f"Thời gian: {dp_time:.6f}s")
    
    # 3. So sánh
    print("\n[3] SO SÁNH:")
    if greedy_result == dp_result:
        print("✅ Greedy ĐÚNG - cho kết quả tối ưu!")
    else:
        print(f"❌ Greedy SAI - kém hơn {dp_result - greedy_result} xu!")
        
    if greedy_time > 0:
        print(f"Tốc độ: Greedy nhanh hơn {dp_time/greedy_time:.2f}x")
    else:
        print("Tốc độ: Cả hai đều cực nhanh.")

# Test với các trường hợp
compare_coin_change(67, [25, 10, 5, 1])
compare_coin_change(30, [25, 10, 1])
