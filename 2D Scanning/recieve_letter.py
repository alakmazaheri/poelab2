import matplotlib.pyplot as plt
from sympy import Symbol, nsolve
import sympy
from serial import Serial, SerialException

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

plt.plot(positions,distances, label = 'letter')
plt.legend()
plt.show()
