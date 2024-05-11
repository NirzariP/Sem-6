class Node:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

def print_tree(node, level=0, side=None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "---- "
        print("   " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

# Sample data points
points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 8], [1, 5], [9, 5]]

# Build balanced KDTree
def build_balanced_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # Dimension of the points
    axis = depth % k

    # Sort points based on the axis
    points.sort(key=lambda x: x[axis])

    # Find the median to use as the pivot element
    median_idx = len(points) // 2
    median_point = points[median_idx]

    # Recursively build subtrees using the points before and after the median
    node = Node(median_point, axis)
    node.left = build_balanced_kdtree(points[:median_idx], depth + 1)
    node.right = build_balanced_kdtree(points[median_idx + 1:], depth + 1)

    return node

root = build_balanced_kdtree(points)

# Print the tree
print_tree(root)
