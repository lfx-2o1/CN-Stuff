# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 08:52:56 2017

@author: FANGXU
"""

import pandas as pd
import scipy.interpolate as IP
import scipy.optimize as OP
import numpy as np
import pylab as py

E_df = pd.read_excel('Chapter 2 D3.xlsx', 'K_Ethane')
B_df = pd.read_excel('Chapter 2 D3.xlsx', 'K_n-Butane')

T_e = E_df['T'].values
K_e = E_df['K'].values
T_b = B_df['T'].values
K_b = B_df['K'].values

K_E = IP.interp1d(T_e,K_e)
K_B = IP.interp1d(T_b,K_b)

# (a)
print '(a)'

x_data = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3])

def f(T,x):
    return x*K_E(T) + (1-x)*K_B(T) - 1

T_data = []
for i in range(len(x_data)):
    T = OP.fsolve(f, 0, args = (x_data[i]))
    T_data.append(float(T))

T_data = np.array(T_data)
y_data = x_data * K_E(T_data)    
    
print 'T = ' + str(T_data)
print 'y = ' + str(y_data)

#(b)
print '\n(b)'

x_data = np.linspace(0, 1, 21)

T_data = [63.19]
for i in range(1,len(x_data)-1):
    T = OP.fsolve(f, 0, args = (x_data[i]))
    T_data.append(float(T))

T_data.append(-37.47)    
T_data = np.array(T_data)

y_data = x_data * K_E(T_data)
y_data[-1] = 1

print 'T = ' + str(T_data)
print 'y = ' + str(y_data)

#py.plot(x_data, T_data)
#py.plot(y_data, T_data)
#py.title('Chapter 2 D3')
#py.xlabel('$x$, $y$', size = 16)
#py.ylabel('$T\degree$C', size = 16)

# (c)
print '\n(c)'

y_E = IP.interp1d(x_data, y_data)

def y_l(x):
    return (0.75 - 1.5 * x)

def f2(x):
    return y_E(x) - y_l(x)

x = OP.fsolve(f2, 0.12)
print 'x = ' + str(x)
print 'y = ' + str(y_E(x))

#py.plot(x_data,y_data)
#py.plot(x_data,y_l(x_data))
#py.ylim(0,1)
#py.title("Chapter 2 D3c")
#py.legend(["$y-x$", "Mat. Balance"], loc = "lower right")