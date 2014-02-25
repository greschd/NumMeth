#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    14.02.2014 21:55:16 CET
# File:    arrayindex.py

import sys
import numpy as np

if __name__ == "__main__":
    
    A = np.array([1, 2, 3, 4])
    
    
    print("Bsp 1")
    print(A[0]) # Indizierung beginnt bei 0
    print(A[1])
    print(A[-1]) # Minus - erstes Element == letztes Element
    print(A[-2])
    
    print('\n')
    
    print("Bsp 2")
    size = 4;
    line = lambda n, m: [x for x in range((n * m),((n + 1) * m))]
    B = np.array([line(n, size) for n in range(0, size)])
    print B
    
    print('\n')
    
    print("Bsp 3")
    # Variante 1: einzelne Elemente
    print("Variante 1")
    print B[(0,1),(1,2)]
    
    print('\n')
    
    # Variante 2: alle Kombinationen der Zeilen - und Spaltenindizes
    print("Variante 2")
    i = np.array([[0],[1]])
    j = np.array([[1,2]])
    print B[i,j]
    
    print('\n')
    
    # Achte auf die doppelte Klammerung (die doppelte Klammer wird zur Zeile, die einfache zur Spalte)
    i = np.array([[0,1]])
    j = np.array([[1],[2]])
    print B[i,j]
