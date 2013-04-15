f = open('text.txt')
lines = f.readlines()

words = ''.join(lines).split()
s=0
for i in xrange(0,100):
	s+=long(words[i])

print s
