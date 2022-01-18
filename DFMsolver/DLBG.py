# First attempt to plot the DBLG interaction potential
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def DBLG_potential(q,w):

    xiPos = np.zeros_like(q)
    xiNeg = np.zeros_like(q)

    erPos = np.zeros_like(q)
    erNeg = np.zeros_like(q)

    for i, (qi, wi) in enumerate(zip(q,w)):
        integrand_pos_temp = lambda y, k: integrand(k, y, qi, wi, 1)
        integrand_neg_temp = lambda y, k: integrand(k, y, qi, wi, -1)
        (xiPos[i], erPos[i]) = integrate.dblquad(integrand_pos_temp, 0., 1., lambda x: abs(x - qi), lambda x: x + qi)
        (xiNeg[i], erNeg[i]) = integrate.dblquad(integrand_neg_temp, 1., np.inf, lambda x: abs(x - qi), lambda x: x + qi)
    
    return xiPos + xiNeg

def integrand(k, y, qi, wi, m):
    eF = 0.01
    t = 3.16
    tp = 0.38
    a = 2.46e-10 / 1.97327e-7
    U = 0.0
    v = np.sqrt(3)*a*t/2

    xi = lambda x,s: s/2 * np.sqrt(4 * v**4 * x**4/tp**2 + U**2*(1 - 2 * v**2 * x**2/tp**2)**2)/eF - 1
    z = lambda x,s: tp/(v**2 * x**2) * ( (xi(x,s) + 1)*eF - U/2 * (1 - 2 * v**2/tp**2 * x**2) )
    Dy = 2 * k * y /np.sqrt(4 * k**2 * qi**2 - (y**2 - k**2 - qi**2)**2 ) \
        * ( (1 - z(k,1)*z(y,m))**2 * 4*k**2 * y**2 + 4*z(k,1)*z(y,m) * (k**2 + y**2 - qi**2)**2 ) \
        /( 4*k**2 * y**2 * (1 + z(k,1)**2) * (1 + z(y,m)**2) )
    return 4*Dy*m*( (xi(y,m) - xi(k,1))/(wi**2 + (xi(y,m) - xi(k,1))**2) )

def main():
    q = np.linspace(0.01,3,num=100)
    P = DBLG_potential(q,np.ones_like(q)*1e-6)
    plt.plot(q,P)
    plt.show()


if __name__ == "__main__":
    main()