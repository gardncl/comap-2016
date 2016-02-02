
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Jan 30 14:11:30 2016
 
=======
Created on Fri Jan 29 22:16:18 2016
>>>>>>> d70314b0477dc941dd80e605757a61503bebec30
@author: crhea
"""
 
 
 
# -*- coding: utf-8 -*-
##Created on Fri Jan 29 22:16:18 2016
import numpy as np
import matplotlib.pyplot as plt
T = 0.0019259230725
s = 6*10**(-4)
#s=1
def time_step(x_length,y_length,y,a,b,n):
    h = (b-a)/n
#    t_0=a
    
    for i in range(0,n):
#        t_i = t_0+i*h
        for i in range(0,len(violations)):
            y[coor[i,1],coor[i,0]] = violations[i]

        for i in range(0,y_length-1):
            for j in range(0,x_length-1):
                y[i,j] = abs(((T*h)/(s))*(y[i+1,j]-4*y[i,j]+y[i-1,j]+y[i,j+1]+y[i,j-1])+y[i,j])
    return y
def contour_plot(x_length,y_length,field):
    x_axis = np.linspace(0,x_length,x_length)
    y_axis = np.linspace(0,y_length,y_length)
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(x_axis, y_axis, copy=False, indexing='xy')
    z = plt.contourf(X, Y, field,cmap='summer')  
#    l_f = LogFormatter(10, labelOnlyBase=False)
#    lvls = np.logspace(0,20,100)
#    cbar = plt.colorbar(z,ticks=lvls, format=l_f)
#    plt.show(cbar)
 
    fig.colorbar(z, ax=ax,ticks=lvls)
     
    #fig.colorbar(z, ax=ax)
 
    
x_length = 280
y_length = 160
y = np.matrix(np.zeros((y_length,x_length)))
violations = np.array([np.log(111),np.log(153),np.log(67),np.log(109),np.log(507),np.log(636),np.log(765),np.log(795),np.log(142),np.log(81)])
coor = np.matrix([[13,10],[15,17],[102,90],[130,138],[160,140],[170,150],[195,140],[230,145],[220,125],[195,118]])
for i in range(0,len(violations)):
    y[coor[i,1],coor[i,0]] = violations[i]
scalar_field = time_step(x_length,y_length,y,0,15,2000)
scalar_field = np.array(scalar_field)

lvls = [0,.8,1.6,2.4,3.2,4.0,4.8,5.6,6.4]
     
contour_plot(x_length,y_length,scalar_field)

#y then x  coordinates
aquifer_pulls = np.matrix([[140,160],[120,240],[5,140],[10,250],[10,210],[20,260]])
for i in range(0,len(aquifer_pulls)):
    print(scalar_field[aquifer_pulls[i,0],aquifer_pulls[i,1]])