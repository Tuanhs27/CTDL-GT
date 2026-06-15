def make_set(vertices):
    parent = {}
    for v in vertices:
        parent[v] = v
    return parent

def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

def demo_dsu_basic():
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent = make_set(vertices)
    
    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E')
    ]
    
    for op in ops:
        if op[0] == "union":
            _, x, y = op
            print(f"Thực hiện union({x}, {y})")
            union(parent, x, y)
        else:
            _, x = op
            root = find(parent, x)
            print(f"find({x}) = {root}")
            
    print("parent hiện tại:", parent)

def make_set_optimized(vertices):
    parent = {}
    size = {}
    for v in vertices:
        parent[v] = v
        size[v] = 1
    return parent, size

def find_optimized(parent, v):
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])
    return parent[v]

def union_optimized(parent, size, a, b):
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)
    
    if root_a == root_b:
        return
        
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a
        
    parent[root_b] = root_a
    size[root_a] += size[root_b]

if __name__ == "__main__":
    demo_dsu_basic()