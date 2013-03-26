import math

def gcd(a,b):
	if a>b:
		a,b = b,a
	while a!=b:
		if b<=0 or a<=0:
			return False
			a=b=0
		b=b-a
		if b<a:
			a, b = b, a
	return a


def lcm(a,b):
	return a*b/gcd(a,b)

l=1
for i in range(1,21):
	l=lcm(l,i)


print l

