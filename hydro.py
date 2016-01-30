# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:16:18 2016

@author: crhea
"""

import numpy as np
import matplotlib.pyplot as plt
import time as t
def time_step(s,y,a,b,n):
    #y[0,0] = y_init
    
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
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(x_axis, y_axis, copy=False, indexing='xy')
    z = plt.contourf(X, Y, field)  
    fig.colorbar(z, ax=ax)

   
def main():
    s=20
    y = np.matrix(np.zeros((s,s)))
    
    y[5,5] = 100
    #for i in range(0,1000):
    scalar_field = time_step(s,y,0,10,1000)
    scalar_field = np.array(scalar_field)
    contour_plot(s,scalar_field)
        #t.sleep(1)
        
main()