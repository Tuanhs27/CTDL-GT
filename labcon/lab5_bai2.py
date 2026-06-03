# lab5_bai2.py

# ==============================================================================
# PHẦN A - Phát hiện chu trình trong đồ thị vô hướng
# ==============================================================================
def has_cycle_undirected(graph):
    """
    Phát hiện chu trình trong đồ thị vô hướng
    Chiến lược: Dùng DFS với tham số parent.
    """
    visited = set()
    
    def dfs(vertex, parent):
        # Đánh dấu vertex là visited
        visited.add(vertex)
        
        # Duyệt các neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Đệ quy với neighbor
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # Gặp đỉnh đã visited và không phải cha -> Có chu trình!
                return True
        return False
        
    # Duyệt tất cả các đỉnh (đồ thị có thể không liên thông)
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# ==============================================================================
# PHẦN B - Phát hiện chu trình trong đồ thị có hướng
# ==============================================================================
def has_cycle_directed(graph):
    """
    Phát hiện chu trình trong đồ thị có hướng
    Sử dụng three-color approach:
    - WHITE: Chưa thăm
    - GRAY: Đang xử lý (trong recursion stack)
    - BLACK: Đã xử lý xong
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    
    # Khởi tạo color cho tất cả đỉnh là WHITE
    color = {vertex: WHITE for vertex in graph}
    
    def dfs(vertex):
        # Đánh dấu đỉnh đang xử lý (GRAY)
        color[vertex] = GRAY
        
        # Duyệt các neighbors
        for neighbor in graph[vertex]:
            # Nếu neighbor đang GRAY -> trong recursion stack -> có chu trình
            if color[neighbor] == GRAY:
                return True
            # Nếu neighbor là WHITE -> chưa thăm
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True
                    
        # Xử lý xong đỉnh này (BLACK)
        color[vertex] = BLACK
        return False
        
    # Duyệt tất cả các đỉnh
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True
    return False

# ==============================================================================
# PHẦN C - So sánh và phân tích
# ==============================================================================
def compare_cycle_detection():
    print("\n" + "="*60)
    print("SO SÁNH CYCLE DETECTION")
    print("="*60)
    
    print("\n[1] ĐỒ THỊ VÔ HƯỚNG:")
    undirected_graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    print(f"Đồ thị test: {undirected_graph}")
    print(f"Kết quả (Có chu trình): {has_cycle_undirected(undirected_graph)}")
    
    print("\n[2] ĐỒ THỊ CÓ HƯỚNG:")
    directed_graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    print(f"Đồ thị test: {directed_graph}")
    print(f"Kết quả (Có chu trình): {has_cycle_directed(directed_graph)}")
    
    print("\n[3] SO SÁNH:")
    print("Vô hướng: Kiểm tra parent")
    print("Có hướng: Three-color (WHITE/GRAY/BLACK)")
    print("Cả hai: Độ phức tạp O(V+E)")

# ==============================================================================
# TEST CASES
# ==============================================================================
if __name__ == "__main__":
    # Test cases vô hướng
    print("=== Test Cycle Detection - Undirected ===")
    graph1_un = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    print(f"Test 1 (có chu trình): {has_cycle_undirected(graph1_un)}")
    
    graph2_un = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    print(f"Test 2 (không có chu trình): {has_cycle_undirected(graph2_un)}")
    
    graph3_un = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    print(f"Test 3 (nhiều components, có chu trình): {has_cycle_undirected(graph3_un)}")

    # Test cases có hướng
    print("\n=== Test Cycle Detection - Directed ===")
    graph1_di = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    print(f"Test 1 (có chu trình A->B->C->A): {has_cycle_directed(graph1_di)}")
    
    graph2_di = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
    print(f"Test 2 (DAG): {has_cycle_directed(graph2_di)}")
    
    graph3_di = {'A': ['B'], 'B': ['C'], 'C': [], 'D': ['C']}
    print(f"Test 3 (cross edge, không có chu trình): {has_cycle_directed(graph3_di)}")

    # Chạy hàm so sánh
    compare_cycle_detection()