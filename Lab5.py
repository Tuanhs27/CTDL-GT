from collections import deque

# ==============================================================================
# BÀI 1: GRAPH TRAVERSAL CƠ BẢN 
# ==============================================================================

# Hàm 1: Xây dựng đồ thị từ danh sách cạnh 
def build_graph(edges, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh sử dụng Dictionary.
    Mục đích: Chuyển đổi danh sách các cặp cạnh thành danh sách kề để tối ưu việc duyệt.
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

# Hàm 2: BFS (Breadth-First Search) 
def bfs(graph, start):
    """
    Duyệt đồ thị theo chiều rộng sử dụng Queue (FIFO).
    Mục đích: Duyệt qua từng lớp (level-by-level) tính từ đỉnh bắt đầu.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Hàm 3: DFS đệ quy (Depth-First Search) 
def dfs_recursive(graph, start, visited=None, result=None):
    """
    Duyệt đồ thị theo chiều sâu sử dụng cơ chế đệ quy (Call Stack).
    Mục đích: Đi sâu vào một nhánh xa nhất có thể trước khi quay lui (backtrack).
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
        
    visited.add(start)
    result.append(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    return result

# Hàm 4: Connected Components 
def count_connected_components(graph):
    """
    Đếm số thành phần liên thông trong đồ thị vô hướng sử dụng BFS helper.
    Mục đích: Tìm số lượng mạng lưới con độc lập và liệt kê các đỉnh thuộc mỗi mạng lưới.
    """
    visited = set()
    components = []
    
    def bfs_component(start_vertex):
        q = deque([start_vertex])
        visited.add(start_vertex)
        comp = []
        while q:
            vertex = q.popleft()
            comp.append(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return comp

    for vertex in graph:
        if vertex not in visited:
            component = bfs_component(vertex)
            components.append(component)
            
    return len(components), components


# ==============================================================================
# BÀI 2: CYCLE DETECTION (PHÁT HIỆN CHU TRÌNH) 
# ==============================================================================

# Phần A: Phát hiện chu trình trong đồ thị vô hướng 
def has_cycle_undirected(graph):
    """
    Phát hiện chu trình đồ thị vô hướng bằng DFS kết hợp biến parent.
    Giải thích: Cần kiểm tra neighbor != parent vì đồ thị vô hướng có tính chất hai chiều.
    Nếu gặp một đỉnh đã visited mà KHÔNG phải là cha vừa gọi nó, chứng tỏ tồn tại đường đi khác -> có chu trình.
    """
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# Phần B: Phát hiện chu trình trong đồ thị có hướng 
def has_cycle_directed(graph):
    """
    Phát hiện chu trình đồ thị có hướng bằng thuật toán tô màu 3 trạng thái (Three-Color).
    WHITE (0): Chưa thăm. GRAY (1): Đang trong nhánh đệ quy hiện tại. BLACK (2): Đã xử lý xong.
    Giải thích: Nếu trong quá trình duyệt đệ quy mà gặp lại một đỉnh đang có màu GRAY, 
    điều đó chứng tỏ đồ thị có đường quay lui (back-edge) tạo thành một vòng khép kín -> có chu trình.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}
    
    def dfs(vertex):
        color[vertex] = GRAY
        for neighbor in graph.get(vertex, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True
            if color.get(neighbor, WHITE) == WHITE:
                if dfs(neighbor):
                    return True
        color[vertex] = BLACK
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True
    return False

# Phần C: Hàm in lý thuyết so sánh 
def compare_cycle_detection():
    print("\n" + "="*60)
    print("SO SÁNH CYCLE DETECTION")
    print("="*60)
    print("Vô hướng: Sử dụng DFS kèm kiểm tra 'parent' để tránh nhận nhầm cạnh vừa đi qua.")
    print("Có hướng: Sử dụng 'Three-color' (WHITE/GRAY/BLACK) để tìm chuẩn xác back-edge.")
    print("Cả hai phương pháp đều chạy với độ phức tạp thời gian tối ưu là O(V + E).")
    print("="*60)


# ==============================================================================
# BÀI 3: TOPOLOGICAL SORT & COURSE SCHEDULE 
# ==============================================================================

# Phần A: Topological Sort với DFS 
def topological_sort_dfs(graph):
    """
    Sắp xếp topo bằng phương pháp Post-Order DFS.
    Chỉ áp dụng với đồ thị có hướng không chu trình (DAG).
    """
    if has_cycle_directed(graph):
        return None
        
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex) # Thêm vào stack sau khi xử lý xong tất cả các neighbors 
        
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            
    return stack[::-1] # Kết quả sắp xếp topo là stack đảo ngược 

# Phần B: Topological Sort với Kahn's Algorithm (BFS + In-degree) 
def topological_sort_kahn(graph):
    """
    Sắp xếp topo sử dụng thuật toán Kahn (Duyệt theo bán bậc vào - In-degree).
    """
    # Khởi tạo in-degree cho mọi đỉnh trong đồ thị bằng 0 
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1
            
    # Đưa các đỉnh không có ràng buộc (in-degree = 0) vào queue 
    queue = deque([u for u in graph if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    # Nếu số lượng phần tử kết quả khác tổng số đỉnh ban đầu -> đồ thị có chu trình 
    if len(result) != len(graph):
        return None
    return result

# Phần C: Ứng dụng Course Schedule 
def build_course_graph(num_courses, prerequisites):
    """Hàm bổ trợ xây dựng danh sách kề cho các môn học """
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course) # Điều kiện: học prereq xong mới được học course 
    return graph

# Bài toán 1: Kiểm tra có thể hoàn thành khóa học 
def can_finish(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    return not has_cycle_directed(graph)

# Bài toán 2: Tìm thứ tự học hợp lệ 
def find_order(num_courses, prerequisites):
    graph = build_course_graph(num_courses, prerequisites)
    order = topological_sort_kahn(graph)
    return order if order is not None else []


# ==============================================================================
# KHU VỰC CHẠY THỬ TOÀN BỘ TEST CASES THEO FILE LAB 
# ==============================================================================
if __name__ == "__main__":
    # Test Bài 1: Graph Traversal 
    print("\n" + "="*60)
    print("TEST BÀI 1: GRAPH TRAVERSAL")
    print("="*60)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    graph = build_graph(edges)
    print(f"Đồ thị: {graph}")
    bfs_result = bfs(graph, 'A')
    dfs_result = dfs_recursive(graph, 'A')
    print(f"BFS từ A: {bfs_result}")
    print(f"DFS từ A: {dfs_result}")
    num_components, components = count_connected_components(graph)
    print(f"Số thành phần liên thông: {num_components}, Các thành phần: {components}")

    # Test Bài 2: Cycle Detection 
    print("\n" + "="*60)
    print("TEST BÀI 2: CYCLE DETECTION")
    print("="*60)
    graph_undirected = build_graph([('A', 'B'), ('B', 'C'), ('C', 'A')], directed=False)
    graph_directed = build_graph([('A', 'B'), ('B', 'C'), ('C', 'A')], directed=True)
    print(f"Đồ thị vô hướng có chu trình: {has_cycle_undirected(graph_undirected)}")
    print(f"Đồ thị có hướng có chu trình: {has_cycle_directed(graph_directed)}")
    compare_cycle_detection()

    # Test Bài 3: Topological Sort & Course Schedule 
    print("\n" + "="*60)
    print("TEST BÀI 3: TOPOLOGICAL SORT & COURSE SCHEDULE")
    print("="*60)
    graph_dag = build_graph([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')], directed=True)
    topo_dfs = topological_sort_dfs(graph_dag)
    topo_kahn = topological_sort_kahn(graph_dag)
    print(f"Sắp xếp topo (DFS): {topo_dfs}")
    print(f"Sắp xếp topo (Kahn): {topo_kahn}")
    
    prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]
    print(f"Có thể hoàn thành khóa học: {can_finish(4, prerequisites)}")
    print(f"Thứ tự học hợp lệ: {find_order(4, prerequisites)}")     