import primetest

print primetest.isprime(2)

def quadratic(n, a, b):
	return n**2+a*n+b
count = 0
ans = 0
for a in xrange(-1000,1001):
	for b in xrange(-1000,1001):
		n = 0
		while primetest.isprime(quadratic(n,a,b)):
			n+=1
		if count < n:
			count = n
			ans = a*b
			print {a,b}

print ans