# Map Coloring using Backtracking

def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve(graph, colors, assignment, nodes, index):
    if index == len(nodes):
        return True

    node = nodes[index]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            if solve(graph, colors, assignment, nodes, index + 1):
                return True
            del assignment[node]

    return False


# User Input
n = int(input("Enter number of regions: "))
graph = {}

for _ in range(n):
    region = input("Enter region name: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[region] = neighbors

colors = input("Enter available colors separated by space: ").split()

assignment = {}
nodes = list(graph.keys())

if solve(graph, colors, assignment, nodes, 0):
    print("\nColor Assignment:")
    for region in assignment:
        print(region, "->", assignment[region])
else:
    print("No solution found.")
