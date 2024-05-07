insertion_cost = 1
doubling_copying = 0
total_cost = insertion_cost + doubling_copying
ci = total_cost
size = 1
previous_size = 1
phi = 1
previous_phi = 0
amortized_cost =  ci + phi - previous_phi
final_amortized_cost = 0

n = int(input("Enter number of elements to be inserted: "))

print("i\tP.S\tS\tD.C\tI\tci\tPhi\tP.Phi\tAm.C")
print(f"{1}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{ci}\t{phi}\t{previous_phi}\t{amortized_cost}\t")
for i in range(2, n+1):
    if i <= size:
        previous_size = size
        doubling_copying = previous_size - size
        total_cost = insertion_cost + doubling_copying
        ci = total_cost
        previous_phi = phi
        phi = 2 * i - size
        amortized_cost =  ci + phi - previous_phi
        final_amortized_cost = final_amortized_cost + amortized_cost
        print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{ci}\t{phi}\t{previous_phi}\t{amortized_cost}\t")
    else:
        previous_size = size
        size = size * 2
        doubling_copying = size - previous_size
        total_cost = insertion_cost + doubling_copying
        ci = total_cost
        previous_phi = phi
        phi = 2 * i - size
        amortized_cost =  ci + phi - previous_phi
        final_amortized_cost = final_amortized_cost + amortized_cost
        print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{ci}\t{phi}\t{previous_phi}\t{amortized_cost}\t")

final_amortized_cost = final_amortized_cost / n
print("Amortized cost: ", round(final_amortized_cost + 0.5) if final_amortized_cost % 1 >= 0.5 else round(final_amortized_cost - 0.5))

# P.s --> Previous size
# S --> Size
# D.C --> Doubling Copying cost
# I --> Insertion cost
# T.C --> Insertion cost
# Am.C --> Amortized cost
# Phi --> Phi
# P.Phi  --> Previous Phi