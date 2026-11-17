import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Heuristic: count misplaced tiles
def h(state):
    return sum(a != b and a != 0 for a, b in zip(state, goal))

def astar():
    queue = [(h(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        i = state.index(0)

        for move in [-3, 3, -1, 1]:
            j = i + move

            if 0 <= j < 9 and (abs(move) == 3 or i // 3 == j // 3):
                new = list(state)
                new[i], new[j] = new[j], new[i]
                new = tuple(new)

                if new not in visited:
                    heapq.heappush(queue, (g + 1 + h(new), g + 1, new, path + [new]))

    return None

path = astar()

if path:
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Total moves:", len(path) - 1)
else:
    print("No solution")
