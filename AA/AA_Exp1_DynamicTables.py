
# Not in Portion



class DynamicTable:
    def __init__(self):
        self.capacity = 1  # Initial capacity
        self.size = 0
        self.table = [None] * self.capacity

    # Function to insert values
    def insert(self, value):
        if self.size == self.capacity:
            # If table is full, double the capacity
            self._resize(self.capacity * 2)
        else:
            self.doubling_copy = 0
        self.table[self.size] = value
        self.size += 1

    # Function to double the size
    def _resize(self, new_capacity):
        new_table = [None] * new_capacity
        for i in range(self.size):
            new_table[i] = self.table[i]
        self.table = new_table
        self.capacity = new_capacity

    # Function to print table
    def print_table(self):
        print(self.table)

    # Function to calculate cost
    def cost_calculation(self):
        insertion_cost = 1
        amortized_cost = 3
        doubling_copying = 0 
        total_cost = insertion_cost + doubling_copying
        bank_balance = amortized_cost - total_cost
        size = 1 # Doubling size
        previous_size = 1  # To calculate Doubling Copying cost
        print("i\tP.S\tS\tD.C\tI\tT.C\tAm.C\tBank")
        for i in range(1,self.size+1):
            if i < size:
                print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{total_cost}\t{amortized_cost}\t{bank_balance}")
                previous_size = size
                doubling_copying = previous_size - size
                total_cost = insertion_cost + doubling_copying
                bank_balance = amortized_cost - total_cost + bank_balance
            else:
                print(f"{i}\t{previous_size}\t{size}\t{doubling_copying}\t{insertion_cost}\t{total_cost}\t{amortized_cost}\t{bank_balance}")
                previous_size = size
                size = size * 2
                doubling_copying = size - previous_size
                total_cost = insertion_cost + doubling_copying
                bank_balance = amortized_cost - total_cost + bank_balance


table = DynamicTable()
for i in range(1, 16):
    table.insert(i)
    print(f"Inserted {i}. Table:")
    table.print_table()
print("Cost Calculation:")
table.cost_calculation()