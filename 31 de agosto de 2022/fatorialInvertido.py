#dado um numero descubra qual fatorial o originou
v = int(input())
c = 1
while(v>1):
    c+=1
    v/=c
print(c)
