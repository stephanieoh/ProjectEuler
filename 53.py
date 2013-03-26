from fractions import Fraction
def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def choose(n,r):
	return Fraction(factorial(n),factorial(r)*factorial(n-r))
	
k=0;
for n in xrange(0,1001):
	for r in xrange(0,n):
		if choose(n,r)>1000000:
			k+=1
print(k)