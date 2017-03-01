# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:45:57 2017

@author: FANGXU
"""

import pandas as pd
import scipy.interpolate as IP
import scipy.optimize as OP

z_iC4 = 0.4
z_C5 = 0.25
z_C6 = 0.35

iC4_df = pd.read_excel("Chapter 2 D19.xlsx","iC4")
C5_df = pd.read_excel("Chapter 2 D19.xlsx","C5")
C6_df = pd.read_excel("Chapter 2 D19.xlsx","C6")

K_iC4_data = iC4_df["K"].values
T_iC4_data = iC4_df["T"].values
K_C5_data = C5_df["K"].values
T_C5_data = C5_df["T"].values
K_C6_data = C6_df["K"].values
T_C6_data = C6_df["T"].values

K_iC4_T = IP.interp1d(T_iC4_data,K_iC4_data)
K_C5_T = IP.interp1d(T_C5_data,K_C5_data)
K_C6_T = IP.interp1d(T_C6_data,K_C6_data)

def f(T):
    K_C6 = K_C6_T(T)
    K_C5 = K_C5_T(T)
    K_iC4 = K_iC4_T(T)
    VoF = 0.1 / (0.9*K_C6 + 0.1)
    x_iC4 = z_iC4 / ((1-VoF) + VoF*K_iC4)
    x_C5 = z_C5 / ((1-VoF) + VoF*K_C5)
    x_C6 = z_C6 / ((1-VoF) + VoF*K_C6)
    return x_iC4 + x_C5 + x_C6 - 1
    

T = OP.fsolve(f, 60)
print "T = " + str(T)

K_C6 = K_C6_T(T)
K_C5 = K_C5_T(T)
K_iC4 = K_iC4_T(T)
VoF = 0.1 / (0.9*K_C6 + 0.1)
x_iC4 = z_iC4 / ((1-VoF) + VoF*K_iC4)
x_C5 = z_C5 / ((1-VoF) + VoF*K_C5)
x_C6 = z_C6 / ((1-VoF) + VoF*K_C6)
print "VoF = " + str(VoF)
print "x_iC4 = " + str(x_iC4)
print "x_C5 = " + str(x_C5)
print "x_C6 = " + str(x_C6)