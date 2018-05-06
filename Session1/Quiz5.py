#The code so that it updates the probability twice
#and gives the posterior distribution after both
#measurements are incorporated. Make sure that your code
#allows for any sequence of measurement of any length.

#AI_for_Robotics
#Quiz5
#Mohammadreza Mousaei
#mmousaei@andrew.cmu.edu

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
	q = []
	for i in range(len(p)):
		hit = (Z == world[i])
		q.append(p[i]*(hit*pHit + (1-hit)*pMiss))

	q = [x/sum(q) for x in (q)]
	return q



for i in range(len(measurements)):
	p = sense(p, measurements[i])



print(p)
