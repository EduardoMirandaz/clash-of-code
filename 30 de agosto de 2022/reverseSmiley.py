#     The game mode is REVERSE: 
# You do not have access to the statement. 
# You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input   :)
# Expected output :)

# 02 Test 2
# Input :))
# Expected output Oh no!

# 03 Test 3
# Input ::))
# Expected output :):)

smiley = input()

if(smiley.count(':') == smiley.count(')') or smiley.count(':') == smiley.count('(')):
    print(':)'*smiley.count(':'))
else:
    print('Oh no!')

