
# Turn an input name into a palindrome using this simple concept:

# Take a name like "Abe Simpson" and alternate each letter with the reverse name "nospmiS ebA" to get:

# Abe Simpson +
# nospmiS ebA =
# Anboes pSmiimSp seobnA

# Now you have your name Palindromified!

# Take an input string (name) and Palindromify it!
# Input
# A single line: A string representing a name
# Output
# A single line: The Palindromified name (formed by reading characters alternately from left and right).
# Constraints
# Input names will have no double whitespace characters.
# Example
# Input
# Rihanna
# Output
# RainhnaanhniaR

a = list(input())
s=''
for i in range(len(a)):
    s+=a.pop() if i%2 else a.pop(0)
print(s+s[::-1])
