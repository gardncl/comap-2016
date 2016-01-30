# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:16:18 2016

@author: crhea
"""

import numpy as np
import matplotlib.pyplot as plt
s=20
y = np.matrix(np.zeros((20,20)))
def time_step(a,b,n):
    #y[0,0] = y_init
    y[10,10] = 100
    #y[10,10] = .0001
    h = (b-a)/n
    t_0=a
    for i in range(0,s):
        t_i = t_0+i*h
        for i in range(0,s-1):
            for j in range(0,s-1):
                y[i,j] = t_i*(y[i+1,j]-4*y[i,j]+y[i-1,j]+y[i,j+1]+y[i,j-1])+y[i,j]
    return y
def contour_plot(n,field):
    x_axis = np.linspace(0,n,n)
    y_axis = np.linspace(0,n,n)
    
    X, Y = np.meshgrid(x_axis, y_axis, copy=False, indexing='xy')
    plt.contourf(X, Y, field)    

   
def main():
    scalar_field = time_step(0,10,1000)
    scalar_field = np.array(scalar_field)
    contour_plot(20,scalar_field)
main()