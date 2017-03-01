# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:26:42 2017

@author: FANGXU
"""

import pandas as pd
import numpy as np
import pylab as py
import scipy.interpolate as IP
import scipy.optimize as OP

df = pd.read_excel('Chapter 2 D1.xlsx', 'Sheet1')

x_m = df['x_m'].values
y_m = df['y_m'].values
T = df['T'].values

#py.plot(x_m,T)
#py.plot(y_m,T)
#py.xlabel('$x$, $y$', size = 16)
#py.ylabel('$T$ $\degree$ C', size = 16)
#py.title('VLE for Methanol-Water (P = 1 atm)')

# (a)
print '(a)'

y = IP.interp1d(x_m, y_m)
x_pts = np.linspace(0,1,51)

def f(x): 
    return y(x) - (1.5 - 1.5*x)

#py.plot(x_pts, y(x_pts))
#py.plot(x_pts, (1.5 - x_pts * 1.5)) 
#py.ylim(0,1)
#py.legend(['$y$-$x$','Mat. Balance'], loc = 'lower left')
   
x = OP.fsolve(f, 0.5)
print "x = " + str(x)
print "y = " +str(y(x))

# (e)
print '\n(e)'
ym = 0.579
xm = 0.2
W_V = ym*264*32.04 + (1-ym)*264*18.01 # lb/h
W_L = xm*736*32.04 + (1-xm)*736*18.01 # lb/h
rho_wg = 18.01 * 101325 / 8.314 / (81.7 + 273)
rho_mg = 32.04 * 101325 / 8.314 / (81.7 + 273)
rho_V = (0.579 * rho_mg + (1-0.579) * rho_wg) / 10**6
MW_L = 0.2*32.04 + 0.8*18.01
V_L = 0.2*32.04/0.7914 + 0.8*18.01/1
rho_L = MW_L / V_L
F_lv = W_L / W_V * (rho_V/rho_L)**0.5

print "W_V = " + str(W_V) + " lb / h"
print "W_L = " + str(W_L) + " lb / h"
print "rho_wg = " + str(rho_wg) + " g / m3"
print "rho_mg = " + str(rho_mg) + " g / m3"
print "rho_V = " + str(rho_V) + " g / cm3"
print "MW_L = " + str(MW_L)
print "V_L = " + str(V_L)
print "rho_L = " + str(rho_L) + " g / cm3"
print "F_lv = " + str(F_lv)

A = -1.8775
B = -0.8146
C = -0.1871
D = -0.01452
E = -0.001015

lnF = np.log(F_lv)

K_drum = np.exp(A + B*lnF + C*lnF**2 + D*lnF**3 + E*lnF**4)
u_perm = K_drum * ((rho_L - rho_V)/rho_V)**0.5
MW_V = 0.579*32.04 + (1-0.579)*18.01
A_c = 264*MW_V / (u_perm * 3600 * (2.54*12) * rho_V / 453.59)
d = (4*A_c/np.pi)**0.5

print "K_drum = " + str(K_drum)
print "u_perm = " + str(u_perm)
print "MW_V = " + str(MW_V)
print "A_c = " + str(A_c)
print "d = " + str(d)

# (f)
print '\n(f)'

x_T = IP.interp1d(T, x_m)
y_T = IP.interp1d(T, y_m)
print 'x_m = ' + str(x_T(77))
print 'y_m = ' + str(y_T(77))

# (g)
print '\n(g)'

x_y = IP.interp1d(y_m,x_m)
print 'x_m = ' + str(x_y(.892))