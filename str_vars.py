s = 'abcdefghij'
print(s)
print(len(s))
print(s[1:3])
print(s[3])
print(s[:3])
print(s[3:])

print('-----------')

ab = 0b1001

print(ab)

ax = 0x6a

print(ax)

a = 8
b = 3

c = a / b
print(type(c))
print(c)

#module division - rest of division

d = a % b
print(type(b))
print(b)


# stings

S1 = 'abcdefghijk'

print(S1)
print(len(S1))
print(S1[3])  # result d
print(S1[:3]) #result abc
print(S1[-3:]) #result ijk
print(S1[5:8]) #result fgh

s2 = "I can't"
print(s2)

s3 = 'I can\'t "Pawel"'
s3 = "I can't \"Pawel\""

print(s3)

s4='abcsd\nfagwrqgqg'
print(s4)

s5 = 'avabba\tbacc'
print(s5)

print(ord('a'))
print(ord('A'))
print(ord('L')) #returns a the unicode equivalent

s8 = 'ababab'
print('count ab: %s' % s8.count('ab')) # count character in a string



