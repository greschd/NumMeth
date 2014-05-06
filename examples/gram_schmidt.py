#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    12.03.2014 00:28:22 CET
# File:    gram_schmidt.py

import sys
import numpy as np
import scipy.linalg as la

def GR(A):
    m, n = A.shape
    
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:,i], A[:, j])
            v -= R[i, j]*Q[:, i]
        R[j, j] = la.norm(v)
        Q[:, j] = v / R[j, j]
    return [Q, R]
    
A = np.array([[1, 2],[0.2, 3]])
[Q, R] = GR(A)
print(np.dot(Q, R))
print(np.dot(Q, np.transpose(Q)))
    
