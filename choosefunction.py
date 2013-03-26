from fractions import Fraction
def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def choose(n,r):
	return Fraction(factorial(n),factorial(r)*factorial(n-r))
	