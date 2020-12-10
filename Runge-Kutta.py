import numpy as np
import matplotlib.pyplot as plt
h = 0.1

def fu(y, v, t):
    return -alfa * v - np.sin(y) + A * np.sin(w * t)

def gu(y, t):
    return - np.sin(y) + A * np.sin(w * t)
    
# Proses RK
alfa = 0.2
A = 2
w = 0.1 * np.pi
y0 = 0
v0 = 0
t0 = 1
rk_x=[]
rk_y=[]

for i in range (1000):
    t1 = t0 + h
    k1 = h*fu(y0,v0,t0)
    k2 = h*fu(y0, v0 + k1/2, t0 + h/2)
    k3 = h*fu(y0, v0 + k2/2, t0 + h/2)
    k4 = h*fu(y0, v0 + k3, t0 + h)
    v1 = v0 + (1/6)*(k1 + 2*k2 + 2*k3 +k4)
    y1 = y0 + (h)*v0
    t0 = t1
    y0 = y1
    v0 = v1
    rk_x.append(t0)
    rk_y.append(y0)
    
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(rk_x, rk_y)
plt.title('RK')
plt.xlabel('Time')
plt.ylabel('y (Displacement)')
plt.legend()
plt.grid(True)
plt.show()
