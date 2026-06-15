from lab6_bai2 import make_set, find, union
from lab6_bai2 import make_set_optimized, find_optimized, union_optimized

def kruskal_mst_basic(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])
    parent = make_set(vertices)
    mst = []
    total_weight = 0
    
    print("Cạnh sau khi sort (w, u, v):")
    for e in edges_sorted:
        print("  ", e)
        
    print("\nDuyệt từng cạnh:")
    for w, u, v in edges_sorted:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        print(f"Xét cạnh {u}-{v} (w={w}), root_u={root_u}, root_v={root_v}")
        
        if root_u != root_v:
            print("  -> Khác nhóm -> CHỌN cạnh này")
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)
        else:
            print("  -> Cùng nhóm -> BỎ (tránh chu trình)")
            
        if len(mst) == len(vertices) - 1:
            break
            
    return mst, total_weight

def kruskal_mst_optimized(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])
    parent, size = make_set_optimized(vertices)
    mst = []
    total_weight = 0
    
    for w, u, v in edges_sorted:
        if find_optimized(parent, u) != find_optimized(parent, v):
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)
            
        if len(mst) == len(vertices) - 1:
            break
            
    return mst, total_weight

def test_kruskal():
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E')
    ]
    
    print("=== Kruskal với DSU basic ===")
    mst1, total1 = kruskal_mst_basic(vertices, edges)
    print("\nMST basic:")
    for u, v, w in mst1:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total1)
    
    print("\n=== Kruskal với DSU optimized ===")
    mst2, total2 = kruskal_mst_optimized(vertices, edges)
    print("\nMST optimized:")
    for u, v, w in mst2:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total2)

if __name__ == "__main__":
    test_kruskal()