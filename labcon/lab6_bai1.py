import heapq

def dijkstra(graph, source):
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    parent = {v: None for v in graph}
    pq = [(0, source)]
    visited = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if current_dist > distances[u]:
            continue
        for v, w in graph[u]:
            new_dist = distances[u] + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
                
    return distances, parent

def reconstruct_path(parent, source, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    if not path or path[0] != source:
        return None
    return path

def print_distances(distances, source):
    print(f"Bảng khoảng cách từ {source}:")
    for v in sorted(distances.keys()):
        d = distances[v]
        if d == float('inf'):
            print(f"  {source} -> {v}: INF (không tới được)")
        else:
            print(f"  {source} -> {v}: {d}")

def test_dijkstra():
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }
    source = 'A'
    distances, parent = dijkstra(graph, source)
    
    print_distances(distances, source)
    print("\nĐường đi chi tiết:")
    
    for v in sorted(graph.keys()):
        if v == source:
            continue
        path = reconstruct_path(parent, source, v)
        if path is None:
            print(f"  {source} -> {v}: không có đường đi")
        else:
            cost = distances[v]
            print(f"  {source} -> {v}: {' -> '.join(path)} (cost = {cost})")

if __name__ == "__main__":
    test_dijkstra()