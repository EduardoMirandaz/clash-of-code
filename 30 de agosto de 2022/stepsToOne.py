# The Collatz conjecture is a opened mathematics problem: 
# given a number N, the repetition of the following operation will always 
# eventually reach the loop 1 ⇒ 4 ⇒2 ⇒1 ...

# * If N is even, N becomes N/2
# * If N is odd, N becomes 3*N+1

# Can you try it with the given numbers and print the number of steps it took to reach 1?


## Solução com loop
# n = int(input())
# c=0
# while(n!=1):
#     n = 3*n + 1 if n % 2 else n/2
#     c+=1
# print(c) 


# Solução com recursão
def loop(n, count):
    n = n/2 if n % 2 == 0 else 3*n + 1
    print(count+1) if n == 1 else loop(n, count+1) 

n = int(input())
loop(n, 0)

