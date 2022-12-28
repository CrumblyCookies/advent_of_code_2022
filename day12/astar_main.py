from collections import deque

#testing
import os
import copy
#end

from node import Node
from graph import Graph
from vec import Vec
import consts


# Note:
# lines is [y][x] indexed
lines = open("input.txt", "r").read().split("\n")


#
# Get neighbouring nodes for a given node
def get_neighbours(graph : Graph, node: Node):
    n = []
    n.append(graph.get_node_by_pos(node.x - 1, node.y)) # Left
    n.append(graph.get_node_by_pos(node.x + 1, node.y)) # Right
    n.append(graph.get_node_by_pos(node.x, node.y - 1)) # Up
    n.append(graph.get_node_by_pos(node.x, node.y + 1)) # Down
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
    
    # Ret
    return g


#
# Check path to see if a given node has already been visitied
def already_visited(node : Node, path):
    for n in path:
        if (n.id == node.id):
            return True
    return False


# 
# Get elevation cost of a given node 
def get_elevation_cost(val):
    v = val
    if (v == "S"):
        v = "a"
    if (v == "E"):
        v = "z"
    return consts.alphabet.index(v)


# 
# Can we travel from X to Y
def can_travel_to_neighbour(from_n : Node, to_n : Node):
    cost_from = get_elevation_cost(from_n.value)
    cost_to = get_elevation_cost(to_n.value)
    return (cost_to <= (cost_from + 1)) 


#
# Check closed list for the given node
def does_closed_list_contain_node(node : Node, closed_list):
    for n in closed_list:
        if (n.id == node.id):
            return True
    return False


#
# Rebuild a path given the end node
def reconstruct_path(end_node : Node):
    path = []
    n = end_node
    path.append(n)
    while (n.parent is not None):
        n = n.parent
        path.append(n)
    return path


#
# Debug helper file
def output_to_file(iter, path):

    # Make output
    output = []
    for line in lines:
        this_line = []
        for c in line:
            this_line.append(c)
        output.append(this_line)

    # Adjust output with path
    for node in path:
        output[node.y][node.x] = "@"

    # Make strings
    strings = []
    for line in output:
        string = ""
        for c in line:
            string += c
        strings.append(string)

    # Write
    filename = "./test_output/" + str(iter) + ".txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for line in strings:
            f.write(line + "\n")
    print("Created file: " + filename)


#
# Find all paths
def search(graph : Graph, start : Node, end : Node):

    # A*

    # Create open and closed lists
    open_list = []
    closed_list = []

    # Add start node to open list
    open_list.append(start)

    # Loop until we find the end
    while (len(open_list) > 0):

        open_list.sort(key=lambda x : x.f)
        
        cur_node = open_list[0]
        open_list.pop(0)
        closed_list.append(cur_node)


        # Check for goal
        if (cur_node.value == end.value):
            print("FOUND")
            return reconstruct_path(cur_node)

        # if (iters % 1000 == 0):
        #     print("On iter " + str(iters))

        # if (iters % 10000 == 0):
        #     output_to_file(iters, reconstruct_path(cur_node))

        # Generate children
        # Children of node will equal the current nodes
        cur_node.children = get_neighbours(graph, cur_node)

        # For each child
        for child in cur_node.children:

            child.parent = cur_node

            # If child is on closed_list, continue
            if (does_closed_list_contain_node(child, closed_list)):
                continue

            # If it's invalid to travel to the child, continue
            if (not can_travel_to_neighbour(cur_node, child)):
                continue

            # Create h, g, f values. 
            child.g = cur_node.g + 1
            child.h = Vec.dist(Vec(child.x, child.y), Vec(end.x, end.y))
            child.f = child.g + child.h

            # Add child to open list
            open_list.append(child)

    print("Loop done, path not found.")


# Construct graph from input
graph = construct_graph_from_input(lines)
print("Graph constructed")

# Find paths
start_node = graph.get_node_by_val("S")
end_node = graph.get_node_by_val("E")
print("Start: {" + str(start_node.x) + ", " + str(start_node.y) + "}")
print("End: {" + str(end_node.x) + ", " + str(end_node.y) + "}")

print("Searching...")
path = search(graph, start_node, end_node)

path_str = "Path: " 
for p in path:
    path_str += p.value + ", "
print(path_str)
print ("Length: " + str(len(path)))