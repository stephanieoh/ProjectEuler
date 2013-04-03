import math

n=int(raw_input('What number do you want the prime factorization of? '))

def primef(n):
	l=[];
	m=n;
	i=2;
	while i<=int(math.ceil(math.sqrt(n)))+1:
		if n%i==0:
			n/=i
			l.append(i)
		else:
			i+=1
	if n!=1:
		l.append(n)
	if len(l)==1:
		print m,
		print 'is prime'
	else: 
		print m,
		print 'has',
		print len(l),
		print 'prime factors and they are: ',
		print l 

primef(n)
			