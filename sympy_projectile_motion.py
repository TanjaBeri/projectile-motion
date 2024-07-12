from sympy import symbols, Eq, solve, sin, cos, pi

v0, angle, t, g = symbols('v0 angle t g')
x, y = symbols('x y')
theta = angle * pi / 180

eq1 = Eq(x, v0 * cos(theta) * t)
eq2 = Eq(y, v0 * sin(theta) * t - 0.5 * g * t**2)

trajectory_eq = solve((eq1,eq2),(x,y))
print(trajectory_eq)



