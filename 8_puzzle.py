import heapq

# Goal State
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Directions for movement (row, col)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Puzzle:
    def __init__(self, state, parent=None, move="", g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # Cost so far
        self.h = self.manhattan()
        self.f = self.g + self.h

    # Manhattan Distance Heuristic
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def __lt__(self, other):
        return self.f < other.f


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_children(node):
    children = []
    x, y = get_blank_position(node.state)

    for dx, dy in MOVES:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in node.state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

            children.append(Puzzle(tuple(map(tuple, new_state)),
                                   node,
                                   move=(new_x, new_y),
                                   g=node.g + 1))
    return children


def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent

    path.reverse()

    print("\nSolution Steps:\n")
    for step in path:
        for row in step:
            print(row)
        print()


def a_star(start_state):
    open_list = []
    closed_set = set()

    start_node = Puzzle(start_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == GOAL:
            print_solution(current)
            return

        closed_set.add(current.state)

        for child in generate_children(current):
            if child.state not in closed_set:
                heapq.heappush(open_list, child)

    print("No solution found.")


# --------- MAIN ---------
if __name__ == "__main__":
    start = ((1, 2, 3),
             (4, 0, 6),
             (7, 5, 8))

    a_star(start)
