#Modify the program to find and print the sum of all 
#the entries in the list p.

#AI_for_Robotics
#Quiz2
#Mohammadreza Mousaei
#mmousaei@andrew.cmu.edu

p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

mask = [pMiss, pHit, pHit, pMiss, pMiss]

p = [x*y for x,y in zip(mask, p)]


print(sum(p))