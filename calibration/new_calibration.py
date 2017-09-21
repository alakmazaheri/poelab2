import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import Symbol, nsolve
import sympy

distance = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,	95,	100, 105, 110, 115,	120, 125, 130, 135, 140]
voltages = [501.5, 439.75, 382.25, 343.75, 302.25, 261.75, 236.25, 213.75, 194.25, 180, 167.5, 159, 151, 136, 137, 124.25, 118.5, 110, 106.5, 103.25, 93.25, 90.5, 86, 84.25, 81.25]

new_distances = [24, 37, 43, 53, 61, 71, 83, 97, 108, 121];
new_voltages = [456, 316, 272, 225, 197.5, 169.75, 140, 113, 98, 91];

calibration = []

for x in voltages:
    d = ((-.004216*(x**2))+(-3.837*x) + (1.388e4))/(x+16.53)
    calibration.append(d)

plt.plot(voltages, distance, 'ro', label = 'calibration points')
plt.plot(new_voltages, new_distances, 'b*', label = 'test points')
plt.plot(voltages, calibration, label = 'calibration curve')
plt.legend()
plt.show()
