# Implementing BFS
import collections

def bfs(graph, root): #root as in start element
    visited = set() #
    queue = collections.deque([root]) #queue = [root], this is not an ideal way to implement a queue in python, but it works for this example.  

    while queue: #while queue is not empty
        vertex = queue.popleft() #pop the first element from the queue
        visited.add(vertex) #add the vertex to the visited set 
        for i in graph[vertex]: #for each element in the graph at the vertex
            if i not in visited: #if the element is not in the visited set
                queue.append(i) #append the element to the queue

    print(visited)

if __name__ == "__main__": # This is a common Python idiom that allows you to run code only if the script is executed directly, not when it is imported as a module.

    # Dictionary representation of the graph
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 4],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }
    bfs(graph, 0)


# 💡 Summary:
# Term	Meaning	Python Method
# deque	A double-ended queue	collections.deque()
# Enqueue	Add to end	append()
# Dequeue	Remove from front	popleft()