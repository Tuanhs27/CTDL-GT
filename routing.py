
import heapq

# --- 1.1 Dijkstra ---
def build_graph(edges):
    graph = {}
    for u, v, cost in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    return graph

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, parent

def shortest_route(graph, source, target):
    dist, parent = dijkstra(graph, source)
    if dist[target] == float('inf'): return float('inf'), []
    route = []
    curr = target
    while curr:
        route.append(curr)
        curr = parent[curr]
    return dist[target], route[::-1]

# --- 1.2 MST (Kruskal + DSU) ---
class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.size = {v: 1 for v in vertices}

    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

def kruskal_mst(vertices, edges):
    dsu = DSU(vertices)
    edges.sort(key=lambda x: x[2])
    mst = []
    total_cost = 0
    for u, v, cost in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, cost))
            total_cost += cost
    return mst, total_cost

def demo_routing_shortest_path():
    edges = [('WH1', 'WH2', 10), ('WH1', 'HN', 50), ('WH2', 'HCM', 30), ('HN', 'DN', 20), ('DN', 'HCM', 40)]
    graph = build_graph(edges)
    cost, route = shortest_route(graph, 'WH1', 'HCM')
    print(f"Shortest path WH1 -> HCM: Cost {cost}, Route: {route}")

def demo_mst_network():
    vertices = ['WH1', 'WH2', 'HN', 'HCM', 'DN']
    edges = [('WH1', 'WH2', 10), ('WH1', 'HN', 50), ('WH2', 'HCM', 30), ('HN', 'DN', 20), ('DN', 'HCM', 40)]
    mst, cost = kruskal_mst(vertices, edges)
    print(f"MST Edges: {mst}, Total Cost: {cost}")