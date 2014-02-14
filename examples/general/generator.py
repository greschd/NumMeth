#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    14.02.2014 21:29:47 CET
# File:    generator.py

import sys

def generator():
    i = 2
    while True:
        yield i
        i = i * 2

if __name__ == "__main__":
    G = generator()
    for i in xrange(1,10):
        print G.next()  
    
