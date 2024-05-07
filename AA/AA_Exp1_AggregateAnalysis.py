arr = [5, 7, 9, 2, 6, 1, 8, 3]

# Initialize stack
stack = []
# Length of the stack
stack_length = 8

# Initialize a list to keep track of units for each operation
units = []
# Initialize operation count
operation_count = 0

# Function to pop an element from the stack
def pop_stack():
    if len(stack) == 0:
        return 
    else:
        top_element = stack[-1]
        stack.pop()

# Function to push an element onto the stack
def push_stack(element):
    global operation_count
    if len(stack) < stack_length:
        operation_count += 1
        stack.append(element)
        print(f"push - 1 unit stack is {stack}")
        # Append 1 unit for the push operation
        units.append(1)
    else:
        return

# Function to pop k elements from the stack
def multi_pop(k):
    global operation_count
    count = 0
    for i in range(k):
        if len(stack) != 0:
            pop_stack()
            operation_count += 1
            count += 1
    return count

for i in arr:
    count = 0
    print(f"For element {i}")
    if i <= len(stack):
        # If the element is less than or equal to the current stack length, perform multipop
        count = multi_pop(i)
        # Append the units for multipop operation
        units.append(count)
        print(f"multipop - {count} unit stack is {stack}")
    # Push the current element onto the stack
    push_stack(i)

# Calculate the total units and operations performed
total_units = sum(units)
print(f"T(n) = {total_units} and n = {operation_count}")
# Calculate the amortized aggregate asymptotic notation
print(f"Amortized aggregate asymptotic notation has complexity as O({total_units // operation_count})")
