from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
  def __init__(self, directed=False):
    self.adj_list = {}
    self.directed = directed

  def add_edge(self, u, v):
    if u not in self.adj_list: self.adj_list[u] = set()
    if v not in self.adj_list: self.adj_list[v] = set()

    self.adj_list[u].add(v)

    if not self.directed:
      self.adj_list[v].add(u)
    
  def getBFS(self, start_node):
    if start_node not in self.adj_list:
      return []

    queue = deque([start_node])
    visited = {start_node}
    result = []

    while queue:
      current = queue.popleft()
      result.append(current)

      for neighbor in self.adj_list[current]:
        if neighbor not in visited:
          queue.append(neighbor)
          visited.add(neighbor)
    
    return result

  def getDFS(self, start_node):
    if start_node not in self.adj_list:
      return []

    result = []
    visited = set()

    def dfs(node):
      if node not in self.adj_list or node in visited:
        return

      result.append(node)
      visited.add(node)
      for child in self.adj_list[node]:
        dfs(child)
    
    dfs(start_node)

    return result
  
  def visualize(self):
    """Creates a visual representation of the current graph state."""
    # 1. Choose the correct NetworkX graph type based on our class property
    if self.directed:
      nx_graph = nx.DiGraph()
    else:
      nx_graph = nx.Graph()

    # 2. Populate the NetworkX graph with our adjacency list
    for node, neighbors in self.adj_list.items():
      for neighbor in neighbors:
        nx_graph.add_edge(node, neighbor)

    # 3. Create a new figure (prevents overlap if you call visualize() multiple times)
    plt.figure(figsize=(6, 4))

    # 4. Draw the graph
    pos = nx.spring_layout(nx_graph)
    nx.draw(
      nx_graph, 
      pos, 
      with_labels=True, 
      node_color='lightblue', 
      edge_color='gray', 
      node_size=2000, 
      font_weight='bold',
      arrows=self.directed  # NetworkX handles the arrow drawing automatically if True
    )
    
    plt.title("Graph Visualization")
    plt.show()

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'A')
graph.add_edge('C', 'D')
graph.add_edge('D', 'B')
graph.add_edge('D', 'C')
graph.add_edge('D', 'E')
graph.add_edge('E', 'B')
graph.add_edge('E', 'D')

print("Graph 1")
for key, val in graph.adj_list.items():
  print(f"{key}: {val}")

print(f"BFS of Graph 1: {graph.getBFS('A')}")
print(f"DFS of Graph 1: {graph.getDFS('A')}")

print()

print("Graph 2")
graph1 = Graph(directed=True)
graph1.add_edge('A', 'B')
graph1.add_edge('A', 'D')
graph1.add_edge('B', 'E')
graph1.add_edge('B', 'C')
graph1.add_edge('D', 'C')
graph1.add_edge('C', 'E')
graph1.add_edge('E', 'F')
graph1.add_edge('F', 'G')

for key, val in graph1.adj_list.items():
  print(f"{key}: {val}")

print(f"BFS of Graph 2: {graph1.getBFS('A')}")
print(f"DFS of Graph 2: {graph1.getDFS('A')}")

print()

print("Graph 3")
graph2 = Graph(directed=True)
graph2.add_edge('A', 'B')
graph2.add_edge('A', 'C')
graph2.add_edge('B', 'D')
graph2.add_edge('B', 'E')
graph2.add_edge('C', 'F')
graph2.add_edge('D', 'G')
graph2.add_edge('E', 'F')
graph2.add_edge('F', 'G')

for key, val in graph2.adj_list.items():
  print(f"{key}: {val}")

print(f"BFS of Graph 3: {graph2.getBFS('A')}")
print(f"DFS of Graph 3: {graph2.getDFS('A')}")