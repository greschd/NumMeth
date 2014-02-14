#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    14.02.2014 21:12:19 CET
# File:    mutable.py

import sys

def f(x): # Eine Aenderung der gesamten Varible ist nur lokal
    x = 0

def g(x): # Eine Aenderung eines Elements von x veraendert den Wert der Variable global
    x[0] = 0

def example1():
    a = [1, 2, 3]
    
    f(a)
    print('mit f(x): ' + str(a))
    
    g(a)
    print('mit g(x): ' + str(a))
    
def example2():
    b = 2 # g angewendet auf einen immutable Typ ergibt einen Fehler
    g(b)
    print b

