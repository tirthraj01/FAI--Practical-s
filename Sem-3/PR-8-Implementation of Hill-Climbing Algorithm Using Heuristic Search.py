# Step 1: Define the heuristic function
def heuristic(x):
    return -(x - 3)**2 + 9


# Step 2: Define Hill-Climbing algorithm
def hill_climbing(start):

    current = start

    # Step 3: Repeat until no better neighbor is found
    while True:

        # Check left and right neighbors
        left = current - 1
        right = current + 1

        # Step 4: Select the better neighbor
        if heuristic(left) > heuristic(right):
            next_state = left
        else:
            next_state = right

        # Step 5: Stop if no improvement is possible
        if heuristic(next_state) <= heuristic(current):
            print("No better neighbor found.")
            break

        # Move to the better state
        print("Move:", current, "->", next_state)
        current = next_state

    return current


# Step 6: Start the algorithm
result = hill_climbing(0)

# Step 7: Display the final result
print("Best state:", result)
print("Maximum value:", heuristic(result))
