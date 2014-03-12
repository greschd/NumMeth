#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    12.03.2014 13:02:02 CET
# File:    gram_schmidt.py

import sys
import numpy as np
import numpy.linalg as la

def GR(A):
    m, n = A.shape
    R = np.zeros((n, n))
    Q = np.zeros((m, n))
    for j in xrange(n):
        vj = A[:, j]
        for i in xrange(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            vj = vj - R[i, j]*Q[:, i]
        R[j, j] = la.norm(vj)
        Q[:, j] = vj / R[j, j]
    return [Q, R]

# test
A = np.array([[1, 2],[0.2, 3]])
[Q, R] = GR(A)
print(Q)
print(R)
print(np.dot(Q, R))
print(np.dot(Q, np.transpose(Q)))
