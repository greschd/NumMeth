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

filetype = ".pdf" # vereinfacht den Wechsel zwischen Dateitypen (.pdf/.png)

# einfaches Beispiel mit Labels
def example1():
    # Bsp 1: Plot mit Labels
    figure()
    plot(x, f(x), label="$f(x)$")
    grid(True)
    xlabel(r"$x$")
    ylabel(r"$y$")
    legend(loc = "upper left")
    savefig("plot1" + filetype) 
    show()

# figure() - Befehl
def example2():
    # Der Befehl "figure()" erzeugt einen neuen Plot: vergleiche
    # Variante 1:
    figure()
    plot(x,f(x))
    plot(x,f(f(x)))
    savefig("plot2" + filetype)
    show()
    
    # Variante 2:
    figure()
    plot(x,f(x))
    figure()
    plot(x,f(f(x)))
    savefig("plot3" + filetype)
    show()

# Subplots - einfaches Beispiel
def example3():
    figure()
    subplot(2,1,1) # 1. Variable: Anzahl Zeilen, 2.: Anzahl Spalten, 3.: "aktiver" Subplot
    plot(x, f(x))
    subplot(2,1,2)
    plot(x, f(f(x)))
    savefig("plot4" + filetype)
    

#~ example1()
#~ example2()
example3()
