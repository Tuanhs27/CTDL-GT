

from collections import deque
def bfs(graph, start):
    # BFS Duyệt đổ thị theo chiều rộng
    # Khởi tạo
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    #BFS loop
    while queue:
    # Lấy đình từ queue
        vertex = queue.popleft()
        result.append(vertex)
        # Duyệt các đỉnh kế
        for neighbor in graph [vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['B']
}
result = bfs(graph, 'A')
print(f"BFS từ A: {result}")
# Output: ['A', 'B', 'C', 'D', 'E']


