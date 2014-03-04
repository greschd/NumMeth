#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    04.03.2014 02:33:37 CET
# File:    exception.py

import sys
from scipy.optimize import *

f1 = lambda x: 3 * x

try:
    bisect(f1, 1, 2)
except:
    print("dumm gelaufen")
    
# man kann das auch benutzen!
def try_bisect(f, x, y):
    try:
        return bisect(f, x, y)
    except:
        return "error"
        
a = try_bisect(f1, 1, 2)
if(a == "error"):
    print("aha!")
    print(try_bisect(f1, -1, 2))
