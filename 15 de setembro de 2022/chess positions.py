# Chess is a game played on a 8x8 board. Columns are named with letters a through h and rows are named with integers 1 through 8.

# In a single move, a bishop can move along a diagonal any number of squares.

# Given a bishop's position P, output the number of legal moves a bishop can make from this square.

# Example:
# From the square b2, a bishop can go to one of the following squares:
# a1, c3, d4, e5, f6, g7, h8, c1, a3
# Thus, the total number of legal moves is 9
# Input
# P: Position of bishop
# Output
# The number of legal moves the bishop can make
# Constraints
# Example
# Input
# b2
# Output
# 9

ent = input()
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
indices = ['1', '2', '3', '4', '5', '6', '7','8']

tab = []
for i, letra in enumerate(letras):
    nl = []
    for j, indice in enumerate(indices):
        nl.append(letra + indice)
    tab.append(nl)

pos = [int( indices[letras.index(ent[0])])-1, int(ent[1])-1]
posicoes_possiveis = []

for i in range(8):
    for j in range(8):
        if( (i+j == sum(pos) or abs(i-j) == abs(pos[0]-pos[1])) and (i != pos[0] and j != pos[1])):
            posicoes_possiveis.append([i,j])

# Printando a tabela
for i in tab:
    print(i)

#Exibindo as posicoes possíveis
for posicao in posicoes_possiveis:
    print(tab[posicao[0]][posicao[1]], end=', ')

#Exibindo o output esperado, quantas sao as possicoes possiveis:
print('posicoes possíveis:', len(posicoes_possiveis))
