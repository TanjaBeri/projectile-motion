import numpy as np
import matplotlib.pyplot as plt
from math import *

g = 9.81

def example_1():
    # Input data
    h = float(input("Enter height of the object:\n"))
    u = float(input("Enter initial speed of the object:\n"))

    g = 9.81
    # Time of flight
    t = sqrt(2*h/g)
    # Range of projectile
    R = u * t

    print(f"Time of flight = {round(t,3)} s")
    print(f"Range of projectile = {round(R,3)} m")

def example_2():
    angle = float(input("Enter the angle in degrees:\n"))
    angle = radians(angle)
    u = float(input("Enter initial speed of the object:\n"))
    # evaluating range
    R = (u ** 2 * sin(2*angle)) / g

    #  maximum height
    h_max = (u ** 2 * (sin(angle)**2)) / 2 * g

    x = np.linspace(0, R, 1000)

    # solving func for y
    y = x * tan(angle) - 0.5 * ((g * x**2) / (u**2 * (cos(angle)**2)))

    # data plotting
    plt.plot(x,y, color = 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

    # print data in tabular form
    print(f"{'S. No.':^10}{'x':^10}{'y':^10}")
    for i in range(len(x)):
        print(f"{i + 1:^10}{round(x[i], 3):^10}{round(y[i], 3):^10}")

def example_3():
    #angle = float(input("Enter the angle in degrees:\n"))
    u = float(input("Enter initial speed of the object:\n"))
    # evaluating range
    for angle in range(0,100,10):
        angle_deg = angle # for legend in plot
        angle = radians(angle)
        R = (u ** 2 * sin(2 * angle)) / g

        #  maximum height
        h_max = (u ** 2 * (sin(angle) ** 2)) / 2 * g

        x = np.linspace(0, R, 1000)

        # solving func for y
        y = x * tan(angle) - 0.5 * ((g * x ** 2) / (u ** 2 * (cos(angle) ** 2)))

        # data plotting

        plt.plot(x, y, label = f'angle = {angle_deg}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
    plt.show()

def example_4():
    # velocity at the start
    u = 100

    # angle of projectile at start
    angle = 45
    angle = radians(angle)

    # elevation of starting point above the ground
    y0 = 100

    # time of flight
    a = g
    b = -2 * u * sin(angle)
    c = -2 * y0

    # coefficient array
    coeff = np.array([a,b,c])

    # finding roots
    t1, t2 = np.roots(coeff)
    print(f"t1 = {t1}s and t2 = {t2} s")

    # max height
    # from throwing point
    h1 = (u ** 2 * (sin(angle) ** 2)) / (2 * g)

    # total height
    h_max = h1 + y0
    print(f"h_max = {h_max} m")

    # range
    r = u * cos(angle) * max(t1,t2)
    print(f"range = {r} m")

    # plotting
    # plotting inclined surface
    plt.plot([0,r],[0,-y0],linewidth=5)
    # plotting y = 0 line
    plt.plot([0,r],[0,0],'k',linewidth=1)

    # array of x
    x = np.linspace(0,r,100)

    # evaluating y based on x
    y = x * tan(angle) - 0.5 * (g * x**2) / (u**2 * (cos(angle)**2))

    # plotting projectile motion
    plt.plot(x,y,'r-',linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# prvi set koord x y z
x1 = float(input("Enter x1 coordinate:\n"))
y1 = float(input("Enter y1 coordinate:\n"))
z1 = float(input("Enter z1 coordinate:\n"))

# drugi set koord x y z
x2 = float(input("Enter x2 coordinate:\n"))
y2 = float(input("Enter y2 coordinate:\n"))
z2 = float(input("Enter z2 coordinate:\n"))

# unos vremena
t1 = float(input("Enter time 1:\n"))
t2 = float(input("Enter time 2:\n"))

positions = np.array([[x1,y1,z1],[x2,y2,z2]])
time_points = np.array([t1,t2])

# racunanje dx
dx = np.diff(positions,axis=0)

# racunanje dt
dt = np.diff(time_points)
#dt = 0.01

print("dt", dt)
# racunanje pocetne brzine
initial_velocity = dx / dt[:,np.newaxis] # prebacivanje dt iz vrste u kolone
v0 = sqrt((initial_velocity[0,0])**2 + (initial_velocity[0,1])**2 + (initial_velocity[0,2])**2)

print("Velocity:",initial_velocity)
print("Velocity :", v0)



# racunanje ugla
pos1 = np.array([x1,y1,z1])
pos2 = np.array([x2,y2,z2])

vector_pos = pos2 - pos1

# racunanje ugla u radijanima
angle_rad = np.arctan2(np.linalg.norm(np.cross(pos1, pos2)), np.dot(pos1, pos2))

print("Angle in rad: ",angle_rad)
print("Angle in deg:",degrees(angle_rad))


# racunanje trajektorije
# evaluating range
R = (v0 ** 2 * sin(2*angle_rad)) / g
print("R=",R)

# calculating v0x and v0y
'''v0x = v0*np.cos(angle_rad)
print("v0x=",v0x)
v0y = v0*np.sin(angle_rad)
print("v0y=",v0y)'''

# taking v0x and v0y from array initial_velocity
v0x = initial_velocity[0,0]
print("v0x=",v0x)
v0y = initial_velocity[0,1]
print("v0y=",v0y)

# calc. total time tf
tf = 2 * (v0y/g)
print("tf=",tf)
num_points = int(tf / 0.01)
t = np.linspace(t1,tf,num_points)
print("num_points=",num_points)

# calc. x and y with respect to t
x = x1 + v0x * t
print("x=",x)
y = y1 + v0y * t - 0.5 * g * t**2
print("y=",y)



# data plotting
plt.scatter([x1,x2],[y1,y2],color='r')
plt.plot([x1,x2],[y1,y2],color='r')
plt.plot(x,y,'k-')
plt.title("Projectile motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
print(f'Time of flight = {tf} s')


