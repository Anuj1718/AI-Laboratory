class A_star:
	def __init__(self):
		self.nodes = {}
		self.heuristics = {}

	def add_node(self, node, heuristic):
		self.nodes[node] = []
		self.heuristics[node] = heuristic

	def add_edge(self, node1, node2, cost):
		self.nodes[node1].append((node2, cost))
		self.nodes[node2].append((node1, cost))

	def get_neighbors(self, node):
		return self.nodes.get(node, [])

	def a_star_algo(self, start, goal):
		open_set = {start}
		closed_set = set()
		g = {start: 0}
		parents = {start: start}
		while open_set:
			n = None
			for v in open_set:
				if n is None or g[v] + self.heuristics[v] < g[n] + self.heuristics[n]:
					n = v

			if n is None:
				print(f'No Path Exists')
				return None

			if n == goal:
				path = []
				while parents[n] != n:
					path.append(n)
					n = parents[n]
				path.append(start)
				print(f'Path Found: {path}')
				return path

			for neighbor, cost in self.get_neighbors(n):
				if neighbor not in open_set and neighbor not in closed_set:
					open_set.add(neighbor)
					parents[neighbor] = n
					g[neighbor] = g[n] + cost
				else:
					if g[neighbor] > g[n] + cost:
						parents[neighbor] = n
						g[neighbor] = g[n] + cost
						if neighbor in closed_set:
							closed_set.remove(neighbor)
							open_set.add(neighbor)
			open_set.remove(n)
			closed_set.add(n)
		print(f'No Path exists')
		return None


def main():
	graph = A_star()
	node_count = int(input("Enter No. of nodes: "))
	for count in range(node_count):
		node, heuristic = input("Enter node and its heuristic separated by space: ").split()
		graph.add_node(node, int(heuristic))

	edge_count = int(input("Enter No. of Edges: "))
	for count in range(edge_count):
		node1, node2, cost = input("Add The node whose between there is and edge and its cost: ").split()
		graph.add_edge(node1, node2, int(cost))

	start_node = input("Enter starting Node: ")
	goal = input("Enter Goal Node: ")
	print(graph.a_star_algo(start_node, goal))


if __name__ == "__main__":
	main()