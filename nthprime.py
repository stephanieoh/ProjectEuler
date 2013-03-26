import math
n=int(raw_input("What is the index of your favorite prime? "))



def isprime(n):
	if n<2:
		return False
	elif n==2:
		return True
	else:
		for x in range(2, int(math.ceil(math.sqrt(n)))+1):
			if n%x==0:
				return False
	return True

def prime(n):
	list=[];
	i=0;
	if n<1:
		print "silly person, I can only find the nth positive prime!"
		return False
	while len(list)<n:
		if isprime(i):
			list.append(i)
		i+=1
	print list[n-1]

prime(n)