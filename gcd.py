n = raw_input("Enter two numbers, separated by a comma, whose gcd you would like to find: ")

if int(n.split(',')[0])> int(n.split(',')[1]):
	b = int(n.split(',')[0]);
	a = int(n.split(',')[1]);
elif int(n.split(',')[0])<=int(n.split(',')[1]):
	b = int(n.split(',')[1]);
	a = int(n.split(',')[0]);


while a!=b:
	if b<=0 or a<=0:
		print None
		a=b=0
	b=b-a
	if b<a:
		a, b = b, a
print a
