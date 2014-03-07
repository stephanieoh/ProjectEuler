import fileinput
import math

l=[];

for line in fileinput.input():
	l.append(line)

N = int(l[0])
#for i in xrange(0, int(l[0])):
#	print int(l[2][i])

squeek = l[1].split()
sequence = [int(i) for i in squeek]


prog = (sequence[N-1] - sequence[0])/N
half = int(math.floor(N/2))

#print sequence[half]
#print sequence[0] + (prog * half)
#print sequence[half]==sequence[0] + prog * half
#print half
while N > 2:
	#missing something in first half of sequence the following will be True
	if sequence[half] > sequence[0] + prog * half:
		#since something is missing in the first half, only look at first half of sequence
		#print "hey"
		sequence = sequence[:half+1]
	#missing something in the second half of sequence the following will be True
	elif sequence[half] == sequence[0] + prog * half:
		#since something is missing int he second half, only look at second half of sequence
		sequence = sequence[half:]
	else:
		sequence = sequence[:N-1]
	N = len(sequence)
	half = int(math.floor(N/2))
	#print sequence
	#print half
print (sequence[1]+sequence[0])/2


#print sequence[half] > sequence[0] + prog* half

#print N/2 * prog	+ sequence[0]
