d=0
T=1
n=1
while d<=500:
	d=0
	T=n*(n+1)/2
	for x in xrange(1,T):
		if T%x==0:
			d+=1;
	n+=1
	print T

print T