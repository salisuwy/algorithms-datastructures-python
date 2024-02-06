#  COLLAB NOTEBOOK 
#  [Link]: https://colab.research.google.com/drive/1TE5XvQSBMXrKCGpL0Hte-A2ZdGj1JUdD?usp=sharing

import heapq
from collections import deque
def find_path_djikstra(vertices, edges, start, end):
  graph, costs = generate_graph_cost(vertices, edges)
  visited = set()
  priority_queue = []
  heapq.heapify(priority_queue)
  costs[start] = (0, None)
  heapq.heappush(priority_queue, (0, start))

  while priority_queue:
    cost, node = heapq.heappop(priority_queue)
    visited.add(node)
    for adjacent_node, adjacent_cost in graph[node]:
      if adjacent_node not in visited:
        final_cost = adjacent_cost + cost
        if final_cost < costs[adjacent_node][0]:
          costs[adjacent_node] = (final_cost, node)
        heapq.heappush(priority_queue, (costs[adjacent_node][0], adjacent_node))

  print("********* A to F *******", costs[end])
  path = deque()
  route = end
  while route:
    path.appendleft(route)
    _, route = costs[route]

  print("********* Route *******", path)  
    
  
def generate_graph_cost(vertices, edges):
  graph = {}
  costs = {}
  for from_node, to_node, cost in edges:
    if from_node not in graph:
      graph[from_node] = []
      costs[from_node] = (float("inf"), None)
    if to_node not in graph:
      graph[to_node] = []
      costs[to_node] = (float("inf"), None)
    graph[from_node].append((to_node, cost))
    graph[to_node].append((from_node, cost))

  return graph, costs

def kruskall_spanning_tree(vertices, edges):
  graph, _ = generate_graph_cost(vertices, edges)
  parent = [i for i in range(len(vertices))]

  def find_parent(node):
    node_index = vertices.index(node)
    if parent[node_index] == node_index:
      return node
    return find_parent(vertices[parent[node_index]])

  def union_node(node1, node2):
    p_node1 = find_parent(node1)
    p_node2 = find_parent(node2)
    if p_node1 != p_node2:
      parent[vertices.index(node1)] =       vertices.index(p_node2)

  queue = []
  heapq.heapify(queue)
  
  for from_node, to_node, cost in edges:
    heapq.heappush(queue, (cost, from_node, to_node))

  tree = []
  visited = set()
  
  while queue and len(visited) < len(vertices):
    cost, from_node, to_node = heapq.heappop(queue)
    print("------Inside------", from_node, to_node, cost)
    if find_parent(from_node) != find_parent(to_node):
      print("_____EXECUTED_____")
      union_node(from_node, to_node)
      visited.add(from_node)
      tree.append((from_node, to_node, cost))
  
  print(tree)



vertices = ["A", "B", "C", "D", "E", "F"]
edges = [
  ["A", "B", 15],
  ["A", "C", 5],
  ["A", "D", 10],
  ["B", "C", 3],
  ["D", "C", 4],
  ["B", "E", 9],
  ["C", "E", 2],
  ["E", "F", 7],
  ["B", "F", 17]
]


# Using the Dijkstra algorithm
find_path_djikstra(vertices, edges, "A", "F")

# Using spanning Krusckall Spanning Tree algorithm
kruskall_spanning_tree(vertices, edges)
