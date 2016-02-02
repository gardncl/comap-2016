import numpy as np
import matplotlib.pyplot as plt

def time_step(violations,coor,x_length,y_length,y,a,b,n):
    T = 0.0019259230725
    s = 6*10**(-4)
    h = (b-a)/n
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
    lvls = [0,.8,1.6,2.4,3.2,4.0,4.8,5.6,6.4]
    fig.colorbar(z, ax=ax,ticks=lvls)

 
def main():
    years = 15
    n = 2000
    x_length = 280
    y_length = 160
    y = np.matrix(np.zeros((y_length,x_length)))
    violations = np.array([111,153,67,109,507,636,765,795,142,81])
    coor = np.matrix([[13,10],[15,17],[102,90],[130,138],[160,140],[170,150],[195,140],[230,145],[220,125],[195,118]])
    for i in range(0,len(violations)):
        y[coor[i,1],coor[i,0]] = np.log(violations[i])
    scalar_field = time_step(violations,coor,x_length,y_length,y,0,years,n)
    scalar_field = np.array(scalar_field) 
    contour_plot(x_length,y_length,scalar_field)
    aquifer_pulls = np.matrix([[140,160],[120,240],[5,140],[10,250],[10,210],[20,260]])
    print("Pollution levels for aquifers:")    
    for i in range(0,len(aquifer_pulls)):
        print("["+str(i)+"]: "+str(scalar_field[aquifer_pulls[i,0],aquifer_pulls[i,1]]))
        
main()