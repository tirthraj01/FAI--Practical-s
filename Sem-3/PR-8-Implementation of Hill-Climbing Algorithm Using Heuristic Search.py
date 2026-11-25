# Define heuristic function
def heuristic(x):
    return -(x - 3) ** 2 + 9

# Hill Climbing algorithm
def hill_climbing(start):
    current = start

    print("Initial State:", current)

    while True:
        # Find neighboring states
        left = current - 1
        right = current + 1

        # Select the better neighbor
        if heuristic(left) > heuristic(right):
            next_state = left
        else:
            next_state = right

        # Stop if no better neighbor exists
        if heuristic(next_state) <= heuristic(current):
            print("No better neighbor found.")
            break

        # Move to the better state
        print("Move:", current, "->", next_state)
        current = next_state

    return current

# Run the algorithm
result = hill_climbing(0)

print("\nBest State:", result)
print("Maximum Value:", heuristic(result))
