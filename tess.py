n=[3,9,5,4,2]
m = [[[9,0,3,4,2],2],[[7,0,7,9,4],0],[[3,9,4,5,8],2],[[3,4,1,0,9],1],[[5,1,5,4,5],2],[[1,2,5,3,1],1]]
import random


def reproduction(mom,dad):
	sex = []
	l = len(mom)
	baby = []
	for x in xrange(1, l+1):
		sex.extend([random.randrange(0,2)])
	for x in xrange(0, l):
		if sex[x] == 0:
			baby.extend([mom[x]])
		elif sex[x] == 1:
			baby.extend([dad[x]])
	return baby

print reproduction([9,0,3,4,2],[7,0,7,9,4])