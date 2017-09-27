# -*- coding: utf-8 -*-
"""

PE_0071

Ordered fractions

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.

Created on Wed Jul 20 11:53:23 2016
@author: mbh
"""

import fractions as fr
import time

t=time.clock()
a=max([fr.Fraction(int((3000000-i)/7),1000000)for i in range(1,100)])
print (max([fr.Fraction(x,y) for x in range(a.numerator-3,a.numerator+3) for y in range (a.denominator-3,a.denominator+1) if float(x)/y<float(3)/7]))
print(time.clock()-t)
    