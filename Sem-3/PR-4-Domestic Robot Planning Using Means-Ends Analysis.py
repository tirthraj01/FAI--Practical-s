
# Step 1: Define initial state
places = {"A": [3, 2, 1], "B": [], "C": []}
steps = 0

# Step 2: Operator to move a block
def move(source, target):
    global steps

    # Pick the top block
    block = places[source][-1]

    # Check whether the move is valid
    if places[target] and places[target][-1] < block:
        print("Invalid Move")
        return

    # Move block to target
    places[target].append(places[source].pop())

    steps += 1
    print("Step", steps, ": Move Block", block,
          "from", source, "to", target)
    print(places)

# Step 3: Means-Ends planning
def mea(n, source, target, temp):

    # Stop if no blocks are left to move
    if n == 0:
        return

    # Move smaller blocks to temporary place
    mea(n-1, source, temp, target)

    # Move the largest remaining block
    move(source, target)

    # Move smaller blocks to target
    mea(n-1, temp, target, source)

# Step 4: Execute the plan
print("Initial State:", places)
mea(3, "A", "C", "B")

# Step 5: Display final state
print("Goal State:", places)
print("Total Moves:", steps)
