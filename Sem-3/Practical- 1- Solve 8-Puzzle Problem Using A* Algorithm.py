# Step 1: Import priority queue library
import heapq

# Step 2: Define initial and goal states
# 0 represents the empty space
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Step 3: Heuristic function
# Count tiles that are in the wrong position
def h(state):
    return sum(a != b and a != 0 for a, b in zip(state, goal))

# Step 4: Main A* algorithm
def astar():

    # Store (f, g, current state, path)
    queue = [(h(start), 0, start, [start])]

    # Store already explored states
    visited = set()

    # Step 5: Repeat until queue is empty
    while queue:

        # Select the state with lowest f(n)
        f, g, state, path = heapq.heappop(queue)

        # If goal is reached, return solution
        if state == goal:
            return path

        # Skip already visited states
        if state in visited:
            continue
        visited.add(state)

        # Step 6: Find empty space (0)
        i = state.index(0)

        # Try Up, Down, Left, Right
        for move in [-3, 3, -1, 1]:
            j = i + move

            # Check if the move is valid
            # Vertical moves: +/-3
            # Horizontal moves: same row
            if 0 <= j < 9 and (abs(move) == 3 or i // 3 == j // 3):

                # Convert tuple to list for swapping
                new = list(state)

                # Swap empty space with another tile
                new[i], new[j] = new[j], new[i]

                # Convert list back to tuple
                new = tuple(new)

                # Step 7: Add new state to queue
                if new not in visited:

                    # f(n) = g(n) + h(n)
                    heapq.heappush(queue, (
                        g + 1 + h(new),
                        g + 1,
                        new,
                        path + [new]
                    ))

    # Return None if no solution is found
    return None

# Step 8: Run the A* algorithm
path = astar()

# Print the solution
if path:
    for state in path:

        # Print puzzle in 3x3 format
        for i in range(0, 9, 3):
            print(state[i:i+3])

        print()

    # Initial state is not counted as a move
    print("Total moves:", len(path) - 1)

else:
    print("No solution")
