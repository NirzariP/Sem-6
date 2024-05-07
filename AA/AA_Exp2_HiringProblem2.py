# Best Candidate comes last - Sorted Rank of Candidates
candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates: ",candidates)
interviewed_candidates = []
hired_candidates = []

# Interview candidates in order
for candidate in candidates:
    interviewed_candidates.append(candidate)

    # Hire the best candidate so far
    if not hired_candidates or candidate > max(hired_candidates):
        hired_candidates.append(candidate)

# Calculate firing cost
firing_cost = len(hired_candidates) - 1   # Since the last candidate is the best

print("Interviewed candidates:", interviewed_candidates)
print("Hired candidates:", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)