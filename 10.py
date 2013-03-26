import math
import time
start= time.clock()


def isprime(n):
	if n<2:
		return False
	elif n==2:
		return True
	else:
		for x in xrange(2, int(math.ceil(math.sqrt(n)))+1):
			if n%x==0:
				return False
	return True

def prime(n):
	list=[];
	i=0;
	while len(list)<n:
		if isprime(i):
			list.append(i)
		i+=1
	return list[n-1]

s=0
n=1
while n<2000000:
	if isprime(n):
		s+=n
	n+=1

print s
		 
end= time.clock()
time= (end-start)/1000
print time
