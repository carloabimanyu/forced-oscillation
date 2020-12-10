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

# Visualisasi
# Uncomment to plot

# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)
# ax1.plot(euler_x, euler_y)
# plt.title('Euler')

# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.plot(etd_x, etd_y)
# plt.title('ETD')

# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# ax3.plot(rk_x, rk_y)
# plt.title('RK')

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.plot(euler_x, euler_y, label='Euler')
ax4.plot(etd_x, etd_y, label='ETD')
ax4.plot(rk_x, rk_y, label='RK')
plt.title('RK , ETD, Euler')

plt.xlabel('Time')
plt.ylabel('y (Displacement)')
plt.legend()
plt.grid(True)
plt.show()
