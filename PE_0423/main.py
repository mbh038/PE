# driver for p423

limit=50
mv=10**9+7

import time
import numpy as np
import numba as nb

import PE_0423


t0=time.perf_counter()
pps=PE_0423.myprimepi(limit+1)
total=PE_0423.p423_sub(limit,pps,mv)
print(total)
print(time.perf_counter()-t0)
