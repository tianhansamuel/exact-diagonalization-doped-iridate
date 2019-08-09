from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

nx=100
ny=100
EQ=[[0 for i in range(nx)] for j in range(ny)]
LX=100
LY=100
delta=0.25
DD=3.398
chi=7.064
mu=-0.93
gt=2*delta/(1+delta)
ff=open('energy_fluctuation.dat','w')
for i1 in range(0,2*LX):
  kx=4*pi*(i1-LX)/(3*(sqrt(3))*LX)        
  for i2 in range(0,2*LY):
    ky=4*pi*(i2-LY)/(3*(sqrt(3))*LX)
    kp=(sin(kx*sqrt(3)))**2+(sin(kx*sqrt(3)*0.5-1.5*ky))**2+(sin(kx*sqrt(3)*0.5+1.5*ky))**2    
    E=sqrt(1+4*cos(0.5*sqrt(3)*kx)*cos(1.5*ky)+4*(cos(0.5*sqrt(3)*kx))**2)
    ff.write(str(E)+'\t')
  ff.write('\n')
X=np.arange(0,1,1.0/LX)
Y=np.arange(0,1,1.0/LY)
X,Y=np.meshgrid(X, Y)
