#code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.

#AI_for_Robotics
#Quiz1
#Mohammadreza Mousaei
#mmousaei@andrew.cmu.edu
p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

mask = [pMiss, pHit, pHit, pMiss, pMiss]

p = [x*y for x,y in zip(mask, p)]

print(p)