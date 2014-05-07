#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    06.05.2014 20:20:19 CEST
# File:    mc_pi.py

import sys
import random
import numpy as np

#--------------------Berechnung von Pi mit MC---------------------------#

def pi(N):
    K = 0

    for i in range(N):
        x = random.random()
        y = random.random()
        if(x**2 + y**2 <= 1):
            K += 1
    
    return 4 * (K / float(N))

#----------------Integration auf dem Kreis (Ortskoordinaten)------------#

def mc_circle(f, N):
    K = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        r = np.sqrt(x**2 + y**2)
        if(r <= 1):
            K += f(x , y)
    return 4 * (K / float(N))

#----------------Integration auf dem Kreis (Polarkoordinaten)-----------#

def mc_circle_2(g, N):
    K = 0
    for i in range(N):
        r = random.random()
        theta = random.random() * 2. * np.pi
        K += g(r, theta) * r
    return K / float(N) * 2.* np.pi # hier muss man mit der Fläche des Kreises skalieren
    
#--Integration auf dem Kreis (Polarkoordinaten, mit Fehlerbetrachtung)--#

def mc_with_error(g, N):
    res = 0
    sqr = 0
    for i in range(N):
        r = random.random()
        theta = random.random() * 2. * np.pi
        res += g(r, theta) * r
        sqr += (g(r, theta) * r)**2
    vol = 2 * np.pi
    n = float(N)
    return [vol * res / n, np.sqrt(vol**2 * (sqr / n - (res / n)**2)) / (n - 1)]
    
N = [2**i for i in range(5, 20)]
f = lambda x, y: x**2 + y**2
g = lambda r, theta: r**2

#~ for n in N:
    #~ print(pi(n))
#~ 
#~ for n in N:
    #~ print(mc_circle(f, n))
    
functions = [pi, lambda n: mc_circle(f, n), lambda n: mc_circle_2(g, n), lambda n: mc_with_error(g, n)]

for func in functions:
    print(func(N[-1]))
    print("")
