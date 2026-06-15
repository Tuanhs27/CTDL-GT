# --- 3.1 DP Basics ---
def fib_memo(n, memo={}):
    if n <= 1: return n
    if n not in memo: memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# --- 3.2 Knapsack 0/1 (2D) ---
def build_combo_dp_table(prices, scores, B):
    n = len(prices)
    dp = [[0] * (B + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(B + 1):
            if prices[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-prices[i-1]] + scores[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp

def trace_combo_from_dp(dp, prices, scores, B):
    n = len(prices)
    res = dp[n][B]
    w = B
    selected = []
    for i in range(n, 0, -1):
        if res <= 0: break
        if res != dp[i-1][w]:
            selected.append(i-1)
            res -= scores[i-1]
            w -= prices[i-1]
    return selected[::-1]

# --- 3.3 Knapsack 0/1 (1D) ---
def combo_knapsack_1d(prices, scores, B):
    dp = [0] * (B + 1)
    for i in range(len(prices)):
        for w in range(B, prices[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - prices[i]] + scores[i])
    return dp[B]