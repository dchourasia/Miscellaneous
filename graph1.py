class node:
	def __init__(self, val):
		self.data = val
		self.list = {} # node index : wt
		
class graph:
	def __init__(self):
		self.nodes = []
		
	def addNodes(self, values):
		for val in values:
			self.nodes.append(node(val))
	 
	def addEdges(self, node, edges):
	 	for edge in edges:
	 		self.nodes[node].list[edge] = 1
	 		self.nodes[edge].list[node] = 1
	 		
	def dfs(self, idx, covered=[]):
		print(idx, self.nodes[idx].data)
		covered.append(idx)
		for n in self.nodes[idx].list:
			if n not in covered:
				self.dfs(n, covered)
				
	def bfs(self, idx):
	 	queue = [idx]
	 	covered = [idx]
	 	
	 	while queue:
	 		n = queue.pop(0)
	 		print(n, self.nodes[n].data)
	 		#covered.append(n)
	 		for x in self.nodes[n].list:
	 			if x not in covered:
	 				queue.append(x)
	 				covered.append(x)
	 	
	 		
	 		
g = graph()
g.addNodes([2, 5, 9, 12, 32, 42, 13, 23])
g.addEdges(0, [1, 3, 5])
g.addEdges(1, [2, 4, 6])
g.addEdges(2, [3, 5, 7])
g.addEdges(3, [4, 6, 3])
g.dfs(0)
print()
g.bfs(0)


			
