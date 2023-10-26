p = True
q = True

if p and q:
    print('p and q True')
else:
    print('p and q False')

#OR
if p or q:
    print('p or q True')
else:
    print('p and q False')

a=2
b=3

if a == b:
    print('a=b')
else:
    print('not a=b')

s1='abc'
s2='abc'

# not equal
if s1 != s2:
    print('s1!=s2')

y = 100 if s1==s2 else 10
print(y)

#swith operator for multiple cases

mv = 500

match mv:
    case 100:
            print('mv=100')
    case 200:
            print('mv=200')
    case _:
            print('mv is different')