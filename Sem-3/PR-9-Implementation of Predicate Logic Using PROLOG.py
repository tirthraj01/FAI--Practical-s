# Predicate Logic

# Parent relationships
parent = [
    ("john", "mary"),
    ("john", "bob"),
    ("mary", "alice"),
    ("bob", "sam")
]

# Gender
male = ["john", "bob", "sam"]
female = ["mary", "alice"]

# Check father
def father(x, y):
    return (x, y) in parent and x in male

# Check mother
def mother(x, y):
    return (x, y) in parent and x in female

# Check sibling
def sibling(x, y):
    for a, b in parent:
        for c, d in parent:
            if b == x and d == y and a == c and x != y:
                return True
    return False

# Check grandparent
def grandparent(x, y):
    for a, b in parent:
        for c, d in parent:
            if a == x and b == c and d == y:
                return True
    return False

# Display results
print("Father:", father("john", "mary"))
print("Mother:", mother("mary", "alice"))
print("Sibling:", sibling("mary", "bob"))
print("Grandparent:", grandparent("john", "alice"))
