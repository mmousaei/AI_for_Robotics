#Move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.

#AI_for_Robotics
#Quiz6
#Mohammadreza Mousaei
#mmousaei@andrew.cmu.edu

import numpy as np

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    exact = np.roll(p, U)
    overshoot = np.roll(p, U+1)
    undershoot = np.roll(p, U-1)

    q = list(pExact*exact + pOvershoot*overshoot + pUndershoot*undershoot)
    return q


print move(p, 1)
