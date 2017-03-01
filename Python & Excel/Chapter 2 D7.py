# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:02:21 2017

@author: FANGXU
"""

import pandas as pd
import numpy as np
import pylab as py
import scipy.interpolate as IP
import scipy.optimize as OP

df = pd.read_excel("Chapter 2 D7.xlsx","Sheet1")

x_data = df["x_EtOH"].values
y_data = df["y_EtOH"].values

# (a)
print "(a)"

y_x = IP.interp1d(x_data,y_data)

def y_l(x):
    return 10/3.0*0.46 - (7/3.0)*x 
    
def f(x):
    return y_x(x) - y_l(x)
    
x = OP.fsolve(f, 0.5)
print "x1 = " + str(x)
print "y1 = " + str(y_x(x))

def y_l2(x):
    return (7/3.0)*0.395039 - 4/3.0*x

def f2(x):
    return y_x(x) - y_l2(x)
    
x = OP.fsolve(f2, 0.5)
print "x2 = " + str(x)
print "y2 = " + str(y_x(x))

#py.plot(x_data,y_data)
#py.plot(x_data,y_l(x_data))
#py.plot(x_data,y_l2(x_data))
#py.ylim(0,1)
#py.title("Chapter 2 D7a")
#py.legend(["1","2","3"], loc = "lower right")

# (b)
print "\n(b)"

def y_l3(x):
    return (1/0.6)*0.46 - 0.4/0.6*x

def f3(x):
    return y_x(x) - y_l3(x)
    
x = OP.fsolve(f3, 0.5)
print "x = " + str(x)
print "y = " + str(y_x(x))

py.plot(x_data,y_data)
py.plot(x_data,y_l3(x_data))
py.ylim(0,1)
py.title("Chapter 2 D7b")
py.legend(["2","1"], loc = "lower right")