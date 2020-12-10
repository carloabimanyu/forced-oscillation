import numpy as np
import matplotlib.pyplot as plt
h = 0.1

def fu(y, v, t):
    return -alfa * v - np.sin(y) + A * np.sin(w * t)

def gu(y, t):
    return - np.sin(y) + A * np.sin(w * t)
    
# Proses Euler
alfa = 0.2
A = 2
w = 0.1 * np.pi
y0 = 0
v0 = 0
t0 = 1
euler_x=[]
euler_y=[]
for i in range (1000):
    t1 = t0 + h
    y1 = y0 + h*v0
    v1 = v0 + (h)*fu(y0,v0,t0)
    t0 = t1
    y0 = y1
    v0 = v1
    euler_x.append(t0)
    euler_y.append(y0)
    
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(euler_x, euler_y)
plt.title('Euler')
plt.xlabel('Time')
plt.ylabel('y (Displacement)')
plt.legend()
plt.grid(True)
plt.show()
