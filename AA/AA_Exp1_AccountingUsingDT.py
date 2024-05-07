insertion_cost = 1  # Initializing Insertion cost
amortized_cost = 3  # Initializing Amortized cost
doubling_copying = 0  # Initializing Doubling Copying cost to 0
total_cost = insertion_cost + doubling_copying  # Calculating Total Cost
bank_balance = amortized_cost - total_cost  # Calculating Bank Balance
size = 1 # Doubling size
previous_size = 1  # To calculate Doubling Copying cost

# P.s --> Previous size
# S --> Size
# D.C --> Doubling Copying cost
# I --> Insertion cost
# T.C --> Total cost
# Am.C --> Amortized cost
# Bank  --> Bank Balance
print("i\tP.S\tS\tD.C\tI\tT.C\tAm.C\tBank")
for i in range(1,16):
    if i < size:
        print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{total_cost}\t{amortized_cost}\t{bank_balance}\t")
        previous_size = size
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost + bank_balance
    else:
        print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{total_cost}\t{amortized_cost}\t{bank_balance}\t")
        previous_size = size
        size = size * 2
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost + bank_balance