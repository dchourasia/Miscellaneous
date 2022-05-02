# adjency matrix == a 2d list of nxn size,wheren is total elements in graph, each value in the array stores a number representing weightage of tbe connection between 2 elements

# l[i][j]  = m
# m = 0 , no connection
# m= 1, connectiom with normal.weight
# m = w, connection qith w weight
'''
adjecency list == a dict where
key = index of the node
value =  list of nodes connect with the node
value can be a dict as well where we store weight of the connection
'''
from collections import defaultdict
class node:
	def __init__(self, val):
		self.data = val
		self.adList = {}
		
class graph:
	 def __init__(self):
	 	self.nodes = []
	 
	 def add_node(self, value):
	 	self.nodes.append(node(value))
	 def add_nodes(self, *values):
	 	for value in values:
	 		self.nodes.append(node(value))
	 	
	 def add_edge(self, x, y, w=1):
	 	self.nodes[x].adList[y] = w
	 	self.nodes[y].adList[x] = w
	 	
	 def add_edges(self, x, y, w=1):
	 	
	 	self.nodes[x].adList = {idx :w for idx in y}
	 	for idx in y:
	 		self.nodes[idx].adList[x] = w
	 def bfs(self, s):
	 	l = len(self.nodes)
	 	traversed = [False]*l
	 	queue = [self.nodes[s]]
	 	traversed[s] = True
	 	
	 	while queue:
	 		n = queue.pop(0)
	 		print(n.data)
	 		
	 		for c in n.adList:
	 			if not traversed[c]:
	 				queue.append(self.nodes[c])
	 				traversed[c] = True
	 	
	 def dfs(self, s, traversed=[]):
	 	if not traversed:
	 		traversed = [False]*len(self.nodes)
	 	#if not traversed[s]:
	 	traversed[s] = True
	 	print(self.nodes[s].data)
	 	for c in self.nodes[s].adList:
	 		if not traversed[c]:
	 			self.dfs(c, traversed)
	 		
	 		
	 	
	 	
	 	
	 	
g = graph()
g.add_nodes(10, 12, 15, 9, 17, 25, 21, 75, 23)
g.add_edges(0, [1, 4])
g.add_edges(1, [0, 4, 2, 3])
g.add_edges(2, [1, 3])
g.add_edges(3, [1, 4, 2])
g.add_edges(4, [3, 0, 1])

g.bfs(2)

print('dfs')
g.dfs(2)


	

