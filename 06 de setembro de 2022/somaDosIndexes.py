# You get a character c and a string s.
# Your task is to print the sum of all indexes of c in s. The index of the first character is 0!
# Example:
# c = o
# s = hello world
# "o" is the fifth and the eighth character: Index 4 + Index 7 = 11
# Input
# Line 1: A character c
# Line 2: A string s
# Output
# Line 1: The sum of all indexes of c in s. Pay attention on UPPER- and lowercase.
# Constraints
# Length of c = 1
# 1 ≤ length of s ≤ 200
# Example
# Input
# e
# hello
# Output
# 1

c = input()
s = input()
a = 0
for i,l in enumerate(s):
    if(l==c):a+=i
print(a)

# c = input()
# s = list(input())
# sum = 0
# while(c in s):
#     i = s.index(c)
#     sum+=i
#     s[i] = '#'
# print(sum)

