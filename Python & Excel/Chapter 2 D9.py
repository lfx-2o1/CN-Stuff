# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:07:20 2017

@author: FANGXU
"""

import numpy as np
import numpy.linalg as LA

# Take 100 g as base

n_e = 30 / 46.07
n_w = 70 / 18.016
x_e = n_e / (n_e + n_w)
x_w = 1 - x_e
c_pm = x_e*37.96 + x_w*18
h_F = c_pm * (200 - 0)
MW_m = x_e*46.07 + x_w*18.016
h_Fkg = h_F / MW_m

A = [[1, 1],[0.15,0.62]]
b = [1000, 300]
x = np.matmul(LA.inv(A),b)

print "n_e = " + str(n_e)
print "n_w = " + str(n_w)
print "x_e = " + str(x_e)
print "x_w = " + str(x_w)
print "c_pm = " + str(c_pm) + " kcal/(kmol*C)"
print "h_F = " + str(h_F) + " kcal/kmol"
print "MW_m = " + str(MW_m) + " kg/kmol"
print "h_Fkg = " + str(h_Fkg) + " kcal/kg"
print "x = " + str(x)