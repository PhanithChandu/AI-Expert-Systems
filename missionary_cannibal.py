from collections import deque

# Function to check valid state
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True


def missionaries_cannibals(M, C):
    start = (M, C, 0, 0, 'L')  # (M_left, C_left, M_right, C_right, Boat)
    goal = (0, 0, M, C, 'R')

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        m_left, c_left, m_right, c_right, boat = state

        # Possible moves
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for m, c in moves:
            if boat == 'L':
                new_state = (m_left-m, c_left-c, m_right+m, c_right+c, 'R')
            else:
                new_state = (m_left+m, c_left+c, m_right-m, c_right-c, 'L')

            if is_valid(*new_state[:4]):
                queue.append((new_state, path))

    return None


# User Input
M = int(input("Enter number of Missionaries: "))
C = int(input("Enter number of Cannibals: "))

solution = missionaries_cannibals(M, C)

# Output
if solution:
    print("\nSteps to reach goal:\n")
    for step in solution:
        print(step)
else:
    print("No solution possible.")
