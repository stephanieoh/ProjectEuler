import random
import math

def generatelots(n):
	l = []
	for x in xrange(1,n+1):
		k = []
		for y in xrange(0,16):
			k.extend([random.randrange(0,10)])
		l.append(k)
	return l


def strangedistance(n,m):
	count = 0
	for i in xrange(0,len(m[0])):
 		if n[i] == m[0][i]:
 			count += 1
 	return (count-m[1])**2


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


def findBest(n, l):
	elite = []
	for x in xrange(0,n):
		elite.extend([l[x]])
	elite.sort()
	for x in xrange(n,len(l)):
		if l[x][0] < elite[n-1][0]:
			for y in xrange(0,n):
				if l[x][0] < elite[y][0]:
					elite.insert(y, l[x])
					elite = elite[:n]
					break
	return elite


m = [[[5,6,1,6,1,8,5,6,5,0,5,1,8,2,9,3],2], [[3,8,4,7,4,3,9,6,4,7,2,9,3,0,4,7],1],[[5,8,5,5,4,6,2,9,4,0,8,1,0,5,8,7],3],[[9,7,4,2,8,5,5,5,0,7,0,6,8,3,5,3],3],[[4,2,9,6,8,4,9,6,4,3,6,0,7,5,4,3], 3],[[3,1,7,4,2,4,8,4,3,9,4,6,5,8,5,8],1],[[4,5,1,3,5,5,9,0,9,4,1,4,6,1,1,7],2],[[7,8,9,0,9,7,1,5,4,8,9,0,8,0,6,7] ,3],[[8,1,5,7,3,5,6,3,4,4,1,1,8,4,8,3],1],[[2,6,1,5,2,5,0,7,4,4,3,8,6,8,9,9] ,2],[[8,6,9,0,0,9,5,8,5,1,5,2,6,2,5,4],3],[[6,3,7,5,7,1,1,9,1,5,0,7,7,0,5,0],1],[[6,9,1,3,8,5,9,1,7,3,1,2,1,3,6,0],1],[[6,4,4,2,8,8,9,0,5,5,0,4,2,7,6,8],2],[[2,3,2,1,3,8,6,1,0,4,3,0,3,8,4,5] ,0],[[2,3,2,6,5,0,9,4,7,1,2,7,1,4,4,8] ,2],[[5,2,5,1,5,8,3,3,7,9,6,4,4,3,2,2] ,2],[[1,7,4,8,2,7,0,4,7,6,7,5,8,2,7,6] ,3],[[4,8,9,5,7,2,2,6,5,2,1,9,0,3,0,6] ,1],[[3,0,4,1,6,3,1,1,1,7,2,2,4,6,3,5] ,3],[[1,8,4,1,2,3,6,4,5,4,3,2,4,5,8,9] ,3],[[2,6,5,9,8,6,2,6,3,7,3,1,6,8,6,7] ,2]]


def guess(n):
	l = generatelots(n)
	score = []
	elite = []
	for i in xrange(0,n):
		score.extend([sum(strangedistance(l[i],m[j]) for j in xrange (0, 22)) ** (0.5), l])
	elite = findBest(int(math.floor(n**(0.5))), score)
	for i in xrange(0,int(math.floor(n**(0.5)))):
		for j in xrange(0,int(math.floor(n**(0.5)))):
			l = reproduction(score[i][1], score[j][1])
	return l

print guess(4)
