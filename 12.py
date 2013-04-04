import math

def primef(n,l):
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

def divisorsf(n,l):
	r=[];
	m=0;
	p=0;
	primef(n,l)
	print len(l)
	for x in xrange(0,len(l)-1):
		m+=1
		if l[x]!=l[x+1]:
			r.append(m+1)
			m=0;
	for x in xrange(0,len(r)):
		p*=r[x]
	return p





l=[];
n=1;
while len(l)<=5:
	l=[];
	T=n*(n+1)/2
	divisorsf(T,l)
	n+=1

print T
print l




