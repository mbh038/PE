# -*- coding: utf-8 -*-
"""

PE_0607

Marsh Crossing

Created on Sun Jul  2 14:12:27 2017
@author: mbh
"""

def trdirect():    
    t=(25*6**0.5)/10+(25*(2-2**0.5)/10)+10*(1/9+1/8+1/7+1/6+1/5)    
    return t

#13.473802361543436
def tew():    
    t=50*(2-2**0.5)/10+10*2**0.5*(1/9+1/8+1/7+1/6+1/5)    
    return t

#14.824477997388708
def tmid():    
    t=(50*(5-2*2**0.5)**0.5)/10+10*(1/9+1/8+1/7+1/6+1/5)    
    return t

import math
import time

#Coordinate system is (x,y)=(perpendicular to marsh, parallel to marsh)
#So we have rotated the world 45 degrees from given diagram
#Idea is to find initial angle of departure that will lead to light ray
#striking target at B. All other angles determined by this angle, given
#refraction and known velocities in all regions.
def lightRay(delta=1e-11):
    t=time.clock()
    yreq=(100/(2**0.5)) #y displacement required
    ds=[25*(2**0.5-1),10,10,10,10,10,25*(2**0.5-1)]
    vs=[10,9,8,7,6,5,10] 
    thetaHigh=math.radians(60)
    thetaLow=math.radians(30)
    ysum=0
    while abs(yreq-ysum)>delta:
        thetaTry=thetaLow+(thetaHigh-thetaLow)/2
        tsum=ds[0]/(vs[0]*math.cos(thetaTry))
        ysum=ds[0]*math.tan(thetaTry)
        theta=thetaTry
        for i in range(1,len(vs)):
            theta=math.asin(math.sin(theta)*vs[i]/vs[i-1])
            tsum+=ds[i]/(vs[i]*math.cos(theta))
            ysum+=ds[i]*math.tan(theta)
        if ysum>yreq:
            thetaHigh=thetaTry
        else:
            thetaLow=thetaTry
    print(round(tsum,10),time.clock()-t)

#optimization using scipy - 60 times slower than my method!
#from user blind Anagram 
t=time.clock()       
from math import pi, cos, tan
from scipy.optimize import minimize

s1 = 50 * 2 ** 0.5
# the shortest distance to the marsh
s2 = s1 / 2 - 25

# the function to minimise - the time to travel from A to B
# <th> is a list of angles from the south east direction to
# move on firm land and in each of the five sections in the
# marsh
def time1(th):
  # t - cumulative time to cross the sections
  # x - cumulative distance moved in the north-east direction
  # s - each section length measured in the south east direction
  t, x, s = 0, 0, s2
  for i, a in enumerate(th):
    # add the time to traverse this section
    t += s / cos(pi * a / 180) / (10 - i)
    # add the distance traversed in the north east direction 
    x += s * tan(pi * a / 180)
    s = 10
  # add the time for the final step
  return t + (s2 ** 2 + (s1 - x) ** 2) ** 0.5 / 10

# start from the straight line path
a = [45, 45, 45, 45, 45, 45]
# and minimise the time
res = minimize(time1, a, method='nelder-mead', options={'xtol': 1e-12})
print(time.clock()-t,round(time1(res.x), 10))
    
       