# -*- coding: utf-8 -*-
"""
Python program from Don Reble (djr(AT)nk.ca), Jan 05 2007
Corrected Mar 06 2008

I A002072 M4560 N1942
S A002072 1,8,80,4374,9800,123200,336140,11859210,11859210,177182720,1611308699,
T A002072 3463199999,63927525375,421138799639,1109496723125,1453579866024,
U A002072 20628591204480,31887350832896,31887350832896,119089041053696,2286831727304144,2286831727304144,17451620110781856,166055401586083680,166055401586083680
N A002072 a(n) = smallest number m such that for all i>m, either i or i+1 has a prime factor > prime(n).
D A002072 D. H. Lehmer, On a problem of Stormer, Ill. J. Math., 8 (1964), 57-69
o A002072 Python program by Don Reble (djr(AT)nk.ca), Jan 05 2007

 If s and s+1 are both smooth, then so is 2s(s+1). Let f be the
 square-free part of that, so that 2s(s+1) = fy^2. F and y are smooth.
 Now, 2fy^2 + 1 = 4s(s+1)+1 = (2s+1)^2. Let x = 2s+1; we have
 x^2 - 2fy^2 = 1, a Pell equation.

 Therefore one can find all smooth s,s+1 pairs by solving
 x^2 - 2fy^2 = 1 for each smooth square-free f. Further, one can ignore
 f=2, since if x^2-4y^2=x^2-(2y)^2=1, then x=1 and s=0.

 A theorem of Lehmer (see reference) reveals that if Z is the highest
 smooth prime, then only the first M Pell solutions of an equation can
 yield smooth solutions; M=max(3,(Z+1)/2). There is a finite (typically
 small) amount of work for each Pell equation.

 Sometimes one can reduce that work. For such a Pell equation, each
 solution's y is a multiple of the first solution's y. If the first y
 isn't smooth, then none of them are, and the Pell equation yields no
 smooth solutions.

 Alas, if there are n smooth primes, then there are 2^n smooth
 square-free numbers, and 2^n-1 Pell equations. Run-time is exponential
 in n.

 The theory of Pell equations is not explained here, and that part of
 the code may look mystical.

@author: Don Reble
"""
#the first few primes. The program produces one result for each prime.
SmallPrimes = ( 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113 )


# This procedure makes the integer part of the square-root of nn.
def intSqrt(nn):
    twopower = 1
    while (twopower*twopower) <= nn:
        twopower *= 2
    sqrt = 0
    while twopower > 1:
        twopower /= 2
        part = nn / (twopower*twopower)
        sqrt *= 2
        sqrtinc = sqrt + 1
        if (sqrtinc * sqrtinc) <= part:
            sqrt = sqrtinc
    return sqrt


# This procedure says whether nn is maxpr-smooth.
def isSmooth(nn, maxpr):
    for pr in SmallPrimes:
        if nn == 1:
            return True
        if pr > maxpr:
            return False
        while (nn % pr) == 0:
            nn /= pr
    return nn == 1


# This recursive generator yields each square-free maxpr-smooth number.
# Use it thus: squareFrees(maxpr,1,0)
def squareFrees(maxpr, product, pindex):
    pr = SmallPrimes[pindex]
    if pr < maxpr:
        for val in squareFrees(maxpr, product, pindex+1):
            yield val
        for val in squareFrees(maxpr, product*pr, pindex+1):
            yield val
    else:
        yield product
        yield product*maxpr



# This class represents quadratic irrationals of the form
# (uu + sqrt(qq)) / vv.
class QuadNumber:
    def __init__(self, qq, uu=0, vv=1):
        if vv == 0:
            raise "QuadNumber denominator is zero"
        self.__qq = qq
        self.__rt = intSqrt(qq)
        self.__uu = uu
        self.__vv = vv
    def intpart(self):
        return (self.__uu + self.__rt) / self.__vv
    def addin(self, val):
        self.__uu += self.__vv * val
    def reciprocal(self):
        xx = self.__qq - self.__uu * self.__uu
        if (xx % self.__vv) != 0:
            raise "QuadNumber can't take reciprocal"
        self.__uu = -self.__uu
        self.__vv = xx / self.__vv



# This class represents a continued-fraction's convergents.
class ContFrac:
    def __init__(self):
        self.restart()
    def restart(self):
        self.__n1,self.__d1 = 0,1
        self.__n2,self.__d2 = 1,0
    def nextQuotient(self, aa):
        self.__n1,self.__n2 = self.__n2, self.__n1+aa*self.__n2
        self.__d1,self.__d2 = self.__d2, self.__d1+aa*self.__d2
    def numer(self):
        return self.__n2
    def denom(self):
        return self.__d2
    def isPellSolution(self, qq):
        return self.__n2*self.__n2 - qq*self.__d2*self.__d2 == 1



maxsol = 0      # largest smooth solution found so far
                # I needn't reset this each time, since an earlier
                # solution is also a later solution.
pellquan = 3    # the number of Pell solutions to be checked
for maxpr in SmallPrimes:
    if maxpr >= 7:
        pellquan = (maxpr+1)/2
    for sf in squareFrees(maxpr,1,0):
        # For each square-free maxpr-smooth number except 2,
        # solve the corresponding Pell equation.
        if sf == 2: continue
        qq = sf * 2             # Pell equation is x^2-qq*y^2=1.

        # use continued-fraction for sqrt(qq)
        qn = QuadNumber(qq)
        cf = ContFrac()

        # use continued-fraction to find first two Pell solutions
        xfirst,xnext = 0,0
        yfirst,ynext = 0,0
        while xfirst == 0:
            aa = qn.intpart()   # get next quotient
            qn.addin(-aa)       # update QuadNumber
            qn.reciprocal()
            cf.nextQuotient(aa) # update ContFrac
            if cf.isPellSolution(qq):
                xfirst,xnext = xnext,cf.numer()
                yfirst,ynext = ynext,cf.denom()

        # check first y
        if not isSmooth(yfirst,maxpr):
            continue                    # abandon this Pell equation

        # check Pell solutions
        sol = (xfirst - 1) / 2
        if (sol > maxsol) and isSmooth(sol,maxpr) and isSmooth(sol+1,maxpr):
            maxsol = sol
        sol = (xnext - 1) / 2
        if (sol > maxsol) and isSmooth(sol,maxpr) and isSmooth(sol+1,maxpr):
            maxsol = sol

        # use recurrence relation to make pellquan-2 more Pell solutions
        more = pellquan - 2
        xprev = xfirst
        while more > 0:
            xprev,xnext = xnext, xnext*xfirst*2 - xprev
            more -= 1
            # check Pell solution
            sol = (xnext - 1) / 2
            if (sol > maxsol) and isSmooth(sol,maxpr) and isSmooth(sol+1,maxpr):
                maxsol = sol

    print (maxsol)