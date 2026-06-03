from collections import deque

# Hàm 1: Xây dựng đồ thị [cite: 19, 20]
def build_graph(edges, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh [cite: 36]
    """
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# Hàm 2: BFS (Breadth-First Search) [cite: 105, 106]
def bfs(graph, start):
    """
    BFS - Duyệt đồ thị theo chiều rộng [cite: 121]
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Hàm 3: DFS đệ quy (Depth-First Search) [cite: 175, 176]
def dfs_recursive(graph, start, visited=None, result=None):
    """
    DFS - Duyệt đồ thị theo chiều sâu (đệ quy) [cite: 189]
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
        
    visited.add(start)
    result.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    return result

# Hàm 4: Connected Components [cite: 238, 239]
def count_connected_components(graph):
    """
    Đếm số connected components trong đồ thị [cite: 253]
    """
    visited = set()
    components = []
    
    def bfs_component(start):
        queue = deque([start])
        visited.add(start)
        component = []
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return component

    for vertex in graph:
        if vertex not in visited:
            component = bfs_component(vertex)
            components.append(component)
            
    return len(components), components

# ==== TEST CASES ====
if __name__ == "__main__":
    edges_undirected = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    graph_un = build_graph(edges_undirected, False)
    print(f"BFS từ A: {bfs(graph_un, 'A')}")
    print(f"DFS từ A: {dfs_recursive(graph_un, 'A')}")
    print(f"Connected Components: {count_connected_components(graph_un)[0]}")