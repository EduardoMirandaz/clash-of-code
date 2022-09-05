n = int(input())
for i in range(n):
    s = []
    [s.append(int(i)) for i in input() ]
    if(sum(s[:3]) == sum(s[3:])):
        print('true')
    else:
        print('false')    
