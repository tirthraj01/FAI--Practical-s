import heapq

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Calculate heuristic (misplaced tiles)
def heuristic(state):
    return sum(
        1 for i in range(9)
        if state[i] != goal[i] and state[i] != 0
    )

# A* algorithm
def astar():
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        # Check if goal is reached
        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        # Find blank tile
        i = state.index(0)

        # Possible movements
        for move in [-3, 3, -1, 1]:
            j = i + move

            # Check valid movement
            if 0 <= j < 9 and (
                abs(move) == 3 or i // 3 == j // 3
            ):
                new_state = list(state)
                new_state[i], new_state[j] = new_state[j], new_state[i]
                new_state = tuple(new_state)

                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(new_state)

                    heapq.heappush(
                        queue,
                        (new_f, new_g, new_state, path + [new_state])
                    )

    return None

# Display solution
path = astar()

if path:
    print("Solution Found!\n")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Total Moves:", len(path) - 1)

else:
    print("No solution found.")
