import math

def primef(n):
	l = [];
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
	return l

def divisorsf(n):
	r=[];
	m=0;
	p=1;
 	l = primef(n)
	for x in xrange(0,len(l)-1):
		m+=1
		if l[x]!=l[x+1]:
			r.append(m+1)
			m=0;
	r.append(m+2)
	for x in xrange(0,len(r)):
		p*=r[x]
	return p


target=500
n=1
T=1
while divisorsf(T) < target:
	n+=1
	T=n*(n+1)/2
	if divisorsf(T) >= target:
		print T