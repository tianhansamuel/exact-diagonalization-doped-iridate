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
NB1=10
delta=0.1
gt=2.0*delta/(1+delta)
g1=4.0/(1+delta)**2
DD=0.1
mu=0.1
chi=0.1
TT=gt*DD*0.5
J=1.5
NI=20
NBB=12
ff=open('dopage.dat','w')

for lll in range(1,NBB):
 delta=0.6*lll/NBB
 DIS=20.0
 
 gt=2.0*delta/(1+delta)
 g1=4.0/(1+delta)**2
 for p1 in range(1,NI):
  DD=1.0+2.0*p1/NI 
  for p2 in range(1,NI):
   chi=3.5+5.0*p2/NI
   for p3 in range(1,NI):
    mu=-(gt)*sqrt(6)*p3/NI
    NOM=0
    DMS=DCS=DDS=0
    for i in range(0,NB1):
     for j in range(0,i):
      px=(j*1.0/NB1-0.5*i/NB1)*4*pi/(3*sqrt(3))+0.01/NB1
      py=sqrt(3)*0.5*i/NB1*4*pi/(3*sqrt(3))+0.01/NB1
      for k in range(0,6):
       qqx=0.5*px+sqrt(3)*0.5*py
       qqy=-0.5*sqrt(3)*px+0.5*py
       kx=qqx
       ky=qqy
       NOM=NOM+1
       kp=(sin(kx*sqrt(3)*0.5+0.5*ky))**2+(sin(kx*sqrt(3)*0.5-0.5*ky) )**2+(sin(ky))**2
       E1=sqrt((3+kp)*(gt+chi)**2+4*kp*(DD**2)+mu**2+2*sqrt((3+kp)*(gt+chi)**2*(mu**2+kp*(DD)**2)))
       E2=sqrt((3-kp)*(gt+chi)**2+4*kp*(DD**2)+mu**2+2*sqrt((3-kp)*(gt+chi)**2*(mu**2+kp*(DD)**2)))
       E3=sqrt((3+kp)*(gt+chi)**2+4*kp*(DD**2)+mu**2-2*sqrt((3+kp)*(gt+chi)**2*(mu**2+kp*(DD)**2)))
       E4=sqrt((3-kp)*(gt+chi)**2+4*kp*(DD**2)+mu**2-2*sqrt((3-kp)*(gt+chi)**2*(mu**2+4*kp*(DD)**2)))
       ee1=sqrt((3+kp)*(gt+chi)**2*(mu**2+kp*(DD)**2))
       ee2=sqrt((3-kp)*(gt+chi)**2*(mu**2+kp*(DD)**2))
      
       DEM1=mu/E1+2*mu*(3+kp)*(gt+chi)**2/(E1*ee1)
       DED1=DD*kp*(1.0/E1+2*(3+kp)*(gt+chi)**2)/(E1*ee1)
       DEC1=(gt+chi)*(3+kp)/E1+2*sqrt((3+kp)*(mu**2+DD**2*kp))/E1
      
       DEM2=mu/E2+2*mu*(3-kp)*(gt+chi)**2/(E2*ee2)
       DED2=DD*kp*(1.0/E2+2*(3-kp)*(gt+chi)**2)/(E2*ee2)
       DEC2=(gt+chi)*(3-kp)/E2+2*sqrt((3-kp)*(mu**2+DD**2*kp))/E2

       DEM3=mu/E3-2*mu*(3+kp)*(gt+chi)**2/(E3*ee1)
       DED3=DD*kp*(1.0/E3+2*(3+kp)*(gt+chi)**2)/(E3*ee1)
       DEC3=(gt+chi)*(3+kp)/E3-2*sqrt((3+kp)*(mu**2+DD**2*kp))/E3
 
       DEM4=mu/E4-2*mu*(3-kp)*(gt+chi)**2/(E4*ee2)
       DED4=DD*kp*(1.0/E4-2*(3-kp)*(gt+chi)**2)/(E4*ee2)
       DEC4=(gt+chi)*(3-kp)/E4-2*sqrt((3-kp)*(mu**2+DD**2*kp))/E4
      
       DMS=DMS+DEM1+DEM2+DEM3+DEM4
       DDS=DDS+DED1+DED2+DED3+DED4
       DCS=DCS+DEC1+DEC2+DED3+DED4
       

    DMS=DMS/NOM
    DDS=DDS*8*g1*J/(9*NOM)
    DCS=DCS*8*g1*J/(9*NOM)
    DIFF=5*abs(delta-DMS)**2+(abs(DD-DDS)**2+abs(chi-DCS)**2)
    if DIFF<DIS:
      DIS=DIFF
      DMS0=delta
      DDS0=DDS
      DCS0=DCS
 ff.write(str(DMS0)+'\t')
 ff.write(str(DDS0)+'\t')
 ff.write(str(DCS0)+'\t')

 ff.write(str(DIS)+'\t')
 ff.write('\n')

 print 'delta'
 print DMS0
 print 'Delta'
 print DDS0
 print 'chi'
 print DCS0
 print 'mu'
 print mu
 print DIS
#X=np.arange(0,1,1.0/LX)
#Y=np.arange(0,1,1.0/LY)
#X,Y=np.meshgrid(X, Y)
