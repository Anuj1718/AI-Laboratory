#2 approaches to implement DFS in python, one using recursion and the other using a stack.
# The recursive approach is more elegant and easier to read, while the stack approach is more explicit and can be easier to understand for those who are not familiar with recursion.
# The stack approach is also more efficient in terms of memory usage, as it does not require the overhead of function calls and stack frames.

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

visited = set() 

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root) #
        for neighbour in graph[root]: 
            dfs(visited, graph, neighbour) #recursive approach

dfs(visited, graph, 'A')
