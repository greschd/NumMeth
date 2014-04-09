#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    09.04.2014 02:00:11 CEST
# File:    random.py

import sys
import numpy as np
import numpy.random as rn

N = 10

print(rn.rand(N))    # 10 zufallszahlen zwischen 0 und 1
print(2 * rn.rand(N) - 1)    # 10 zufallszahlen zwischen -1 und 1
