#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@ethz.ch>
# Date:    04.03.2014 00:56:44 CET
# File:    contour.py

import sys
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: x**2 - y**2 + 1
g = lambda x, y: -x + y ** 2 - 1

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z1 = f(X, Y)
Z2 = g(X, Y)

# man kann zwei contour - plots auch uebereinander anzeigen... die etwas schlechtere variant
plt.figure()
CS1 = plt.contour(X, Y, Z1)
plt.clabel(CS1, inline=1, fontsize=10)
CS2 = plt.contour(X, Y, Z2)
plt.clabel(CS2, inline=1, fontsize=10)
plt.show()

# Optionen: N "Levels"
plt.figure()
CS1 = plt.contour(X, Y, Z1, 10)
plt.clabel(CS1, inline=1, fontsize=10)
plt.show()

# Optionen: Levels angeben
plt.figure()
CS1 = plt.contour(X, Y, Z1, [0, 1.115])
plt.clabel(CS1, inline=1, fontsize=10)
plt.show()

# gute Variante fuer die Nulstellensuche
plt.figure()
CS1 = plt.contour(X, Y, Z1, [0])
plt.clabel(CS1, inline=1, fontsize=10)
CS2 = plt.contour(X, Y, Z2, [0])
plt.clabel(CS2, inline=1, fontsize=10)
plt.show()

