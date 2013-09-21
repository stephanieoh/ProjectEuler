def digitsum(n):
	x = str(n)
	c = 0
	for digit in x:
		c = c + int(digit)**5
	return c

def main():
	total = 0
	for x in xrange(2,999999):
		if digitsum(x) == x:
			print x
			total += x
	print total

main()