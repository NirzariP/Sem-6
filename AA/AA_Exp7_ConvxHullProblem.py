import math
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def graham_scan(points):
    n = len(points)
    if n < 3:
        return []
    
    min_point = min(points, key=lambda x: (x[1], x[0]))
    sorted_points = sorted(points, key=lambda x: (math.atan2(x[1] - min_point[1], x[0] - min_point[0]), x))
    stack = [sorted_points[0], sorted_points[1], sorted_points[2]]
    print("Stack after adding first 3 points:", stack)

    for i in range(3, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])
        print("Stack after adding point", sorted_points[i], ":", stack)
    return stack

points = [(0, 3), (2, 2), (1, 1),(4,4), (1, 2),(3,1), (0, 0), (3, 3),(1,-1)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)