import numpy as np
import matplotlib.pyplot as plt
from moving_average_filter import X_kol1,Y_kol1,Z_kol1
from moving_average_filter import X_list,Y_list,Z_list

g = 9.81
# racunanje V0x, V0y, V0z
# Pozicije u dva razlicita vremena (primer)
x1, y1, z1 = X_list[0],Y_list[0], Z_list[0]    # Pozicija u trenutku t1
x2, y2, z2 = X_list[1],Y_list[1],Z_list[1]    # Pozicija u trenutku t2

print(f"x1 = {x1}, y1 = {y1}, z1 = {z1}")
print(f"x2 = {x2}, y2 = {y2}, z2 = {z2}")


# Vremenski trenuci
t1 = 0
t2 = 0.1

# Calculate the displacement vector components
dx = x2 - x1
print("dx=",dx)
dy = y2 - y1
print("dy = ",dy)
dz = z2 - z1
print("dz = ",dz)

# Calculate the time interval
dt = t2 - t1
print("dt = ",dt)
# Calculate the velocity components
vx = dx / dt
vy = dy / dt
vz = dz / dt
print(f"vx = {vx}, vy = {vy}, vz = {vz}")

# Calculate the magnitude of the horizontal velocity component
vh = np.sqrt(vx**2 + vy**2)
v0_int = np.sqrt(vx**2 + vy**2 + vz**2)
print(f"vh = {vh}, v0_int = {v0_int}")
# Calculate the angle in radians
alpha_rad = np.arctan2(vz, vh)
beta_rad = np.arctan2(vy,vx)
print(f"alpha = {alpha_rad}, beta = {beta_rad}")


print("Inetenzitet vektora pocetne brzine: ",v0_int)
print("Angle with respect to the horizontal plane:", alpha_rad)

# vektori brzine
v0 = np.array([vx,vy,vz])

print("v0=",v0)

# vektori pocetnog polozaja r0
r0 = np.array([x1,y1,z1])

print("r0=",r0)

# matematicki model kosog hica - od Jefimije

# racunanje ukupnog vremena tf
t = []
t.append(t1)
t.append(t2)
rxf = []
ryf = []
rzf = []
while True:
    d_t = 0.01
    t2 = t2+d_t
    t.append(t2)
    rx = v0_int * np.cos(alpha_rad) * np.cos(beta_rad) * t2 + r0[0]
    rxf.append(rx)
    ry = v0_int * np.cos(alpha_rad) * np.sin(beta_rad) * t2 + r0[1]
    ryf.append(ry)
    rz = v0_int * np.sin(alpha_rad) * t2 - 0.5 * g * (t2 ** 2) + r0[2]
    rzf.append(rz)

    if  rz < 0.5:
        break

t = np.array(t)
rxf = np.array(rxf)
ryf = np.array(ryf)
rzf = np.array(rzf)
print("t=",t)
print(type(t))
suma = 0
for n in t:
    suma = suma + n
print("Ukupno tacaka: ",suma)
# calc. total time tf
'''tf = 2 * (vy/g)
print("tf=",tf)
num_points = int(tf / 0.01)
t = np.linspace(t1,tf,num_points)
print("num_points=",num_points)
print("t=",t)
print(type(t))'''

#rx= v0_int * np.cos(alpha_rad) * np.cos(beta_rad) * t + r0[0]

#ry = v0_int * np.cos(alpha_rad) * np.sin(beta_rad) * t + r0[1]

#rz = v0_int * np.sin(alpha_rad) * t - 0.5 * g * t**2 + r0[2]



r = rxf + ryf + rzf

print("r=",r)
print("rx=",rxf)
print("ry=",ryf)
print("rz=",rzf)

# data plotting
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(rxf,ryf,rzf,label = 'Kosi hitac izracunat matematicki')
ax.plot(X_list,Y_list,Z_list,'r',label='Usrednjene vredn.')

ax.set_title('3D projectile motion1')
plt.show()