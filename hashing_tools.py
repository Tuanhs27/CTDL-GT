from collections import defaultdict

# --- 2.1 Hash Table ---
class OrderHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size
        
    def insert(self, order_id, order_data):
        idx = self._hash(order_id)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == order_id:
                self.table[idx][i] = (order_id, order_data)
                return
        self.table[idx].append((order_id, order_data))
        
    def get(self, order_id):
        idx = self._hash(order_id)
        for k, v in self.table[idx]:
            if k == order_id: return v
        return None

    def remove(self, order_id):
        idx = self._hash(order_id)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == order_id:
                del self.table[idx][i]
                return True
        return False

# --- 2.2 Group Anagrams ---
def group_coupon_anagrams(codes):
    groups = defaultdict(list)
    for code in codes:
        key = tuple(sorted(code))
        groups[key].append(code)
    return list(groups.values())

# --- 2.3 Longest Consecutive ---
def longest_consecutive_days(days):
    day_set = set(days)
    longest = 0
    for day in day_set:
        if day - 1 not in day_set:
            curr = day
            streak = 1
            while curr + 1 in day_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
    return longest

# --- 2.4 Subarray Sum = k ---
def count_revenue_windows(revenues, k):
    prefix_sums = {0: 1}
    current_sum = 0
    count = 0
    for rev in revenues:
        current_sum += rev
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    return count

# --- 2.5 Rolling Hash ---
def rolling_hash_search(text, pattern):
    if not pattern or not text or len(pattern) > len(text): return -1
    d = 256
    q = 101
    M, N = len(pattern), len(text)
    p_hash, t_hash, h = 0, 0, 1
    
    for _ in range(M - 1): h = (h * d) % q
    for i in range(M):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
        
    for i in range(N - M + 1):
        if p_hash == t_hash:
            if text[i:i+M] == pattern: return i
        if i < N - M:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + M])) % q
            if t_hash < 0: t_hash += q
    return -1