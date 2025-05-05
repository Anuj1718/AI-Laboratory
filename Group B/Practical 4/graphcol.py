# The **graph coloring problem** is a classic problem in graph theory where the goal is to assign colors to the vertices of a graph such that **no two adjacent vertices share the same color**. The main objective is usually to **minimize the number of colors used**.

# ### Formally:

# * Given a graph $G = (V, E)$, assign a color to each vertex $v \in V$.
# * Constraint: For every edge $(u, v) \in E$, the colors of $u$ and $v$ must be different.
# * Goal: Use the **minimum number of colors** (called the **chromatic number** of the graph).

# ### Example:

# If you have a triangle graph (3 vertices, all connected), you need 3 different colors — one for each vertex.

# ### Applications:

# * Register allocation in compilers
# * Scheduling problems
# * Map coloring (e.g., coloring regions on a map such that no two adjacent regions have the same color)
# * Frequency assignment in mobile networks
# * Sudoku solving

# * Graph coloring is NP-hard, meaning that no polynomial-time algorithm is known to solve all instances of the problem efficiently.
 
m = int(input("Enter number of max colors: "))

g= {}

n = int(input("Enter the number of edges: "))

for i in range(n):
    a,b = map(int, input().split()) #Reads two integers a and b, representing an edge between vertex a and vertex b
    if g.get(a) is None: # If vertex a is not already in the graph dictionary, it creates an empty list for it, Adds vertex b to a's adjacency list.
        g[a] = []
    g[a].append(b)  #This line always runs, regardless of the if condition. # It adds vertex b to a's adjacency list.
    if g.get(b) is None: #Same logic for vertex b, making sure the graph is undirected by also adding a to b’s adjacency list.
        g[b] = []
    g[b].append(a)

print(g)

possibleColors = ["red", "blue", "green", "yellow", "orange", "purple"] # List of possible colors to be used for coloring the graph.

def canColor(g,n,col,colList): # Function to check if the current vertex n can be colored with color i.
    for child in g[n]: # Iterates through the adjacency list of vertex n.
        if colList[child] == possibleColors[col]: # If the color of the adjacent vertex is the same as the current color, return False.
            return False # This stops the function if False is returned
    return True # If no adjacent vertex has the same color, return True.
        

def graphColoring(g,m,v,n,colList):
    if n == v: # Base case: If n equals the number of vertices, it means we have successfully colored all vertices.
        return True # This stops the function if True is returned

    for col in range(m):
        if(canColor(g,n,col,colList)): # Checks if the current vertex n can be colored with color i.
            colList[n] = possibleColors[col]
            if graphColoring(g,m,v,n+1,colList) == True: # n represents the current vertex we are attempting to color.# why n+1? because we are checking the next vertex. ## If the recursive call returns True, it means we have successfully colored all vertices.
                return True  # This stops the function if True is returned
            colList[n] = -1  # This executes only if the recursive call fails (i.e., if False is returned)

colList = {} # Dictionary to store the color assigned to each vertex.

for i in g.keys():
    colList[i] = -1 # Initializes the color of each vertex to -1 (indicating no color assigned yet).


if graphColoring(g,m,len(g.keys()),0,colList): # Calls the graphColoring function with the graph, number of colors, number of vertices, starting vertex (0), and the color list.
    print("Graph can be colored with", m, "colors") 
    for i in g.keys():
        print("Vertex", i, "is colored with color", colList[i]) # Prints the color assigned to each vertex.
else:
    print("Graph cannot be colored with", m, "colors")




# input():
# Reads a line of input from the user as a string.

# Example:
# If the user types:

# Copy code
# 1 2
# then input() returns the string '1 2'.

# 🔹 .split():
# Splits that string into a list of substrings using whitespace as the default separator.

# '1 2'.split() → ['1', '2']


# 0 1
# 0 2
# 0 3
# 1 2
# 2 3
# 3 4
# This is basic test case for the graph coloring problem.