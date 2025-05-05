import heapq

# Step 1: Build the graph with weights
g = {}
n = int(input("Enter the number of edges: "))
print("Enter edges (format: a b weight):")

for i in range(n):
    a, b, w = map(int, input().split())  # read edge: from a to b with weight w
    if g.get(a) is None:
        g[a] = []
    g[a].append((b, w))

    if g.get(b) is None:
        g[b] = []
    g[b].append((a, w))  # undirected graph

# Step 2: Prim's Algorithm
start_node = next(iter(g))  # Start from any node
visited = set()
min_heap = [(0, start_node, -1)]  # (weight, current_node, from_node)
mst_cost = 0
mst_edges = []

while min_heap:
    weight, node, from_node = heapq.heappop(min_heap)
    if node in visited:
        continue
    visited.add(node)
    mst_cost += weight
    if from_node != -1:
        mst_edges.append((from_node, node, weight))

    for neighbor, w in g[node]:
        if neighbor not in visited:
            heapq.heappush(min_heap, (w, neighbor, node))

# Step 3: Output the result
print("\nMinimum Spanning Tree:")
print("MST Cost:", mst_cost)
print("MST Edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} with weight {w}")
