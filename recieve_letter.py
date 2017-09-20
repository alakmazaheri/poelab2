import matplotlib.pyplot as plt
from sympy import Symbol, nsolve
import sympy
from serial import Serial, SerialException

cxn = Serial('COM4', 9600)

positions = []
sensor_values = []

i = 0

while i < 420:
    servoPos = float(cxn.readline().strip())
    sensorVal = float(cxn.readline().strip())

    positions.append(servoPos)
    sensor_values.append(sensorVal)

    i += 1

distances = []

for value in sensor_values:
    #eqa = Eq(744.4.*exp(-.04263*a) + 216.*exp(-.0071584*a), value)
    a = Symbol('a')
    d = nsolve(744.4*sympy.exp(-.04263*a) + 216*sympy.exp(-.0071584*a) == value, a)
    distances.append(d)

print(distances)
plt.plot(positions,distances, label = 'letter')
plt.legend()
plt.show()
