import numpy as np
import matplotlib.pyplot as plt
h = 0.1

def fu(y, v, t):
    return -alfa * v - np.sin(y) + A * np.sin(w * t)

def gu(y, t):
    return - np.sin(y) + A * np.sin(w * t)

# Proses ETD
alfa = 0.2
A = 2
w = 0.1 * np.pi
y0 = 0
v0 = 0
t0 = 1
etd_x = []
etd_y = []
for i in range(1000):
    t1 = t0 + h
    v1 = v0 * np.exp(-alfa*h) + gu(y0, t0) * (np.exp(-alfa*h) - 1)/(-alfa)
    y1 = y0 + h * v0
    etd_y.append(y0)
    etd_x.append(t0)
    t0 = t1
    y0 = y1
    v0 = v1
    
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(etd_x, etd_y)
plt.title('ETD')
plt.xlabel('Time')
plt.ylabel('y (Displacement)')
plt.legend()
plt.grid(True)
plt.show()
