import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math

# Points and lines
def points_and_lines():
    plt.plot([-1, 3], [-3, 9])

    # points are in form (x,y)

    plt.plot(-1, -3, 'r*')
    plt.plot(3, 9, 'ro')
    plt.axis([-4, 5, -5, 10])
    plt.show()

def scatter_plots():
    x = [3.2,4.54,5.334,6]
    y = [5,4,8.34,2.444]
    plt.scatter(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def polynomials():
    x = np.linspace(-4,4,100)
    y = x**2+x**(3)
    plt.plot(x,y,label = '$x^2+x^3$',linewidth=2,\
             linestyle = '--', color='b')
    # dollar sign at start and end for latex format
    plt.legend()
    plt.ylim([-20,20])
    plt.xlim([-10,10])
    # or plt.axis([-10,10,-20,20])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Multiple plots on the same axis
def multiple_plots():
    x = np.linspace(-4,4,100)
    y = x**2+x**(3) # function
    g = 1 / x  # function
    plt.plot(x,y,label='$x^2+x^3',linewidth=2,\
             linestyle='--',color='b')
    plt.plot(x,g,label='$1/x$',color='r')

    plt.legend()
    plt.ylim([-20,20])
    plt.xlim([-10,10])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show() # all plots before plt.show() will be shown on same plot

def transcendental_func():
    x = np.linspace(-4,4,200)
    y=np.cos(x**2)+x**2
    plt.plot(x,y,label='f')
    plt.legend()
    plt.show()

def subplots():
    x=sym.symbols('x')
    xx=sym.symbols('xx')
    x=np.linspace(-4,4,200)
    xx=np.linspace(-10,10,200) # domain for 2nd (g) function

    f = np.cos(x**2)+x
    g = np.exp(xx)

    fig, axs = plt.subplots(1,2,figsize=(8,6))
    # 1 row and 2 columns

    # for f plot
    axs[0].plot(x,f,label='f')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('f')
    axs[0].legend()

    # for g plot
    axs[1].plot(x,g,label='g',color='r')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('g')
    axs[1].legend()

    plt.show()

def plots_in_sympy():
    x = sym.symbols('x')
    y = sym.cos(x)*x**3
    p=sym.plotting.plot(y,(x,-7.5,7.5),xlabel='x',\
                        ylabel='y',title='plot',legend=True,line_color='red')

    #(x,-7.5,7.5) is the domain


def mul_same_axis_sympy():
    x = sym.symbols('x')
    y = sym.cos(x)*x**2
    g = sym.exp(x)
    p = sym.plotting.plot(y,(x,-7.5,7.5),xlabel='x',ylabel='y',\
                          legend=True,line_color='red',show=False)
    p.extend(sym.plotting.plot(g,(x,-7.5,7.5),show=False))
    p.title='Functions'
    p.ylim=[-20,100] # y axis limit
    p.xlim=[-10,10] # x axis limit
    p.show()

def plot_3d():
    x,y=sym.symbols('x,y')
    f=x**2+y # function
    sym.plotting.plot3d(f,(x,-10,10),(y,-10,10))

def special_case_plots():
    x = sym.symbols('x')
    y = (x)*sym.exp(x)

    #trying to find turning point here
    derivative = sym.diff(y)
    display(Math(sym.latex(derivative)))
    sol = sym.solve(derivative)
    print(sol)

    # plotting part
    yxx = sym.lambdify(x,y) # to make a func callable
    xx = np.linspace(-5,5,50) # domain of the efunction
    # easy to remember: x is algebraic variable for algebraic manipulations.
    # to plot a graph, we need another variable (xx) which can be assigned a domain.
    plt.plot(xx,yxx(xx),label='%s' %(sym.latex(y)))
    plt.ylim([-2,10])
    plt.legend()
    plt.grid(True)
    plt.sho

def piecewise_func():
    x = sym.symbols('x')
    piece1 = x  # for x<0
    piece2 = sym.cos(x)  # for x>0 snd x<5
    piece3 = 1/x  # for x>5

    # put them together
    y = sym.Piecewise((piece1,x<0),(piece2,(x>0) & (x<5)),(piece3,x>=5))

    # making another xx variable to give domain to the func
    xx = np.linspace(-5,25,100)
    fxx = sym.lambdify(x,y)

    plt.plot(xx,fxx(xx),'b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

def comic_graph():
    x = np.linspace(-4, 4, 100)
    y = x ** 2 + x ** (3)
    plt.xkcd()
    plt.plot(x, y, label='$x^2+x^3$', linewidth=2, \
             linestyle='--', color='b')
    # dollar sign at start and end for latex format
    plt.legend()
    plt.ylim([-20, 20])
    plt.xlim([-10, 10])
    # or plt.axis([-10,10,-20,20])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()