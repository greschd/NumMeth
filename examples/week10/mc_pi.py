#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    06.05.2014 20:20:19 CEST
# File:    mc_pi.py

import sys
import random
import numpy as np

def pi(N):
    K = 0

    for i in range(N):
        x = random.random()
        y = random.random()
        if(x**2 + y**2 <= 1):
            K += 1
    
    return 4 * (K / float(N))

def mc_circle(f, N):
    K = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        r = np.sqrt(x**2 + y**2)
        if(r <= 1):
            K += f(r)
    return 4 * (K / float(N))
    
N = [2**i for i in range(5, 20)]
f = lambda r: r**2

#~ for n in N:
    #~ print(pi(n))
#~ 
#~ for n in N:
    #~ print(mc_circle(f, n))
    
functions = [pi, (lambda n: mc_circle(f, n))]

for func in functions:
    print(func(N[-1]))
