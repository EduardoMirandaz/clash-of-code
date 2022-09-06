# Given a string t and a number n you must output the unscrambled string.

# A string is unscrambled by swapping every n:th character with the character to the left of it.
# Input
# Line 1: A scrambled string t.
# Line 2: An integer n.
# Output
# Line 1 : The unscrambled string.
# Constraints
# 2 ≤ t ≤ 999
# 2 ≤ n ≤ 10
# Example
# Input
# ehll oowlrd
# 2
# Output
# hello world

# ['T', 'i', 'h', 's', 'i', ' ', 's', 'a', ' ', ' ', 'o', 'l', 'n', 'e', 'g', 'r', 's', ' ', 'e', 't', 'n', 'e', 'c', 'n', 'e', '.']

# ['H', 'e', 'l', 'o', 'L', ' ', 'w', 'o', 'l', 'R', 'D']

entrada = list(input())
n = int(input())
nl = []
for i in range(len(entrada)):
    if((i+1)%n == 0):
        nl.pop()
        nl.append(entrada[i])
        nl.append(entrada[i-1])
    else:
        nl.append(entrada[i])
print("".join(nl))
