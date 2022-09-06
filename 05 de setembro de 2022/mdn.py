# Find the sum of arithmetic progression of N members starting with first member M.

# Arithmetic progression is a sequence, in which every member differs from other by D. For example, sequence where M=3 and D=3 looks like this
# 3,6,9,12,...
# Input
# Line 1: Three integers M D N
# Output
# Line 1: The sum of the progression
# Constraints
# 1≤ M ≤ 1000
# 1≤ D ≤ 1000
# 1≤ N ≤ 100
# Example
# Input
# 3 3 5
# Output
# 45

m,d,n=[int(i) for i in input().split()]
print(sum(range(m, (d*n)+m, d)))
