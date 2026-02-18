# Simple solution for the Water Jug Problem

def water_jug_problem():
    visited = set()
    stack = [(0, 0)]  # (jug4, jug3)

    while stack:
        jug4, jug3 = stack.pop()
        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))
        print(f"4-gallon jug: {jug4} | 3-gallon jug: {jug3}")

        if jug4 == 2:
            print("\nGoal achieved! 4-gallon jug has exactly 2 gallons.")
            return

        # Possible actions
        actions = set()
        actions.add((4, jug3))                # Fill 4-gallon jug
        actions.add((jug4, 3))                # Fill 3-gallon jug
        actions.add((0, jug3))                # Empty 4-gallon jug
        actions.add((jug4, 0))                # Empty 3-gallon jug

        # Pour from 4 -> 3
        pour = min(jug4, 3 - jug3)
        actions.add((jug4 - pour, jug3 + pour))

        # Pour from 3 -> 4
        pour = min(jug3, 4 - jug4)
        actions.add((jug4 + pour, jug3 - pour))

        stack.extend(actions)

water_jug_problem()
