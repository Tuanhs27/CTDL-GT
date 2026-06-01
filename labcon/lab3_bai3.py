import time
class Counter:
    """Class để đếm số lần gọi hàm đệ quy"""
    def __init__(self):
        self.calls = 0
def subset_sum_basic(nums, target, counter):
    """Subset Sum cơ bản (chỉ để so sánh)"""
    result = [] 
    def backtrack(start, path, current_sum):
        counter.calls += 1
        
        if current_sum == target:
            result.append(path.copy())
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
    backtrack(0, [], 0)
    return result
def subset_sum_pruned(nums, target, counter):
    """Subset Sum áp dụng 4 kỹ thuật tối ưu"""
    result = []
    nums.sort() 
    suffix_sums = [0] * len(nums)
    curr_sum = 0
    for i in range(len(nums) - 1, -1, -1):
        curr_sum += nums[i]
        suffix_sums[i] = curr_sum
    def backtrack(start, path, current_sum):
        counter.calls += 1
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return 
        for i in range(start, len(nums)):
 
            if i > start and nums[i] == nums[i-1]:
                continue
            if current_sum + nums[i] > target:
                break
            remaining_sum = suffix_sums[i] 
            if current_sum + remaining_sum < target:
                break 
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
    backtrack(0, [], 0)
    return result
def compare_subset_sum(nums, target):
    print(f"{'='*50}")
    print(f"SO SÁNH SUBSET SUM (Target = {target}, N = {len(nums)})")
    print(f"{'='*50}")
    counter_basic = Counter()
    start_time = time.time()
    res_basic = subset_sum_basic(nums, target, counter_basic)
    time_basic = time.time() - start_time
    counter_pruned = Counter()
    start_time = time.time()
    res_pruned = subset_sum_pruned(nums.copy(), target, counter_pruned)
    time_pruned = time.time() - start_time
    nhanh_cat_tia = counter_basic.calls - counter_pruned.calls
    ty_le_cat = (nhanh_cat_tia / counter_basic.calls) * 100 if counter_basic.calls > 0 else 0
    toc_do_tang = time_basic / time_pruned if time_pruned > 0 else float('inf')
    print("[1] BẢN CƠ BẢN (KHÔNG PRUNING):")
    print(f" - Tổng số lần gọi hàm: {counter_basic.calls:,}")
    print(f" - Thời gian chạy     : {time_basic:.6f} giây")
    print(f" - Số nghiệm tìm được : {len(res_basic):,}")
    print("\n[2] BẢN TỐI ƯU (CÓ 4 PRUNING):")
    print(f" - Tổng số lần gọi hàm: {counter_pruned.calls:,}")
    print(f" - Thời gian chạy     : {time_pruned:.6f} giây")
    print(f" - Số nghiệm tìm được : {len(res_pruned):,}")
    print("\n[3] BÁO CÁO HIỆU NĂNG:")
    print(f" - Số nhánh đã cắt tỉa: {nhanh_cat_tia:,}")
    print(f" - Tỷ lệ cắt (%)      : {ty_le_cat:.2f}%")
    print(f" - Tốc độ tăng (lần)  : {toc_do_tang:.2f}x nhanh hơn")
if __name__ == "__main__":
    test_nums = list(range(1, 20)) # [1, 2, ..., 19]
    test_target = 50
    compare_subset_sum(test_nums, test_target)