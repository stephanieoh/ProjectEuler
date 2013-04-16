
m=[]
for n in xrange(1,1000000):
	l=[n]
	d=n
	if n==1:
		m.append(len(l))
	else:
		while n>=d:
			if n%2==0:
				n/=2
				l.append(n)
			else:
				n=3*n+1
				l.append(n)
		m.append(len(l)+m[n-1]-1)
answer=0
ranswer=0
for x in xrange(0,len(m)):
	if m[x]>answer:
		answer=m[x]
		ranswer=x

print answer
print ranswer