# Step 1: Create the game tree
tree = [
    [[3, 5], [6, 9]],     # Left MIN node
    [[1, 2], [0, -1]]     # Right MIN node
]

# Step 2: Define Alpha-Beta Pruning
def alpha_beta(node, is_max, alpha, beta):

    # Step 3: If node is a leaf, return its value
    if isinstance(node, int):
        print("Visited leaf:", node)
        return node

    # Step 4: MAX player tries to get maximum value
    if is_max:
        best = float("-inf")

        for i in range(len(node)):
            value = alpha_beta(node[i], False, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Check whether pruning is possible
            if alpha >= beta:
                print("Pruned branch:", node[i+1:])
                break

        return best

    # Step 5: MIN player tries to get minimum value
    else:
        best = float("inf")

        for i in range(len(node)):
            value = alpha_beta(node[i], True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Check whether pruning is possible
            if beta <= alpha:
                print("Pruned branch:", node[i+1:])
                break

        return best


# Step 6: Call the function
result = alpha_beta(tree, True, float("-inf"), float("inf"))

# Step 7: Display the final result
print("Optimal value:", result)
