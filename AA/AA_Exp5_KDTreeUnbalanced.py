class Node:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

def insert(root, point, axis=0):
    if root is None:
        return Node(point, axis)

    if point[axis] < root.point[axis]:
        root.left = insert(root.left, point, (axis + 1) % len(point))
    else:
        root.right = insert(root.right, point, (axis + 1) % len(point))

    return root

def print_tree(node, level=0, side=None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "---- "
        print("   " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

# Sample data points
points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]
# points = [[6, 2, 9], [7, 1, 2], [2, 9, 6], [3, 6, 1], [4, 8, 5], [8, 4, 4], [5, 3, 7], [1, 5, 1], [9, 5, 4]]


# Build KDTree
root = None
for point in points:
    root = insert(root, point)

# Print the tree
print_tree(root)
