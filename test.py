import math

n=int(raw_input("What number would you like to check primality of? "))

def isprime(n):
	for x in range(2, int(math.ceil(math.sqrt(n)))+1):
		if n%x==0:
			return False
	return True

print isprime(n)