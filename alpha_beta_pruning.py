def alphabeta(depth, node_index, alpha, beta, is_max, scores, height):
    # If leaf node
    if depth == height:
        return scores[node_index]

    if is_max:
        best = -999999

        for i in range(2):
            value = alphabeta(
                depth + 1,
                node_index * 2 + i,
                alpha,
                beta,
                False,
                scores,
                height
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break   # Beta cut-off

        return best

    else:
        best = 999999

        for i in range(2):
            value = alphabeta(
                depth + 1,
                node_index * 2 + i,
                alpha,
                beta,
                True,
                scores,
                height
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break   # Alpha cut-off

        return best


# -------- Driver Code --------
import math

n = int(input("Enter number of leaf nodes (power of 2): "))

scores = []
print("Enter leaf node values:")
for _ in range(n):
    scores.append(int(input()))

height = int(math.log2(n))

result = alphabeta(0, 0, -999999, 999999, True, scores, height)

print("Optimal value for MAX player:", result)
