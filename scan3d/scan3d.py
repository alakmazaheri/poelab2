import matplotlib.pyplot as plt
from sympy import Symbol, nsolve
import sympy
from serial import Serial, SerialException
import math
import numpy as np

def recieve_letter():
    cxn = Serial('COM4', 9600)

    angles = []
    sensor_values = []

    i = 0
    check = 0
    up_check = 0

    while check != 9999.0:
        pans = []
        temp_values = []

        while check != 9999.0:
            tilt = float(cxn.readline().strip())
            check = tilt
            up_check = tilt

            if check == 9999.0:
                return sensor_values, angles
            if up_check == 667.0:
                break

            pan = float(cxn.readline().strip())
            sensorVal = float(cxn.readline().strip())

            pans.append(pan)
            temp_values.append(sensorVal)

        if check == 9999.0:
            break

        for p in pans:
            angles.append([tilt, p])

        sensor_values.append(temp_values)
        temp_values = []
        
    return sensor_values, angles

def get_distance(sensor_values, angles):
    distances = []
    dist = []

    for a in sensor_values:
        for x in a:
            d = ((-.004216*(x**2))+(-3.837*x) + (1.388e4))/(x+16.53)
            dist.append(d)
        distances.append(dist)

    return distances

def visualize(distances, angles):
    #array = np.zeros(1, max(positions) - min(positions)), dtype= np.uint8)
    #distances

    #for x in distances:
    #    for dist in x:
    #        if dist > 150:
    #            dist = 149


    #for row in distances:
    #    r = np.array(row)
    #    r2 = np.vstack((r2,r))

    #r2 = np.vstack((r, r));
    #plt.imshow(r2, interpolation = 'nearest', cmap = 'gray_r')

    dist = np.array(distances)

    print(len(distances))
    print(len(distances[0]))
    plt.imshow(dist, interpolation = 'nearest', cmap = 'gray_r')
    plt.show()

    #plt.plot(angles,distances, label = 'letter')
    #plt.legend()
    #plt.show()

if __name__ == "__main__":
    sensor_vals, angles = recieve_letter()
    distances = get_distance(sensor_vals, angles)
    visualize(distances, angles)
