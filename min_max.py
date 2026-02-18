def minimax(depth, node_index, is_max, scores, height):
    # If leaf node is reached
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )


# -------- Driver Code --------
import math

n = int(input("Enter number of leaf nodes (power of 2): "))

scores = []
print("Enter leaf node values:")
for _ in range(n):
    scores.append(int(input()))

height = int(math.log2(n))

result = minimax(0, 0, True, scores, height)

print("Optimal value for MAX player:", result)
