import math

def setFalse(list, n):
	count = n  
	while n - 1 < len(list) - count:
		list[count + n - 1] = False
		n += count
	return list

#print setFalse([True for x in range(10)], 3)

#find first True in the list after the jth element
def findFirstTrue(list, j):
	while not list[j]:
		j += 1
	return j

#print findFirstTrue([False, False,False,False,False,False, True, True, True])

def findFirstTrueThenSetAppropFalse(list, j):
	return setFalse(list, 	findFirstTrue(list, j)+1)

#print findFirstTrueThenSetAppropFalse([False, False, True, True, True, True])

def primecache(n):
	list = [True for x in range(n)]
	list[0] = False
	i = 1

	while i < int(math.ceil(math.sqrt(n))):
		#list = setFalse(list, findFirstTrue(list, i+1)+1)
		j = i + 1
		# while not list[j]:
		# 	j += 1
		# j += 1
		
		count = j 
		while j - 1 < len(list) - count:
			list[count + j - 1] = False
			j += count
		i += 1
		while not list[i]:
			i += 1
	#print list


	primes = []
	for j in xrange(0, n):
		if list[j]:
			primes.append(j+1)
	return primes

print len(primecache(2000000))

