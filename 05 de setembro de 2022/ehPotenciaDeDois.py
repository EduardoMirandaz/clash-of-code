# A power of 2 is a number of the form 2^а, where а is an integer.

# Example:
# 2^4 = 2*2*2*2 = 16
# Therefore 16 is a power of 2

# You must output if a given number n is a power of 2.
# Input
# Line 1: An integer n representing the number.
# Output
# Line 1 : "true" if n is a power of 2 and "false" if it isn't.
# Constraints
# 1<=n<=2147483647
# Example
# Input
# 8
# Output
# true  

print('true' if bin(int(input())).count('1') == 1 else 'false')

