def depth_first_search(neighbour_list, root_node):
  visited_nodes = set()
  stack = [root_node]
  while stack:
    node = stack.pop()
    if node not in visited_nodes:
      visited_nodes.add(node)
      stack.extend(set(neighbour_list[node]) - visited_nodes)
  return list(visited_nodes)