'''
Graph from links - Create a program that will create a graph or network from a series of links.
'''

# def checkNode(node, graph):
#     '''Checks whether a node is in a graph'''
#     if node in graph:
#         return(True)
#     else:
#         return (False)
        
# def fromLinks(links):
#     '''
#     Takes a list of links in the form of tuples, or lists, 
#     with two elements describing the connected nodes and returns a graph in the form of a dictionary.
    
#     Exampple input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]
    
#     Example output (fm input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
#     '''
#     ## set up an empty dictionary
#     graph = {}
#     ##iterate thru the input nodes
#     for link in links:
#         ##Check if each node is in the graph, if it isnt add it.
#         for node in link:
#             if not checkNode(node, graph):
#                 graph[node] = []
#         ##for both ends of the node add the link to the other
#         graph[link[0]].append(link[1])
#         graph[link[1]].append(link[0])
#     return graph
# ##tests

# assert(fromLinks([(1,2),(1,4),(2,3),(3,4)]) == {1:[2,4],2:[1,3],3:[2,4],4:[1,3]})
# assert(fromLinks([[1,2],[1,4],[2,3],[3,4]]) == {1:[2,4],2:[1,3],3:[2,4],4:[1,3]})

#---------------------------------------------------------------------------

'''
Eulerian Path - Create a program which will take as an input a graph and output either a Eulerian path or a Eulerian cycle, or state that it is not possible. A Eulerian Path starts at one node and traverses every edge of a graph through every node and finishes at another node. A Eulerian cycle is a eulerian Path that starts and finishes at the same node.
'''

'''
Connected Graph - Create a program which takes a graph as an input and outputs whether every node is connected or not.
'''

# from copy import copy

# '''

# 	is_connected - Checks if a graph in the form of a dictionary is 
# 	connected or not, using Breadth-First Search Algorithm (BFS)


# '''
# def is_connected(G):
# 	start_node = list(G)[0]
# 	color = {v: 'white' for v in G}
# 	color[start_node] = 'gray'
# 	S = [start_node]
# 	while len(S) != 0:
# 		u = S.pop()
# 		for v in G[u]:
# 			if color[v] == 'white':
# 				color[v] = 'gray'
# 				S.append(v)
# 			color[u] = 'black'
# 	return list(color.values()).count('black') == len(G)

# '''
# 	odd_degree_nodes - returns a list of all G odd degrees nodes
# '''
# def odd_degree_nodes(G):
# 	odd_degree_nodes = []
# 	for u in G:
# 		if len(G[u]) % 2 != 0:
# 			odd_degree_nodes.append(u)
# 	return odd_degree_nodes

# '''
# 	from_dict - return a list of tuples links from a graph G in a 
# 	dictionary format
# '''	
# def from_dict(G):
# 	links = []
# 	for u in G:
# 		for v in G[u]:
# 			links.append((u,v))
# 	return links

# '''
# 	fleury(G) - return eulerian trail from graph G or a 
# 	string 'Not Eulerian Graph' if it's not possible to trail a path
# '''
# def fleury(G):
# 	'''
# 		checks if G has eulerian cycle or trail
# 	'''
# 	odn = odd_degree_nodes(G)
# 	if len(odn) > 2 or len(odn) == 1:
# 		return 'Not Eulerian Graph'
# 	else:
# 		g = copy(G)
# 		trail = []
# 		if len(odn) == 2:
# 			u = odn[0]
# 		else:
# 			u = list(g)[0]
# 		while len(from_dict(g)) > 0:
# 			current_vertex = u
# 			for u in g[current_vertex]:
# 				g[current_vertex].remove(u)
# 				g[u].remove(current_vertex)
# 				bridge = not is_connected(g)
# 				if bridge:
# 					g[current_vertex].append(u)
# 					g[u].append(current_vertex)
# 				else:
# 					break
# 			if bridge:
# 				g[current_vertex].remove(u)
# 				g[u].remove(current_vertex)
# 				g.pop(current_vertex)
# 			trail.append((current_vertex, u))
# 	return trail

# # testing seven bridges of konigsberg
# print('Konigsberg')
# G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
# print(fleury(G))

# # testing an eulerian cycle
# print('1st Eulerian Cycle')
# G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
# print(fleury(G))

# # testing another eulerian cycle
# print('2nd Eulerian Cycle')
# G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
# print(fleury(G))

# # testing an eulerian trail
# print('Eulerian Trail')
# G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
# print(fleury(G))

# ******************************************************

## IMPLEMENTATION #2
# from collections import defaultdict
 
# # This class represents a undirected graph using adjacency list representation
 
 
# class Graph:
 
#     def __init__(self, vertices):
#         self.V = vertices  # No. of vertices
#         self.graph = defaultdict(list)  # default dictionary to store graph
 
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
 
#     # A function used by isConnected
#     def DFSUtil(self, v, visited):
#         # Mark the current node as visited
#         visited[v] = True
 
#         # Recur for all the vertices adjacent to this vertex
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.DFSUtil(i, visited)
 
#     '''Method to check if all non-zero degree vertices are
#     connected. It mainly does DFS traversal starting from 
#     node with non-zero degree'''
 
#     def isConnected(self):
 
#         # Mark all the vertices as not visited
#         visited = [False]*(self.V)
 
#         #  Find a vertex with non-zero degree
#         for i in range(self.V):
#             if len(self.graph[i]) != 0:
#                 break
 
#         # If there are no edges in the graph, return true
#         if i == self.V-1:
#             return True
 
#         # Start DFS traversal from a vertex with non-zero degree
#         self.DFSUtil(i, visited)
 
#         # Check if all non-zero degree vertices are visited
#         for i in range(self.V):
#             if visited[i] == False and len(self.graph[i]) > 0:
#                 return False
 
#         return True
 
#     '''The function returns one of the following values
#        0 --> If graph is not Eulerian
#        1 --> If graph has an Euler path (Semi-Eulerian)
#        2 --> If graph has an Euler Circuit (Eulerian)  '''
 
#     def isEulerian(self):
#         # Check if all non-zero degree vertices are connected
#         if self.isConnected() == False:
#             return 0
#         else:
#             # Count vertices with odd degree
#             odd = 0
#             for i in range(self.V):
#                 if len(self.graph[i]) % 2 != 0:
#                     odd += 1
 
#             '''If odd count is 2, then semi-eulerian.
#             If odd count is 0, then eulerian
#             If count is more than 2, then graph is not Eulerian
#             Note that odd count can never be 1 for undirected graph'''
#             if odd == 0:
#                 return 2
#             elif odd == 2:
#                 return 1
#             elif odd > 2:
#                 return 0
 
#      # Function to run test cases
 
#     def test(self):
#         res = self.isEulerian()
#         if res == 0:
#             print("graph is not Eulerian")
#         elif res == 1:
#             print("graph has a Euler path")
#         else:
#             print("graph has a Euler cycle")
 
 
# # Let us create and test graphs shown in above figures
# g1 = Graph(5)
# g1.addEdge(1, 0)
# g1.addEdge(0, 2)
# g1.addEdge(2, 1)
# g1.addEdge(0, 3)
# g1.addEdge(3, 4)
# g1.test()
 
# g2 = Graph(5)
# g2.addEdge(1, 0)
# g2.addEdge(0, 2)
# g2.addEdge(2, 1)
# g2.addEdge(0, 3)
# g2.addEdge(3, 4)
# g2.addEdge(4, 0)
# g2.test()
 
# g3 = Graph(5)
# g3.addEdge(1, 0)
# g3.addEdge(0, 2)
# g3.addEdge(2, 1)
# g3.addEdge(0, 3)
# g3.addEdge(3, 4)
# g3.addEdge(1, 3)
# g3.test()
 
# # Let us create a graph with 3 vertices
# # connected in the form of cycle
# g4 = Graph(3)
# g4.addEdge(0, 1)
# g4.addEdge(1, 2)
# g4.addEdge(2, 0)
# g4.test()
 
# # Let us create a graph with all vertices
# # with zero degree
# g5 = Graph(3)
# g5.test()
#---------------------------------------------------------------------------

'''
Dijkstra’s Algorithm - Create a program that finds the shortest path through a graph using its edges.
'''

# import sys
 
 
# class Graph():
 
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]]
 
#     def printSolution(self, dist):
#         print("Vertex \tDistance from Source")
#         for node in range(self.V):
#             print(node, "\t\t", dist[node])
 
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minDistance(self, dist, sptSet):
 
#         # Initialize minimum distance for next node
#         min = sys.maxsize
 
#         # Search not nearest vertex not in the
#         # shortest path tree
#         for u in range(self.V):
#         	if dist[u] < min and sptSet[u] == False:
#         		min = dist[u]
#         		min_index = u

#         return min_index
 
#     # Function that implements Dijkstra's single source
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):
 
#         dist = [sys.maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
 
#         for cout in range(self.V):
 
#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # x is always equal to src in first iteration
#             x = self.minDistance(dist, sptSet)
 
#             # Put the minimum distance vertex in the
#             # shortest path tree
#             sptSet[x] = True
 
#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             for y in range(self.V):
#                 if self.graph[x][y] > 0 and sptSet[y] == False and \
#                         dist[y] > dist[x] + self.graph[x][y]:
#                     dist[y] = dist[x] + self.graph[x][y]
 
#        self.printSolution(dist)
 
 
# # Driver's code
# if __name__ == "__main__":
#     g = Graph(9)
#     g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#                [4, 0, 8, 0, 0, 0, 0, 11, 0],
#                [0, 8, 0, 7, 0, 4, 0, 0, 2],
#                [0, 0, 7, 0, 9, 14, 0, 0, 0],
#                [0, 0, 0, 9, 0, 10, 0, 0, 0],
#                [0, 0, 4, 14, 10, 0, 2, 0, 0],
#                [0, 0, 0, 0, 0, 2, 0, 1, 6],
#                [8, 11, 0, 0, 0, 0, 1, 0, 7],
#                [0, 0, 2, 0, 0, 0, 6, 7, 0]
#                ]
#     g.dijkstra(0)

#---------------------------------------------------------------------------


'''
Minimum Spanning Tree - Create a program which takes a connected, undirected graph with weights and outputs the minimum spanning tree of the graph i.e., a subgraph that is a tree, contains all the vertices, and the sum of its weights is the least possible.
'''

# # Class to represent a graph 
# class Graph: 
  
#     def __init__(self, vertices): 
#         self.V = vertices 
#         self.graph = [] 
  
#     # Function to add an edge to graph 
#     def addEdge(self, u, v, w): 
#         self.graph.append([u, v, w]) 
  
#     # A utility function to find set of an element i 
#     # (truly uses path compression technique) 
#     def find(self, parent, i): 
#         if parent[i] != i: 
  
#             # Reassignment of node's parent 
#             # to root node as 
#             # path compression requires 
#             parent[i] = self.find(parent, parent[i]) 
#         return parent[i] 
  
#     # A function that does union of two sets of x and y 
#     # (uses union by rank) 
#     def union(self, parent, rank, x, y): 
  
#         # Attach smaller rank tree under root of 
#         # high rank tree (Union by Rank) 
#         if rank[x] < rank[y]: 
#             parent[x] = y 
#         elif rank[x] > rank[y]: 
#             parent[y] = x 
  
#         # If ranks are same, then make one as root 
#         # and increment its rank by one 
#         else: 
#             parent[y] = x 
#             rank[x] += 1
  
#     # The main function to construct MST 
#     # using Kruskal's algorithm 
#     def KruskalMST(self): 
  
#         # This will store the resultant MST 
#         result = [] 
  
#         # An index variable, used for sorted edges 
#         i = 0
  
#         # An index variable, used for result[] 
#         e = 0
  
#         # Sort all the edges in 
#         # non-decreasing order of their 
#         # weight 
#         self.graph = sorted(self.graph, 
#                             key=lambda item: item[2]) 
  
#         parent = [] 
#         rank = [] 
  
#         # Create V subsets with single elements 
#         for node in range(self.V): 
#             parent.append(node) 
#             rank.append(0) 
  
#         # Number of edges to be taken is less than to V-1 
#         while e < self.V - 1: 
  
#             # Pick the smallest edge and increment 
#             # the index for next iteration 
#             u, v, w = self.graph[i] 
#             i = i + 1
#             x = self.find(parent, u) 
#             y = self.find(parent, v) 
  
#             # If including this edge doesn't 
#             # cause cycle, then include it in result 
#             # and increment the index of result 
#             # for next edge 
#             if x != y: 
#                 e = e + 1
#                 result.append([u, v, w]) 
#                 self.union(parent, rank, x, y) 
#             # Else discard the edge 
  
#         minimumCost = 0
#         print("Edges in the constructed MST") 
#         for u, v, weight in result: 
#             minimumCost += weight 
#             print("%d -- %d == %d" % (u, v, weight)) 
#         print("Minimum Spanning Tree", minimumCost) 
  
  
# # Driver code 
# if __name__ == '__main__': 
#     g = Graph(4) 
#     g.addEdge(0, 1, 10) 
#     g.addEdge(0, 2, 6) 
#     g.addEdge(0, 3, 5) 
#     g.addEdge(1, 3, 15) 
#     g.addEdge(2, 3, 4) 
  
#     # Function call 
#     g.KruskalMST() 

