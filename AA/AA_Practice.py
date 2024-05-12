# Accounting Using DT
insertion_cost = 1
doubling_copying = 0
amortized_cost = 3
total_cost = insertion_cost + doubling_copying
size = 1
previous_size = 1
bank_balance = amortized_cost - total_cost

n = int(input("Enter number of elements: "))
print("i\tP.S\tS\tI\tD.C\tAm.c\tT.C\tBank Balance")

for i in range(1, n+1):
    if i < size:
        print(f"{i}\t{previous_size}\t{size}\t{insertion_cost}\t{doubling_copying}\t{amortized_cost}\t{total_cost}\t{bank_balance}")
        previous_size = size
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost + bank_balance
    else:
        print(f"{i}\t{previous_size}\t{size}\t{insertion_cost}\t{doubling_copying}\t{amortized_cost}\t{total_cost}\t{bank_balance}")
        previous_size = size
        size = size * 2
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost + bank_balance





# Potential Function Using DT
insertion_cost = 1
doubling_copying = 0
total_cost = insertion_cost + doubling_copying
ci = total_cost
size = 1
previous_size = 1
phi = 1
previous_phi = 0
amortized_cost = ci + phi - previous_phi
final_amortized_cost = 0

n = int(input("Enter number of elements: "))
print("i\tS\tP.S\tI\tD.C\tCi\tP.Phi\tPhi\t Am.C")
print(f"{1}\t{size}\t{previous_size}\t{insertion_cost}\t{doubling_copying}\t{ci}\t{previous_phi}\t{phi}\t{amortized_cost}")

for i in range(2, n+1):
    if i <= size:
        previous_size = size
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        ci = total_cost
        previous_phi = phi
        phi = 2 * i - size
        amortized_cost = ci + phi - previous_phi
        final_amortized_cost = final_amortized_cost + amortized_cost
        print(f"{i}\t{size}\t{previous_size}\t{insertion_cost}\t{doubling_copying}\t{ci}\t{previous_phi}\t{phi}\t{amortized_cost}")
    else:
        previous_size = size
        size = size * 2
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        ci = total_cost
        previous_phi = phi
        phi = 2 * i - size
        amortized_cost = ci + phi - previous_phi
        final_amortized_cost = final_amortized_cost + amortized_cost
        print(f"{i}\t{size}\t{previous_size}\t{insertion_cost}\t{doubling_copying}\t{ci}\t{previous_phi}\t{phi}\t{amortized_cost}")

final_amortized_cost = final_amortized_cost / n
print("Amortized cost: ", round(final_amortized_cost + 0.5) if final_amortized_cost % 1 >= 0.5 else round(final_amortized_cost - 0.5))





# Aggregate Analysis
arr = [5, 7, 9, 2, 6, 1, 8, 3]

stack_length = len(arr)
stack = []
units = []
operation_count = 0

def pop_stack():
    if len(stack) == 0:
        return
    else:
        top_element = stack[-1]
        stack.pop()

def push_stack(element):
    global operation_count
    if len(stack) < stack_length:
        operation_count += 1
        stack.append(element)
        print(f"push 1 - unit, stack: {stack}")
        units.append(1)
    else:
        return
    
def multipop(k):
    global operation_count
    count = 0
    for i in range(k):
        if len(stack) != 0:
            operation_count += 1
            count += 1
            pop_stack()
    return count

for i in arr:
    count = 0
    print(f"For element {i}")
    if i <= len(stack):
        count = multipop(i)
        units.append(count)
        print(f"multipop {count} - unit, stack: {stack}")
    push_stack(i)

total_units = sum(units)
print(f"T(n) = {total_units} and n = {operation_count}")
print(f"Amortized aggregate asymptotic notation has complexity as O({total_units // operation_count})")





# Hiring Problem - Sorted Order
candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates", candidates)
interviewed_candidates = []
hired_candidates = []

for candidate in candidates:
    interviewed_candidates.append(candidate)
    if not hired_candidates or candidate > max(hired_candidates):
        hired_candidates.append(candidate)

firing_cost = len(hired_candidates) - 1
print("Interviewed Candidates", interviewed_candidates)
print("Hired Candidates", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)





# Hiring Problem - Randomized Order
import random
candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates", candidates)
interviewed_candidates = []
hired_candidates = []

for i in range(len(candidates)):
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)

max = -1
for i in range(len(interviewed_candidates)):
    if interviewed_candidates[i] > max:
        max = interviewed_candidates[i]
        hired_candidates.append(interviewed_candidates[i])

firing_cost = len(hired_candidates) - 1
print("Interviewed Candidates", interviewed_candidates)
print("Hired Candidates", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)





# Randomized Quicksort
import random
c1, c2 = 0, 0
def randomized_quicksort(arr):
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c1 += len(left) + len(right)
        return randomized_quicksort(left) + middle + randomized_quicksort(right)
    
def quicksort(arr):
    global c2
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2 += 1
            else:
                right.append(arr[i])
                c2 += 1
        return quicksort(left) + [pivot] + quicksort(right)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print("Regualr Quick Sort")
print(quicksort(arr))
print("Comparisons" ,c2)

print("Randomized Quick Sort:")
print(randomized_quicksort(arr))
print("Comparisons :", c1)





# KD Tree Unbalanced
class Node():
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

def insert(root, point, axis = 0):
    if root is None:
        return Node(point, axis)
    
    if point[axis] < root.point[axis]:
        root.left = insert(root.left, point, (axis + 1) % len(point))
    else:
        root.right = insert(root.right, point, (axis + 1) % len(point))
    return root

def print_tree(node, level = 0, side = None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "----"
        print("  " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]

root = None
for point in points:
    root = insert(root, point)

print_tree(root)





# KD Tree Unbalanced
class Node():
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

def print_tree(node, level = 0, side = None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "----"
        print("  " * level + prefix + str(node.point))
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")

points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 8], [1, 5], [9, 5]]

def build_balanced_kdtree(points, depth = 0):
    if not points:
        return
    
    k = len(points[0])
    axis = depth % k

    points.sort(key = lambda x: x[axis])

    median_idx = len(points) // 2
    median_point = points[median_idx]

    node = Node(median_point, axis)
    node.left = build_balanced_kdtree(points[:median_idx], depth + 1)
    node.right = build_balanced_kdtree(points[median_idx + 1:], depth + 1)
    return node

root = build_balanced_kdtree(points)

print_tree(root)





# Convex Hull Graham Scan
import math
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(points):
    n = len(points)
    if n < 3:
        return []
    
    min_point = min(points, key = lambda x: (x[1], x[0]))
    sorted_points = sorted(points, key = lambda x: (math.atan2(x[1] - min_point[1], x[0] - min_point[0]), x))
    stack = [sorted_points[0], sorted_points[1], sorted_points[2]]
    print("Stack after adding 3 points: ", stack)

    for i in range(3, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])
        print(f"After adding points: {sorted_points[i]} stack: {stack}")
    return stack

points = [(0, 3), (2, 2), (1, 1),(4,4), (1, 2),(3,1), (0, 0), (3, 3),(1,-1)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)