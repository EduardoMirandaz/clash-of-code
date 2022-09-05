def removeDuplicates(s):
    chars = []
    prev = None
 
    for c in s:
        if prev != c:
            chars.append(c)
            prev = c
 
    return ''.join(chars)

s = removeDuplicates(''.join(sorted(input())))
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
for letra_alfabeto in alfabeto:
    for letra in s:
        if(letra == letra_alfabeto):
            count+=1
print(26-count)


