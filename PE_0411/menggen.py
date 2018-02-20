#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:29:08 2018

@author: mbh
"""

import bisect
import sys
import time

class Problem():
    def solve(self):
        #self.benchmark()
        print(self.get())

    def benchmark(self):
        for n in [22]:#[22, 123, 10000]:
            print(n, "=>", self.S(n))

    def get(self):
        result = 0
        for k in range(1, 30 + 1):
            maximum_number = self.S(k**5)
            result += maximum_number
            print(k, "=>", maximum_number)
        return result

    def S(self, n):
        station_set = set()

        for i in range(2 * n + 1):
            station = (pow(2, i, n), pow(3, i, n))
            if station in station_set:
#                print(2*n+1,'i=',i)
                break
            else:
                station_set.add(station)
        sorted_station_array = sorted(list(station_set))
#        print(sorted_station_array)
        y_array = [y for x, y in sorted_station_array]
#        print(y_array)
        return self.get_longest_increasing_subsequence_length(y_array)

    def get_longest_increasing_subsequence_length(self, sequence):
        length = len(sequence)
        if length == 0:
            return 0
        subsequence = [sequence[0]]
        for i in range(1, length):
            n = sequence[i]
            if n >= subsequence[-1]:
                subsequence.append(n)
            else:
                subsequence[bisect.bisect_right(subsequence, n)] = n
#        print(subsequence)
        return len(subsequence)

def menggen():
    t=time.clock()
    problem = Problem()
#    problem.benchmark()
    problem.solve()
    print(time.clock()-t)

#if __name__ == '__main__':
#    sys.exit(main())