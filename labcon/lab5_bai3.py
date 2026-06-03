from collections import deque

# Import hàm cycle detection từ phần trước (hoặc copy sang nếu cần chạy độc lập)
# Để mô phỏng, tôi sẽ đặt trực tiếp logic cycle detection ở đây
def has_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}
    def dfs(v):
        color[v] = GRAY
        for neighbor in graph.get(v, []):
            if color.get(neighbor, WHITE) == GRAY: return True
            if color.get(neighbor, WHITE) == WHITE and dfs(neighbor): return True
        color[v] = BLACK
        return False
    for v in graph:
        if color[v] == WHITE and dfs(v): return True
    return False

# Phần A: Topological Sort với DFS [cite: 503, 504]
def topological_sort_dfs(graph):
    if has_cycle(graph):
        return None
        
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)
        
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            
    return stack[::-1] # Trả về stack đảo ngược [cite: 531]

# Phần B: Topological Sort với Kahn's Algorithm [cite: 534, 535]
def topological_sort_kahn(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1
            
    queue = deque([u for u in graph if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(result) != len(graph):
        return None # Có chu trình [cite: 558]
    return result

# Phần C: Course Schedule [cite: 561, 562]
def build_course_graph(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course) # Phải học prereq trước course [cite: 568]
    return graph

# Bài toán 1 [cite: 563]
def can_finish(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    return not has_cycle(graph)

# Bài toán 2 [cite: 578]
def find_order(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    order = topological_sort_kahn(graph)
    return order if order is not None else []

# ==== TEST CASES ==== [cite: 590]
if __name__ == "__main__":
    n1 = 4
    prereqs1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"Test Course Schedule 1 (Can Finish): {can_finish(n1, prereqs1)}")
    print(f"Order: {find_order(n1, prereqs1)}")
    
    n2 = 2
    prereqs2 = [[1, 0], [0, 1]]
    print(f"Test Course Schedule 2 (Cycle): {can_finish(n2, prereqs2)}")
    print(f"Order: {find_order(n2, prereqs2)}")