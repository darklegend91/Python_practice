
from collections import defaultdict , deque

# Kosaraju's algorithm
#Directed [Start , end ]
n = 8
A = [[0,1] , [1,2] , [0,3] , [3,4] , [3,6] , [3,7] , [4,2] , [4,5] ,[5,2]]

#Convert to Adjancy matrix
# M = []

# for i in range (n):
#     M.append([0] * n)

# for j in range(n):
#     for u , v in A:
#         M[u][v] = 1
    
# print("adjacency matrix is : " , M)
    
#Convert to Adjancy List

adj_list = defaultdict(list)

for u , v in A:
    adj_list[u].append(v)
    
# print("Adjacency list is: " , adj_list)


# ======================================DFS======================================
# DFS on a graph which have a time and space complexity of O(V + E) where v is vertices and e is number of edges

# This is a recusrive function that will go through all the nodes one by one untill all nodes in that adjacanecy list is fully interated.
# def dfs_recursive(node):
#     print(node)

#     for nei_node in adj_list[node]:
#         if nei_node not in seen:
#             seen.add(nei_node)
#             dfs_recursive(nei_node)

# source = 0
# seen = set()
# seen.add(source)
# dfs_recursive(source)

# This stores all the nodes currectly visited in stack and then go through them one by one
# DFS - Iterative approach using stack
# source = 0
# seen = set()
# seen.add(source)
# stack = [source]

# while stack:
#     node = stack.pop()
#     print(node)
    
#     for nei_node in adj_list[node]:
#         if nei_node not in seen:
#             seen.add(nei_node)
#             stack.append(nei_node)

# ======================================BFS======================================
source = 0

# # seen set made and source added
# seen = set()
# seen.add(source)

# # queue made and osurce added
# q = deque()
# q.append(source)

# while q:
#     node = q.popleft()
#     print(node)
#     for nei_node in adj_list[node]:
#         seen.add(nei_node)
#         q.append(nei_node)
    
# Graph node class
class Node:
    def __init__(self , value):
        self.value = value
        self.neighbours = []
    
    def __str__(self):
        return self.value
    
    def display(self):
        connections = [node.value for node in self.neighbours]
        return f"{self.value} is connected to {connections}"
    

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbours.append(B)
B.neighbours.append(A)

C.neighbours.append(D)
D.neighbours.append(C)

print(A.display())
print(B.display())
print(C.display())
print(D.display())