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
E0=0
E1=0

NNN=0
for i1 in range(0,2*LX):
  kx=4*pi*(i1-LX)/(3*(sqrt(3))*LX)        
  for i2 in range(0,2*LY):
    ky=2*pi*(i2-LY)/(3*LY)
    EE0=sqrt(3+sqrt((sin(sqrt(3)*kx))**2+(sin(sqrt(3)*kx*0.5+1.5*ky))**2)+(sin(sqrt(3)*kx*0.5-1.5*ky)**2))
    EE1=sqrt(4*(cos(sqrt(3)*0.5*kx))**2+4*cos(sqrt(3)*0.5*kx)*cos(1.5*ky)+1)
    E0=E0+EE0
    E1=E1+EE1
    NNN=NNN+1
E0=E0/NNN
E1=E1/NNN
print E0
print E1
