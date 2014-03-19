#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    19.03.2014 02:00:51 CET
# File:    lstsq.py

import sys
import scipy.linalg as la

# ein simples Ausgleichsproblem
A = [[1, 0.2],[1, 0.8],[1, 1.2]]
b = [1, 0.3, 0]

x, res, rang, s = la.lstsq(A,b)

print("Loesung des Ausgleichsproblems: ")
print(x)
print("\nResiduum: ")
print(res)
print("\nRang der Matrix A:")
print(rang)
print("\nSingulaerwerte von A:")
print(s)

