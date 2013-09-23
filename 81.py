f = open('matrix.txt')
lines = f.readlines()

words = ''.join(lines).split()
list = []
for x in words:
	list.append(x.split(','))
x=[1234,'1234']
print x



for number in xrange(1,80):
	list[0][number] = int(list[0][number-1])+int(list[0][number])
	list[number][0] = int(list[number-1][0])+int(list[number][0])

for line in xrange(1,80):
	for number in xrange(1,80):
		if int(list[line][number-1])<int(list[line-1][number]):
			list[line][number] = int(list[line][number-1]) + int(list[line][number])
		else:
			list[line][number] = int(list[line-1][number]) + int(list[line][number])

print list[79][79]