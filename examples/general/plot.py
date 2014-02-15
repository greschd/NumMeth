#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    14.02.2014 22:35:24 CET
# File:    plot.py

import sys

from numpy import *
from matplotlib.pyplot import *



x = linspace(0,1,100)

f = lambda x: x**2
    
def example1():
    # Bsp 1: Plot mit Labels
    figure()
    plot(x, f(x), label="$f(x)$")
    grid(True)
    xlabel(r"$x$")
    ylabel(r"$y$")
    legend(loc = "upper left")
    #~ savefig("plot.pdf")
    #~ savefig("plot.png")
    show()

def example2():
    # Der Befehl "figure()" erzeugt einen neuen Plot: vergleiche
    # Variante 1:
    figure()
    plot(x,f(x))
    plot(x,f(f(x)))
    show()
    
    # Variante 2:
    figure()
    plot(x,f(x))
    figure()
    plot(x,f(f(x)))
    show()

example1()
example2()
