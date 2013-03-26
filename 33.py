from fractions import Fraction
l=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0];t=1;b=1
for c in l:
	for d in l:
		for a in l:
			if (c*10.0+a)/(a*10.0+d)==(c/d):
				if a!=c:
					t=t*int(c)
					b=b*int(d)
					print[c*10+a,a*10+d,c,d]
					print[Fraction(t,b)]
