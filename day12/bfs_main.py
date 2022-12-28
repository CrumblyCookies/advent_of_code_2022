# This is a very, very slow solution. 
#
# It uses BFS to find all possible 
# paths, and then sorts the paths 
# to find the shortest one. 
#
# It scales very poorly and will take 
# a lot of time to find the answer.
# 
# I recommend that you do *not* run this!

from collections import deque

from node import Node
from graph import Graph
import consts


# Note:
# lines is [y][x] indexed
lines = open("input.txt", "r").read().split("\n")


#
# Get neighbouring nodes for a given node
def get_neighbours(graph, x, y):
    n = []
    n.append(graph.get_node_by_pos(x - 1, y)) # Left
    n.append(graph.get_node_by_pos(x + 1, y)) # Right
    n.append(graph.get_node_by_pos(x, y - 1)) # Up
    n.append(graph.get_node_by_pos(x, y + 1)) # Down
    filtered = [i for i in n if i is not None] # Filter the None
    return filtered


#
# Create Graph object from input
def construct_graph_from_input(input):
    cur_id = 0
    g = Graph()
    wid = len(input[0])

    # Make all the nodes
    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            val = input[y][x]
            n = Node(cur_id, val, x, y)
            g.add_node(n)
            cur_id += 1

    # Setup their neighbours
    for node in g.nodes:
        ns = get_neighbours(g, node.x, node.y)
        for n in ns:
            node.add_neighbour(n)
    
    # Ret
    return g


#
# Check path to see if a given node has already been visitied
def already_visited(node, path):
    for n in path:
        if (n.id == node.id):
            return True
    return False


# 
# Get elevation cost of a given node 
def get_elevation_cost(val):
    if (val == "S"):
        val = "a"
    if (val == "E"):
        val = "z"
    return consts.alphabet.index(val)


# 
# Can we travel from X to Y
def can_travel_to_neighbour(from_n, to_n):
    cost_from = get_elevation_cost(from_n.value)
    cost_to = get_elevation_cost(to_n.value)
    return (cost_to <= (cost_from + 1)) 


#
# Find all paths
def bfs(graph, start, end):

    # Store current paths being explored
    q = deque()
    
    # Current path
    path = []
    path.append(start)
    q.append(path.copy())

    # Store all of the possible paths to the destination
    all_possible_paths = []

    # 
    while q:

        # Path to explore
        path = q.popleft()

        # End of this path
        last = path[len(path)-1]

        # If last node is desired destination, we're done
        if (last.value == end.value):
            all_possible_paths.append(path.copy())
            continue

        # Traverse neighbours
        for next in last.neighbours:

            if (can_travel_to_neighbour(last, next)):

                if (not already_visited(next, path)):
                    new_path = path.copy()
                    new_path.append(next)
                    q.append(new_path)

    # All have been found
    return all_possible_paths


# Construct graph from input
graph = construct_graph_from_input(lines)

# Find paths
start_node = graph.get_node_by_val("S")
end_node = graph.get_node_by_val("E")
completed_paths = bfs(graph, start_node, end_node)

# Get shortest
shortest_path = None
for path in completed_paths:
    if (shortest_path is None or len(path) < len(shortest_path)):
        shortest_path = path

print (len(shortest_path))