# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:16:18 2016

@author: crhea
"""

import numpy as np
import matplotlib.pyplot as plt
import time as t
def time_step(x_length,y_length,y,a,b,n):
    #y[0,0] = y_init
    
    #y[10,10] = .0001
    h = (b-a)/n
    t_0=a
    for i in range(0,n):
        t_i = t_0+i*h
        for i in range(0,y_length-1):
            for j in range(0,x_length-1):
                y[i,j] = t_i*(y[i+1,j]-4*y[i,j]+y[i-1,j]+y[i,j+1]+y[i,j-1])+y[i,j]
    return y
def contour_plot(x_length,y_length,field):
    x_axis = np.linspace(0,x_length,x_length)
    y_axis = np.linspace(0,y_length,y_length)
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(x_axis, y_axis, copy=False, indexing='xy')
    z = plt.contourf(X, Y, field)  
    
    fig.colorbar(z, ax=ax)

   
def main():
    x_length = 280
    y_length = 160
    y = np.matrix(np.zeros((y_length,x_length)))
    y[15,15] = 264
    y[110,210] = 1783
    y[105,180] = 1252
    y[80, 130] = 67
    #for i in range(0,1000):
    scalar_field = time_step(x_length,y_length,y,0,.1,10)
    scalar_field = np.array(scalar_field)
    contour_plot(x_length,y_length,scalar_field)
        #t.sleep(1)
        
main()