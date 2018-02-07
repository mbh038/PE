#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 11 2017
@author: Phil Lucido

#! python3


A generalized Pell equation solver.  Finds nonnegative, non-trivial solutions
to the equation x^2 - D*y^2 = N for x, y integers.

This implements the PQa and LMM algorithms, plus the simpler cases for abs(N)
equal to 1 or 4, as described in John Robertson's 2004 paper "Solving the
generalized Pell equation" at http://www.jpr2718.org/pell.pdf.

There are two main entrypoints, both of which are generators that will return
successive (x, y) solution pairs in increasing order by x:

    Pell_solver(D, N):
        Return solutions to x^2 - Dy^2 = N
    Pell_plusminus_solver(D, N):
        Return solutions to both x^2 - Dy^2 = N and x^2 - Dy^2 = -N

Care is taken to handle all special cases: N = 0, D <= 0, or D is a perfect
square.

Phil Lucido, May 11 2017

"""

import sys, itertools, heapq

def is_perfect_square(n):
    """ Simple perfect square tester.  Good for at least 15 digits """
    if n < 0:
        return False
    return int(n ** 0.5) ** 2 == n

def PQa(P, Q, D):
    """
    Compute the simple continued fraction expansion of the quadratic irrational
    (P + sqrt(D))/Q, plus auxiliary variables which can be used to determine
    when, e.g., a solution to a related Pell's equation has been found.
    This is a generator which will yield the next convergents on each call.
    """
    assert (P*P - D) % Q == 0
    Ap, A = 0, 1
    Bp, B = 1, 0
    Gp, G = -P, Q
    D_sqrt = D**0.5
    i = 0
    while True:
        a = int((P + D_sqrt)//Q)
        Ap, A = A, a*A + Ap
        Bp, B = B, a*B + Bp
        Gp, G = G, a*G + Gp
        yield i, P, Q, a, A, B, G
        i += 1
        P = a*Q - P
        Q = (D - P*P)//Q

def Pell_generator(D, t, u, d, x, y):
    """
    Produce successive solutions, given the initial solution (x,y) and the
    recurrence multiplier (t + u*sqrt(D)).
    """
    while True:
        yield x, y
        x, y = (t*x + D*u*y)//d, (u*x + t*y)//d

def Pell_fundamental_1(D):
    """
    Find the fundamental solution to x^2 - Dy^2 = plus or minus 1.  Returns
    the number of iterations the PQa algorithm took to find the fundamental,
    plus the resulting x and y.
    """
    gen = PQa(0, 1, D)
    tprev = next(gen)
    for t in gen:
        if t[2] == 1:
            break
        tprev = t
    return t[0], tprev[6], tprev[5]

def Pell_plus_1(D):
    """ Generate the solutions to x^2 - Dy^2 = 1 """
    l, x, y = Pell_fundamental_1(D)
    if l % 2 == 1:
        # There are alternating -1, +1 solutions, so skip
        # to just the +1 ones.
        x, y = x*x + D*y*y, 2*x*y
    yield from Pell_generator(D, x, y, 1, x, y)

def Pell_minus_1(D):
    """ Generate the solutions to x^2 - Dy^2 = -1, if any exist """
    l, x, y = Pell_fundamental_1(D)
    if l % 2 == 0:
        # There are no solutions
        return
    t, u = x*x + D*y*y, 2*x*y
    yield from Pell_generator(D, t, u, 1, x, y)

def Pell_plusminus_1(D):
    """ Generate the solutions to x^2 - Dy^2 = plus or minus 1 """
    _, x, y = Pell_fundamental_1(D)
    yield from Pell_generator(D, x, y, 1, x, y)

def Pell_fundamental_4(D):
    """
    Find the fundamental solution to x^2 - Dy^2 = plus or minus 4.  Returns
    the number of iterations the PQa algorithm took to find the fundamental,
    plus the resulting x and y.
    """
    kind = D % 4
    if kind == 0:
        gen = PQa(0, 1, D//4)
        xmult, ymult, stop = 2, 1, 1
    elif kind == 1:
        gen = PQa(1, 2, D)
        xmult, ymult, stop = 1, 1, 2
    else:
        gen = PQa(0, 1, D)
        xmult, ymult, stop = 2, 2, 1
    tprev = next(gen)
    for t in gen:
        if t[2] == stop:
            break
        tprev = t
    return t[0], xmult * tprev[6], ymult * tprev[5]

def Pell_plus_4(D):
    """ Generate the solutions to x^2 - Dy^2 = 4 """
    l, x, y = Pell_fundamental_4(D)
    if l % 2 == 1:
        # There are alternating -4, +4 solutions, so skip
        # to just the +4 ones.
        x, y = (x*x + D*y*y)//2, x*y
    yield from Pell_generator(D, x, y, 2, x, y)

def Pell_minus_4(D):
    """ Generate the solutions to x^2 - Dy^2 = -4, if any exist """
    l, x, y = Pell_fundamental_4(D)
    if l % 2 == 0:
        # There are no solutions
        return
    t, u = x*x + D*y*y, 2*x*y
    yield from Pell_generator(D, t, u, 4, x, y)

def Pell_plusminus_4(D):
    """ Generate the solutions to x^2 - Dy^2 = plus or minus 4 """
    _, x, y = Pell_fundamental_4(D)
    yield from Pell_generator(D, x, y, 2, x, y)

def Pell_fundamental_general(P, Q, D):
    """
    Use algorithm PQa to find a fundamental solution to the general Pell's
    equation, given the arguments P, Q, D.  Returns either the x, y pair
    of the fundamental, or None if the continued fraction form of the
    quadratic surd (P + sqrt(D))/Q completes a full cycle without finding
    a row with Q(i) = 1 or -1.
    """
    Dsqrt = D ** 0.5
    Preduced, Qreduced = None, None
    gen = PQa(P, Q, D)
    tprev = next(gen)
    for t in gen:
        if abs(t[2]) == 1:
            return tprev[6], tprev[5]
        if t[1] == Preduced and t[2] == Qreduced:
            return
        surd = (t[1] + Dsqrt)/t[2]
        conj = (t[1] - Dsqrt)/t[2]
        if surd > 1 and -1 < conj < 0:
            Preduced, Qreduced = t[1], t[2]
        tprev = t

def Pell_general_solver(D, N):
    """
    Implement algorithm LMM to solve the generalized Pell's equation.
    """
    # First solve x^2 - Dy^2 = +/-1.  These are needed for generating new
    # solutions via the recurrence relationships.
    t, u = next(Pell_plusminus_1(D))
    if t*t - D*u*u == -1:
        tneg, uneg = t, u
        t, u = t*t + D*u*u, 2*t*u
    else:
        tneg, uneg = None, None
    # Find all the fundamental solutions
    fundamentals = set()
    for f in range(1, int(abs(N)**0.5)+1):
        f_sq = f*f
        if N % f_sq:
            continue
        m = N // f_sq
        abs_m = abs(m)
        for z in range(1, abs_m//2 + 1):
            if (z*z - D) % abs_m:
                continue
            for sign in (1, -1):
                result = Pell_fundamental_general(z*sign, abs_m, D)
                if not result:
                    continue
                r, s = result
                if r*r - D*s*s == m:
                    fundamentals.add((f*r, f*s))
                elif tneg:
                    fundamentals.add((f*(r*tneg + D*s*uneg), f*(r*uneg + s*tneg)))
    if not fundamentals:    # No solutions found
        return
    # Generate the minimum non-negative solutions
    queue = []
    for x, y in fundamentals:
        if x < 0: x, y = -x, -y
        if y < 0: x, y = x*t + D*y*u, x*u + y*t
        if x < 0: x, y = -x, -y
        heapq.heappush(queue, (x, y))
    # Produce all solutions in sorted order, using a priority queue
    while True:
        x, y = heapq.heappop(queue)
        yield x, y
        heapq.heappush(queue, (x*t + D*y*u, x*u + y*t))

def Pell_special_cases(D, N):
    """ Handle all the special cases for which the normal algorithms fail. """
    if N == 0:
        if D == 0:  # x^2 = 0
            for i in itertools.count():
                yield 0, i
        elif D < 0: # x^2 + |D|y^2 = 0, trivial solution
            yield 0, 0
        else:
            Dsqrt = int(D ** 0.5)
            if D != Dsqrt * Dsqrt:  # x^2 = Dy^2, D not a square - no solutions
                return
            for i in itertools.count():
                yield Dsqrt * i, i
        return
    if D == 0:
        Nsqrt = int(abs(N) ** 0.5)
        if N != Nsqrt * Nsqrt:      # x^2 = N, N not a square - no solutions
            return
        for i in itertools.count():
            yield Nsqrt, i
    elif D < 0:
        if N < 0:                   # x^2 + |D|y^2 = -|N|, no solutions
            return
        # x^2 + |D|y^2 = |N| - search for finite number of solutions
        for y in range(int((N//(-D)) ** 0.5), -1, -1):
            diff = N + D*y*y
            x = int(diff ** 0.5)
            if diff == x * x:
                yield x, y
    else:
        assert is_perfect_square(D)
        # For D a square, solve (x + y*sqrt(D))(x - y*sqrt(D)) = N.
        # Find the factor pairs (f1, f2), then solve the linear equations
        # x - y*sqrt(D) = f1, x + y*sqrt(D) = f2
        TwiceDsqrt = 2 * int(D ** 0.5)
        for f1 in range(int(abs(N)**0.5), 0, -1):
            if N % f1 == 0:
                f2 = N // f1
                if (f2 - f1) % TwiceDsqrt == 0:
                    x, y = (f1 + f2)//2, (f2 - f1)//TwiceDsqrt
                    yield x, y

def Pell_solver(D, N):
    """
    Primary entrypoint.  Produce solutions to x^2 - Dy^2 = N.
    """
    if N == 0 or D <= 0 or is_perfect_square(D):
        yield from Pell_special_cases(D, N)
    elif N == 1:
        yield from Pell_plus_1(D)
    elif N == -1:
        yield from Pell_minus_1(D)
    elif N == 4:
        yield from Pell_plus_4(D)
    elif N == -4:
        yield from Pell_minus_4(D)
    else:
        yield from Pell_general_solver(D, N)

def Pell_plusminus_solver(D, N):
    """
    Alternate entrypoint.  Produce solutions which satisfy either
    x^2 - Dy^2 = N or x^2 - Dy^2 = -N.
    """
    if N == 0:
        yield from Pell_special_cases(D, N)
    elif D <= 0 or is_perfect_square(D):
        yield from heapq.merge(Pell_special_cases(D, N),
                               Pell_special_cases(D, -N))
    elif abs(N) == 1:
        yield from Pell_plusminus_1(D)
    elif abs(N) == 4:
        yield from Pell_plusminus_4(D)
    else:
        yield from heapq.merge(Pell_general_solver(D, N),
                               Pell_general_solver(D, -N))

def test_solve(D = 5, N = 1, max_sols = 10):
    i = 0
    for i, solution in enumerate(Pell_plusminus_solver(D, N), 1):
        x, y = solution
        print(i, x, y, x*x - D*y*y)
        if i >= max_sols:
            break
    if i == 0:
        print("No solutions found")

if __name__ == "__main__":
    test_solve(*(int(arg) for arg in sys.argv[1:]))
