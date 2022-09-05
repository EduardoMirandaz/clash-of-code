# The goal is to reformat a sequence of integers, 
# so that each pair is separated by a number of points ('.') 
# equal to the number on the left.
# Input
# Line 1: An integer sequence T
# Output
# Line 1: A string containing the sequence of integers, T, separated by the correct number of '.'s


# Constraints
# 1 ≤ Length_of_T ≤ 50
# 0 ≤ Element_of_T ≤ 500

# Example
# Input

# 5
# 1 2 3 4 5

# Output
# 1.2..3...4....5

len_t = int(input())
lista = [int(i) for i in input().split()]
while(lista):
    i = lista.pop(0)
    print(i, end='')
    if(len(lista) != 0):
        print('.'*i, end='')