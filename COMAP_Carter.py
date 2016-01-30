# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:49:42 2016

@author: crhea
"""
import numpy as np
import matplotlib.pyplot as plt
s=20
y = np.matrix(np.zeros((20,20)))
def time_step(a,b,n):
    #y[0,0] = y_init
    y[0,0] = 100
    y[10,10] = 100
    h = (b-a)/n
    t_0=a
    for i in range(0,s):
        t_i = t_0+i*h
        for i in range(0,s-1):
            for j in range(0,s-1):
                y[i,j] = abs(t_i*(y[i+1,j]-4*y[i,j]+y[i-1,j]+y[i,j+1]+y[i,j-1])+y[i,j])
    return y
    
scalar_field = time_step(0,1000,10)
scalar_field = np.array(scalar_field)
x_axis = np.linspace(0,s,s)
y_axis = np.linspace(0,s,s)

X, Y = np.meshgrid(x_axis, y_axis, copy=False, indexing='xy')
plt.contourf(X, Y, scalar_field)    
