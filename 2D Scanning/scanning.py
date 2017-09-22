import matplotlib.pyplot as plt
from sympy import Symbol, nsolve
import sympy
from serial import Serial, SerialException
import math
import numpy as np

def recieve_letter():
    cxn = Serial('COM4', 9600)

    positions = []
    sensor_values = []

    i = 0
    check = 0

    while check != 42.0:
        servoPos = float(cxn.readline().strip())
        check = servoPos
        if check == 42.0:
            break
        sensorVal = float(cxn.readline().strip())

        positions.append(servoPos)
        sensor_values.append(sensorVal)

    #averaging function here

    distances = []

    for x in sensor_values:
        d = ((-.004216*(x**2))+(-3.837*x) + (1.388e4))/(x+16.53)
        distances.append(d)

    return distances, positions

def visualize(distances, positions):
    #array = np.zeros(1, max(positions) - min(positions)), dtype= np.uint8)
    #distances

    for dist in distances:
        if dist > 150:
            dist = 149

    print(distances)
    r = np.array(distances)
    r2 = np.vstack((r, r));
    plt.imshow(r2, interpolation = 'nearest', cmap = 'gray_r')
    plt.show()

    plt.plot(positions,distances, label = 'letter')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    distances, positions = recieve_letter()
    visualize(distances, positions)
