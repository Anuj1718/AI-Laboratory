import heapq

# Step 1: Build the graph with weights
g = {}
n = int(input("Enter the number of edges: "))
print("Enter edges (format: a b weight):")

for i in range(n):
    a, b, w = map(int, input().split())  # read edge: from a to b with weight w
    if g.get(a) is None:
        g[a] = [] # If vertex a is not already in the graph dictionary, it creates an empty list for it, Adds vertex b and weight w to a's adjacency list.
    g[a].append((b, w))

    if g.get(b) is None:
        g[b] = []
    g[b].append((a, w))  # undirected graph

# Step 2: Prim's Algorithm
start_node = next(iter(g))  # Start from any node
visited = set()
min_heap = [(0, start_node, -1)]  # (weight, current_node, from_node) 
mst_cost = 0 # Total cost of the MST
mst_edges = [] # List to store edges in the MST
# The min_heap is a priority queue that stores tuples of (weight, current_node, from_node).
# A priority queue storing tuples (weight, current_node, from_node).
# Initially contains the start_node with weight 0 and from_node = -1 (since there's no parent yet).
                                                                    
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

# Continues while there are nodes to process.

# removes and returns the element with the lowest weight from the min_heap (a priority queue), and unpacks it into three variables: weight, current_node, and from_node.
# If the current node is already visited, it skips to the next iteration to avoid cycles.
# Adds the current node to the visited set.
# If the from_node is not -1 (meaning it's not the starting node), it adds the edge to the mst_edges list.
# Updates the total cost of the MST by adding the weight of the edge connecting from_node to current_node.
# The from_node is the parent of the current node in the MST.
# For each unvisited neighbor of the current node, it pushes the neighbor and its weight into the min_heap.


# Step 3: Output the result
print("\nMinimum Spanning Tree:")
print("MST Cost:", mst_cost)
print("MST Edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} with weight {w}")
