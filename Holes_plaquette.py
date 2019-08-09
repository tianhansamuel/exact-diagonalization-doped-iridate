from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp



MP=zeros([4096,4096],'complex')
N=100
NS=0
NSS=0
ff=open('Holes_plaquette.txt','w')
ff2=open('Holes_plaquette0.txt','w')
#ff1=open('half_filling.dat','w')
NOP=6
delta=abs(NOP-6)*1.0/6
gt=2.0*delta/(1+delta)
g1=4.0/(1+delta)**2
U=6

NNN=20
t0=-1
tx=-1
ty=-1
tz=-1

for ll in range(0,NNN+1):
 
 MP=zeros([4096,4096],'complex')
 p=ll*1.0/NNN
 #ff1.write(str(p)+'\t')
 t1=p
 t2=1-p
 J1=g1*4*t1**2*1.0/U
 J2=g1*4*t2**2*1.0/U


 t1=1
 t2=0
 NP=0
 NS=0
 print t1
 print t2
 print J1
 print J2

 for p1 in range(0,4):
  for p2 in range(0,4):
   for p3 in range(0,4):
    for p4 in range(0,4):
     for p5 in range(0,4):   
      for p6 in range(0,4):
       NP=0
       if p1==0 or p1==1:
        NP=NP+1
       if p1==3:
        NP=NP+2 
       if p2==0 or p2==1:
        NP=NP+1
       if p2==3:
        NP=NP+2
       if p3==0 or p3==1:
        NP=NP+1
       if p3==3:
        NP=NP+2
       if p4==0 or p4==1:
        NP=NP+1
       if p4==3:
        NP=NP+2
       if p5==0 or p5==1:
        NP=NP+1
       if p5==3:
        NP=NP+2
       if p6==0 or p6==1:
        NP=NP+1
       if p6==3:
        NP=NP+2
       if NP==NOP:
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
        NS=NS+1
        NSS=0
        for pp1 in range(0,4):
         for pp2 in range(0,4):
          for pp3 in range(0,4):
           for pp4 in range(0,4):
            for pp5 in range(0,4):   
             for pp6 in range(0,4):
              NPP=0
              if pp1==0 or pp1==1:
               NPP=NPP+1
              if pp1==3:
               NPP=NPP+2 
              if pp2==0 or pp2==1:
               NPP=NPP+1
              if pp2==3:
               NPP=NPP+2
              if pp3==0 or pp3==1:
               NPP=NPP+1
              if pp3==3:
               NPP=NPP+2
              if pp4==0 or pp4==1:
               NPP=NPP+1
              if pp4==3:
               NPP=NPP+2
              if pp5==0 or pp5==1:
               NPP=NPP+1
              if pp5==3:
               NPP=NPP+2
              if pp6==0 or pp6==1:
               NPP=NPP+1
              if pp6==3:
               NPP=NPP+2
              if NPP==NOP:
               N2=pp1+4*pp2+16*pp3+64*pp4+256*pp5+1024*pp6
               NSS=NSS+1

# Hopping
#Hopping


            # kinetic t1 
             #12
               if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                if p1==pp2 and p2==pp1: 
                 if (p1==0 and p2==3) or (p1==1 and p2==3) or (p1==3 and p2==0) or (p1==3 and p2==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p1==2 and p2==0) or (p1==2 and p2==1) or (p1==0 and p2==2) or (p1==1 and p2==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p1==1 and p2==0 and pp1==3 and pp2==2) or (p1==1 and p2==0 and pp1==2 and pp2==3) or (p1==2 and p2==3 and pp1==1 and pp2==0) or (p1==3 and p2==2 and pp1==1 and pp2==0):
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p1==2 and p2==3 and pp1==0 and pp2==1) or (p1==0 and p2==1 and pp1==3 and pp2==2) or (p1==3 and p2==2 and pp1==0 and pp2==1) or (p1==0 and p2==1 and pp1==2 and pp2==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #23
               if abs(p1-pp1)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if p2==pp3 and p3==pp2:
                 if (p2==0 and p3==3) or (p2==1 and p3==3) or (p2==3 and p3==0) or (p2==3 and p3==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p2==2 and p3==0) or (p2==2 and p3==1) or (p2==0 and p3==2) or (p2==1 and p3==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p2==1 and p3==0 and pp2==3 and pp3==2) or (p2==1 and p3==0 and pp2==2 and pp3==3) or (p2==2 and p3==3 and pp2==1 and pp3==0) or (p2==3 and p3==2 and pp2==1 and pp3==0):
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p2==2 and p3==3 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==2 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==2 and pp3==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #34
               if abs(p1-pp1)+abs(p2-pp2)+abs(p5-pp5)+abs(p6-pp6)==0: 
                if p3==pp4 and p4==pp3:
                 if (p3==0 and p4==3) or (p3==1 and p4==3) or (p3==3 and p4==0) or (p3==3 and p4==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p3==2 and p4==0) or (p3==2 and p4==1) or (p3==0 and p4==2) or (p3==1 and p4==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p3==1 and p4==0 and pp3==3 and pp4==2) or (p3==1 and p4==0 and pp3==2 and pp4==3) or (p3==2 and p4==3 and pp3==1 and pp4==0) or (p3==3 and p4==2 and pp3==1 and pp4==0): 
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p3==2 and p4==3 and pp3==0 and pp4==1) or (p3==0 and p4==1 and pp3==3 and pp4==2) or (p3==3 and p4==2 and pp3==0 and pp4==1) or (p3==0 and p4==1 and pp3==2 and pp4==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #45
               if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p6-pp6)==0:
                if p4==pp5 and p5==pp4:
                 if (p4==0 and p5==3) or (p4==1 and p5==3) or (p4==3 and p5==0) or (p4==3 and p5==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p4==2 and p5==0) or (p4==2 and p5==1) or (p4==0 and p5==2) or (p4==1 and p5==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p4==1 and p5==0 and pp4==3 and pp5==2) or (p4==1 and p5==0 and pp4==2 and pp5==3) or (p4==2 and p5==3 and pp4==1 and pp5==0) or (p4==3 and p5==2 and pp4==1 and pp5==0):
                 
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p4==2 and p5==3 and pp4==0 and pp5==1) or (p4==0 and p5==1 and pp4==3 and pp5==2) or (p4==3 and p5==2 and pp4==0 and pp5==1) or (p4==0 and p5==1 and pp4==2 and pp5==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #56
               if  abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p5==pp6 and p6==pp5:
                 if (p5==0 and p6==3) or (p5==1 and p6==3) or (p5==3 and p6==0) or (p5==3 and p6==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p5==2 and p6==0) or (p5==2 and p6==1) or (p5==0 and p6==2) or (p5==1 and p6==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p5==1 and p6==0 and pp5==3 and pp6==2) or (p5==1 and p6==0 and pp5==2 and pp6==3) or (p5==2 and p6==3 and pp5==1 and pp6==0) or (p5==3 and p6==2 and pp5==1 and pp6==0):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p5==2 and p6==3 and pp5==0 and pp6==1) or (p5==0 and p6==1 and pp5==3 and pp6==2) or (p5==3 and p6==2 and pp5==0 and pp6==1) or (p5==0 and p6==1 and pp5==2 and pp6==3):       
                  MP[N1][N2]=MP[N1][N2]+t1*t0
             #61
               if abs(p5-pp5)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p6==pp1 and p1==pp6:
                 if (p6==0 and p1==3) or (p6==1 and p1==3) or (p6==3 and p1==0) or (p6==3 and p1==1):
                  MP[N1][N2]=MP[N1][N2]+t1*t0*(-1)**NOP
                 if (p6==2 and p1==0) or (p6==2 and p1==1) or (p6==0 and p1==2) or (p6==1 and p1==2): 
                  MP[N1][N2]=MP[N1][N2]-t1*t0*(-1)**NOP
                if (p6==1 and p1==0 and pp6==3 and pp1==2) or (p6==1 and p1==0 and pp6==2 and pp1==3) or (p6==2 and p1==3 and pp6==1 and pp1==0) or (p6==3 and p1==2 and pp6==1 and pp1==0):
                  MP[N1][N2]=MP[N1][N2]+t1*t0*(-1)**NOP
                if (p6==2 and p1==3 and pp6==0 and pp1==1) or (p6==0 and p1==1 and pp6==3 and pp1==2) or (p6==3 and p1==2 and pp6==0 and pp1==1) or (p6==0 and p1==1 and pp6==2 and pp1==3):        
                  MP[N1][N2]=MP[N1][N2]-t1*t0*(-1)**NOP


            ### t2 y 23
               if (p2==0 and p3==3 and pp2==3 and pp3==1) or (p2==2 and p3==3 and pp2==0 and pp3==0) or (p2==2 and p3==3 and pp2==1 and pp3==1) or (p2==0 and p3==0 and pp2==3 and pp3==2) or (p2==2 and p3==0 and pp2==1 and pp3==2) or (p2==1 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==0 and pp2==1 and  pp3==3) or (p2==0 and p3==2 and pp2==2 and pp3==1):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+1j*t2*ty
               if (p2==1 and p3==3 and pp2==3 and pp3==0) or  (p2==2 and p3==1 and pp2==0 and pp3==2) or (p2==3 and p3==1 and pp2==0 and  pp3==3) or (p2==3 and p3==2 and pp2==1 and  pp3==1) or (p2==3 and p3==2 and pp2==0 and pp3==0) or (p2==0 and p3==0 and pp2==2 and pp3==3) or (p2==1 and p3==1 and pp2==2 and pp3==3) or (p2==1 and p3==2 and pp2==2 and pp3==0):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-1j*t2*ty

            ### t2 y 56
               if (p5==0 and p6==3 and pp5==3 and pp6==1) or (p5==2 and p6==3 and pp5==0 and pp6==0) or (p5==2 and p6==3 and pp5==1 and pp6==1) or (p5==0 and p6==0 and pp5==3 and pp6==2) or (p5==2 and p6==0 and pp5==1 and pp6==2) or (p5==1 and p6==1 and pp5==3 and pp6==2) or (p5==3 and p6==0 and pp5==1 and  pp6==3) or (p5==0 and p6==2 and pp5==2 and pp6==1): 
                if abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+1j*t2*ty
               if (p5==1 and p6==3 and pp5==3 and pp6==0) or  (p5==2 and p6==1 and pp5==0 and pp6==2) or (p5==3 and p6==1 and pp5==0 and  pp6==3) or (p5==3 and p6==2 and pp5==1 and  pp6==1) or (p5==3 and p6==2 and pp5==0 and pp6==0) or (p5==0 and p6==0 and pp5==2 and pp6==3) or (p5==1 and p6==1 and pp5==2 and pp6==3) or (p5==1 and p6==2 and pp5==2 and pp6==0):
                if abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-1j*t2*ty


                           
             # t2 z 61
               if (p6==0 and p1==3 and pp6==3 and pp1==0) or (p6==2 and p1==3 and pp6==0 and pp1==1) or (p6==2 and p1==3 and pp6==1 and pp1==0) or (p6==2 and p1==0 and pp6==0 and pp1==2):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz*(-1)**NOP
               if (p6==1 and p1==3 and pp6==3 and pp1==1) or (p6==1 and p1==0 and pp6==3 and pp1==2) or (p6==0 and p1==1 and pp6==3 and pp1==2) or (p6==2 and p1==1 and pp6==1 and pp1==2): 
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz*(-1)**NOP
               if (p6==3 and p1==0 and pp6==0 and pp1==3) or (p6==0 and p1==1 and pp6==2 and pp1==3) or (p6==0 and p1==2 and pp6==2 and pp1==0) or (p6==1 and p1==0 and pp6==2 and pp1==3):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz*(-1)**NOP
               if (p6==3 and p1==1 and pp6==1 and pp1==3) or (p6==3 and p1==2 and pp6==0 and pp1==1) or (p6==3 and p1==2 and pp6==1 and pp1==0) or (p6==1 and p1==2 and pp6==2 and pp1==1):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tz*(-1)**NOP



  
             # t2 Z 34 
               if (p3==0 and p4==3 and pp3==3 and pp4==0) or (p3==2 and p4==3 and pp3==0 and pp4==1) or (p3==2 and p4==3 and pp3==1 and pp4==0) or (p3==2 and p4==0 and pp3==0 and pp4==2):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz
               if (p3==1 and p4==3 and pp3==3 and pp4==1) or (p3==1 and p4==0 and pp3==3 and pp4==2) or (p3==0 and p4==1 and pp3==3 and pp4==2) or (p3==2 and p4==1 and pp3==1 and pp4==2):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz
               if (p3==3 and p4==0 and pp3==0 and pp4==3) or (p3==0 and p4==1 and pp3==2 and pp4==3) or (p3==0 and p4==2 and pp3==2 and pp4==0) or (p3==1 and p4==0 and pp3==2 and pp4==3):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz
               if (p3==3 and p4==1 and pp3==1 and pp4==3) or (p3==3 and p4==2 and pp3==0 and pp4==1) or (p3==3 and p4==2 and pp3==1 and pp4==0) or (p3==1 and p4==2 and pp3==2 and pp4==1):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]-t2*tz 

             ### t2 X 12
               if (p1==0 and p2==3 and pp1==3 and pp2==1) or (p1==1 and p2==3 and pp1==3 and pp2==0) or (p1==2 and p2==3 and pp1==1 and pp2==1) or (p1==0 and p2==0 and pp1==3 and pp2==2) or (p1==2 and p2==0 and pp1==1 and pp2==2) or (p1==2 and p2==1 and pp1==0 and pp2==2):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p1==2 and p2==3 and pp1==0 and pp2==0) or (p1==1 and p2==1 and pp1==3 and pp2==2):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx           

               if (p1==3 and p2==0 and pp1==1 and pp2==3) or (p1==3 and p2==1 and pp1==0 and pp2==3) or (p1==3 and p2==2 and pp1==0 and pp2==0) or (p1==0 and p2==2 and pp1==2 and pp2==1) or (p1==1 and p2==1 and pp1==2 and pp2==3) or (p1==1 and p2==2 and pp1==2 and pp2==0):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p1==3 and p2==2 and pp1==1 and pp2==1) or (p1==0 and p2==0 and pp1==2 and pp2==3):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx             
              # t2 45
               if (p4==0 and p5==3 and pp4==3 and pp5==1) or (p4==1 and p5==3 and pp4==3 and pp5==0) or (p4==2 and p5==3 and pp4==1 and pp5==1) or (p4==0 and p5==0 and pp4==3 and pp5==2) or (p4==2 and p5==0 and pp4==1 and pp5==2) or (p4==2 and p5==1 and pp4==0 and pp5==2):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p4==2 and p5==3 and pp4==0 and pp5==0) or (p4==1 and p5==1 and pp4==3 and pp5==2):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx           

               if (p4==3 and p5==0 and pp4==1 and pp5==3) or (p4==3 and p5==1 and pp4==0 and pp5==3) or (p4==3 and p5==2 and pp4==0 and pp5==0) or (p4==0 and p5==2 and pp4==2 and pp5==1) or (p4==1 and p5==1 and pp4==2 and pp5==3) or (p4==1 and p5==2 and pp4==2 and pp5==0):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p4==3 and p5==2 and pp4==1 and pp5==1) or (p4==0 and p5==0 and pp4==2 and pp5==3):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx 
              
#Magnetic
            # LINK 12 and LINK 45
            # x
               if p1+pp1==1 and p2+pp2==1 and p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+J2+J1

               if p4+pp4==1 and p5+pp5==1 and p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+J2+J1

            # z
               if p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p1+p2)*J2+(-1)**(p1+p2)*J1
                         
               if p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p4+p5)*J2+(-1)**(p4+p5)*J1
            
            # y
               if p1+pp1==1 and p2+pp2==1 and p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if p1+p2==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                 
                if p1+p2==0 or p1+p2==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
 
               if p5+pp5==1 and p4+pp4==1 and p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                if p5+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                if p5+p4==0 or p5+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1


              
                          
            # LINK 34 and LINK 61
            # z
               if p3<2 and pp3<2 and p4<2 and pp4<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+(-1)**(p3+p4)*J2+(-1)**(p3+p4)*J1 
               if p6<2 and pp6<2 and p1<2 and pp1<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+(-1)**(p6+p1)*J2+(-1)**(p6+p1)*J1
            # x
               if p3+pp3==1 and p4+pp4==1 and p3<2 and pp3<2 and p4<2 and pp4<2 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
               if p6+pp6==1 and p1+pp1==1 and p6<2 and pp6<2 and p1<2 and pp1<2 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1

            # y
               if p3<2 and pp3<2 and p4<2 and pp4<2 and p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                if p3+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                if p3+p4==0 or p3+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
               if p6<2 and pp6<2 and p1<2 and pp1<2 and p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                if p6+p1==1:
                  MP[N1][N2]=MP[N1][N2]-J2+J1
                if p6+p1==0 or p6+p1==2:            
                  MP[N1][N2]=MP[N1][N2]+J2-J1
                         

            # LINK 23 and LINK 56
            # y
               if p2<2 and pp2<2 and p3<2 and pp3<2 and p2+pp2==1 and p3+pp3==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                if p2+p3==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
                if p2+p3==0 or p2+p3==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
               if p5+pp5==1 and p6+pp6==1 and p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p5+p6==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
                if p5+p6==0 or p5+p6==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
            # x
               if p2<2 and pp2<2 and p3<2 and pp3<2 and p3+pp3==1 and p2+pp2==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
               if p6+pp6==1 and p5+pp5==1 and p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
            # z
               if p2<2 and pp2<2 and p3<2 and pp3<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p2+p3)*J2+(-1)**(p2+p3)*J1
               if p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p5+p6)*J2+(-1)**(p5+p6)*J1


 VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
 VAL,VEC=VAL.real,VEC


 idx = VAL.argsort()   
 VAL = VAL[idx]
 VEC = VEC[:,idx]
 print NS
 print NSS
 print VAL[0]
 print VAL[1]
 print VAL[2]
 print VAL[3]
 #ff1.write(str(VAL[0])+'\t')
 #ff1.write(str(VAL[1])+'\t')
 #ff1.write(str(VAL[2])+'\t')
 #ff1.write(str(VAL[3])+'\n')
 V0=VEC[:,0]


 V1=VEC[:,1]
 V2=VEC[:,2]




 for i in range(0,495):
  ff.write(str(VAL[i])+'\t')
 for i in range(0,4096):
  ff2.write(str(V0[i])+'\t')

ff3=open('Holes_plaquette2.txt','w')
NOP=4
NNN=20
t0=-1
tx=-1
ty=-1
tz=-1

for ll in range(0,NNN+1):
 
 MP=zeros([4096,4096],'complex')
 p=ll*1.0/NNN
 #ff1.write(str(p)+'\t')
 t1=p
 t2=1-p
 J1=g1*4*t1**2*1.0/U
 J2=g1*4*t2**2*1.0/U


 t1=1
 t2=0
 NP=0
 NS=0
 print t1
 print t2
 print J1
 print J2
 for p1 in range(0,4):
  for p2 in range(0,4):
   for p3 in range(0,4):
    for p4 in range(0,4):
     for p5 in range(0,4):   
      for p6 in range(0,4):
       NP=0
       if p1==0 or p1==1:
        NP=NP+1
       if p1==3:
        NP=NP+2 
       if p2==0 or p2==1:
        NP=NP+1
       if p2==3:
        NP=NP+2
       if p3==0 or p3==1:
        NP=NP+1
       if p3==3:
        NP=NP+2
       if p4==0 or p4==1:
        NP=NP+1
       if p4==3:
        NP=NP+2
       if p5==0 or p5==1:
        NP=NP+1
       if p5==3:
        NP=NP+2
       if p6==0 or p6==1:
        NP=NP+1
       if p6==3:
        NP=NP+2
       if NP==NOP:
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
        NS=NS+1
        NSS=0
        for pp1 in range(0,4):
         for pp2 in range(0,4):
          for pp3 in range(0,4):
           for pp4 in range(0,4):
            for pp5 in range(0,4):   
             for pp6 in range(0,4):
              NPP=0
              if pp1==0 or pp1==1:
               NPP=NPP+1
              if pp1==3:
               NPP=NPP+2 
              if pp2==0 or pp2==1:
               NPP=NPP+1
              if pp2==3:
               NPP=NPP+2
              if pp3==0 or pp3==1:
               NPP=NPP+1
              if pp3==3:
               NPP=NPP+2
              if pp4==0 or pp4==1:
               NPP=NPP+1
              if pp4==3:
               NPP=NPP+2
              if pp5==0 or pp5==1:
               NPP=NPP+1
              if pp5==3:
               NPP=NPP+2
              if pp6==0 or pp6==1:
               NPP=NPP+1
              if pp6==3:
               NPP=NPP+2
              if NPP==NOP:
               N2=pp1+4*pp2+16*pp3+64*pp4+256*pp5+1024*pp6
               NSS=NSS+1

# Hopping
#Hopping


            # kinetic t1 
             #12
               if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                if p1==pp2 and p2==pp1: 
                 if (p1==0 and p2==3) or (p1==1 and p2==3) or (p1==3 and p2==0) or (p1==3 and p2==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p1==2 and p2==0) or (p1==2 and p2==1) or (p1==0 and p2==2) or (p1==1 and p2==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p1==1 and p2==0 and pp1==3 and pp2==2) or (p1==1 and p2==0 and pp1==2 and pp2==3) or (p1==2 and p2==3 and pp1==1 and pp2==0) or (p1==3 and p2==2 and pp1==1 and pp2==0):
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p1==2 and p2==3 and pp1==0 and pp2==1) or (p1==0 and p2==1 and pp1==3 and pp2==2) or (p1==3 and p2==2 and pp1==0 and pp2==1) or (p1==0 and p2==1 and pp1==2 and pp2==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #23
               if abs(p1-pp1)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if p2==pp3 and p3==pp2:
                 if (p2==0 and p3==3) or (p2==1 and p3==3) or (p2==3 and p3==0) or (p2==3 and p3==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p2==2 and p3==0) or (p2==2 and p3==1) or (p2==0 and p3==2) or (p2==1 and p3==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p2==1 and p3==0 and pp2==3 and pp3==2) or (p2==1 and p3==0 and pp2==2 and pp3==3) or (p2==2 and p3==3 and pp2==1 and pp3==0) or (p2==3 and p3==2 and pp2==1 and pp3==0):
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p2==2 and p3==3 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==2 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==2 and pp3==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #34
               if abs(p1-pp1)+abs(p2-pp2)+abs(p5-pp5)+abs(p6-pp6)==0: 
                if p3==pp4 and p4==pp3:
                 if (p3==0 and p4==3) or (p3==1 and p4==3) or (p3==3 and p4==0) or (p3==3 and p4==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p3==2 and p4==0) or (p3==2 and p4==1) or (p3==0 and p4==2) or (p3==1 and p4==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p3==1 and p4==0 and pp3==3 and pp4==2) or (p3==1 and p4==0 and pp3==2 and pp4==3) or (p3==2 and p4==3 and pp3==1 and pp4==0) or (p3==3 and p4==2 and pp3==1 and pp4==0): 
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p3==2 and p4==3 and pp3==0 and pp4==1) or (p3==0 and p4==1 and pp3==3 and pp4==2) or (p3==3 and p4==2 and pp3==0 and pp4==1) or (p3==0 and p4==1 and pp3==2 and pp4==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #45
               if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p6-pp6)==0:
                if p4==pp5 and p5==pp4:
                 if (p4==0 and p5==3) or (p4==1 and p5==3) or (p4==3 and p5==0) or (p4==3 and p5==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p4==2 and p5==0) or (p4==2 and p5==1) or (p4==0 and p5==2) or (p4==1 and p5==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p4==1 and p5==0 and pp4==3 and pp5==2) or (p4==1 and p5==0 and pp4==2 and pp5==3) or (p4==2 and p5==3 and pp4==1 and pp5==0) or (p4==3 and p5==2 and pp4==1 and pp5==0):
                 
                 MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p4==2 and p5==3 and pp4==0 and pp5==1) or (p4==0 and p5==1 and pp4==3 and pp5==2) or (p4==3 and p5==2 and pp4==0 and pp5==1) or (p4==0 and p5==1 and pp4==2 and pp5==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
             #56
               if  abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p5==pp6 and p6==pp5:
                 if (p5==0 and p6==3) or (p5==1 and p6==3) or (p5==3 and p6==0) or (p5==3 and p6==1):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                 if (p5==2 and p6==0) or (p5==2 and p6==1) or (p5==0 and p6==2) or (p5==1 and p6==2): 
                  MP[N1][N2]=MP[N1][N2]+t1*t0
                if (p5==1 and p6==0 and pp5==3 and pp6==2) or (p5==1 and p6==0 and pp5==2 and pp6==3) or (p5==2 and p6==3 and pp5==1 and pp6==0) or (p5==3 and p6==2 and pp5==1 and pp6==0):
                  MP[N1][N2]=MP[N1][N2]-t1*t0
                if (p5==2 and p6==3 and pp5==0 and pp6==1) or (p5==0 and p6==1 and pp5==3 and pp6==2) or (p5==3 and p6==2 and pp5==0 and pp6==1) or (p5==0 and p6==1 and pp5==2 and pp6==3):       
                  MP[N1][N2]=MP[N1][N2]+t1*t0
             #61
               if abs(p5-pp5)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p6==pp1 and p1==pp6:
                 if (p6==0 and p1==3) or (p6==1 and p1==3) or (p6==3 and p1==0) or (p6==3 and p1==1):
                  MP[N1][N2]=MP[N1][N2]+t1*t0*(-1)**NOP
                 if (p6==2 and p1==0) or (p6==2 and p1==1) or (p6==0 and p1==2) or (p6==1 and p1==2): 
                  MP[N1][N2]=MP[N1][N2]-t1*t0*(-1)**NOP
                if (p6==1 and p1==0 and pp6==3 and pp1==2) or (p6==1 and p1==0 and pp6==2 and pp1==3) or (p6==2 and p1==3 and pp6==1 and pp1==0) or (p6==3 and p1==2 and pp6==1 and pp1==0):
                  MP[N1][N2]=MP[N1][N2]+t1*t0*(-1)**NOP
                if (p6==2 and p1==3 and pp6==0 and pp1==1) or (p6==0 and p1==1 and pp6==3 and pp1==2) or (p6==3 and p1==2 and pp6==0 and pp1==1) or (p6==0 and p1==1 and pp6==2 and pp1==3):        
                  MP[N1][N2]=MP[N1][N2]-t1*t0*(-1)**NOP


            ### t2 y 23
               if (p2==0 and p3==3 and pp2==3 and pp3==1) or (p2==2 and p3==3 and pp2==0 and pp3==0) or (p2==2 and p3==3 and pp2==1 and pp3==1) or (p2==0 and p3==0 and pp2==3 and pp3==2) or (p2==2 and p3==0 and pp2==1 and pp3==2) or (p2==1 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==0 and pp2==1 and  pp3==3) or (p2==0 and p3==2 and pp2==2 and pp3==1):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+1j*t2*ty
               if (p2==1 and p3==3 and pp2==3 and pp3==0) or  (p2==2 and p3==1 and pp2==0 and pp3==2) or (p2==3 and p3==1 and pp2==0 and  pp3==3) or (p2==3 and p3==2 and pp2==1 and  pp3==1) or (p2==3 and p3==2 and pp2==0 and pp3==0) or (p2==0 and p3==0 and pp2==2 and pp3==3) or (p2==1 and p3==1 and pp2==2 and pp3==3) or (p2==1 and p3==2 and pp2==2 and pp3==0):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-1j*t2*ty

            ### t2 y 56
               if (p5==0 and p6==3 and pp5==3 and pp6==1) or (p5==2 and p6==3 and pp5==0 and pp6==0) or (p5==2 and p6==3 and pp5==1 and pp6==1) or (p5==0 and p6==0 and pp5==3 and pp6==2) or (p5==2 and p6==0 and pp5==1 and pp6==2) or (p5==1 and p6==1 and pp5==3 and pp6==2) or (p5==3 and p6==0 and pp5==1 and  pp6==3) or (p5==0 and p6==2 and pp5==2 and pp6==1): 
                if abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+1j*t2*ty
               if (p5==1 and p6==3 and pp5==3 and pp6==0) or  (p5==2 and p6==1 and pp5==0 and pp6==2) or (p5==3 and p6==1 and pp5==0 and  pp6==3) or (p5==3 and p6==2 and pp5==1 and  pp6==1) or (p5==3 and p6==2 and pp5==0 and pp6==0) or (p5==0 and p6==0 and pp5==2 and pp6==3) or (p5==1 and p6==1 and pp5==2 and pp6==3) or (p5==1 and p6==2 and pp5==2 and pp6==0):
                if abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-1j*t2*ty


                           
             # t2 z 61
               if (p6==0 and p1==3 and pp6==3 and pp1==0) or (p6==2 and p1==3 and pp6==0 and pp1==1) or (p6==2 and p1==3 and pp6==1 and pp1==0) or (p6==2 and p1==0 and pp6==0 and pp1==2):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz*(-1)**NOP
               if (p6==1 and p1==3 and pp6==3 and pp1==1) or (p6==1 and p1==0 and pp6==3 and pp1==2) or (p6==0 and p1==1 and pp6==3 and pp1==2) or (p6==2 and p1==1 and pp6==1 and pp1==2): 
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz*(-1)**NOP
               if (p6==3 and p1==0 and pp6==0 and pp1==3) or (p6==0 and p1==1 and pp6==2 and pp1==3) or (p6==0 and p1==2 and pp6==2 and pp1==0) or (p6==1 and p1==0 and pp6==2 and pp1==3):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz*(-1)**NOP
               if (p6==3 and p1==1 and pp6==1 and pp1==3) or (p6==3 and p1==2 and pp6==0 and pp1==1) or (p6==3 and p1==2 and pp6==1 and pp1==0) or (p6==1 and p1==2 and pp6==2 and pp1==1):
                if abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tz*(-1)**NOP



  
             # t2 Z 34 
               if (p3==0 and p4==3 and pp3==3 and pp4==0) or (p3==2 and p4==3 and pp3==0 and pp4==1) or (p3==2 and p4==3 and pp3==1 and pp4==0) or (p3==2 and p4==0 and pp3==0 and pp4==2):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz
               if (p3==1 and p4==3 and pp3==3 and pp4==1) or (p3==1 and p4==0 and pp3==3 and pp4==2) or (p3==0 and p4==1 and pp3==3 and pp4==2) or (p3==2 and p4==1 and pp3==1 and pp4==2):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tz
               if (p3==3 and p4==0 and pp3==0 and pp4==3) or (p3==0 and p4==1 and pp3==2 and pp4==3) or (p3==0 and p4==2 and pp3==2 and pp4==0) or (p3==1 and p4==0 and pp3==2 and pp4==3):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]+t2*tz
               if (p3==3 and p4==1 and pp3==1 and pp4==3) or (p3==3 and p4==2 and pp3==0 and pp4==1) or (p3==3 and p4==2 and pp3==1 and pp4==0) or (p3==1 and p4==2 and pp3==2 and pp4==1):
                if abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]-t2*tz 

             ### t2 X 12
               if (p1==0 and p2==3 and pp1==3 and pp2==1) or (p1==1 and p2==3 and pp1==3 and pp2==0) or (p1==2 and p2==3 and pp1==1 and pp2==1) or (p1==0 and p2==0 and pp1==3 and pp2==2) or (p1==2 and p2==0 and pp1==1 and pp2==2) or (p1==2 and p2==1 and pp1==0 and pp2==2):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p1==2 and p2==3 and pp1==0 and pp2==0) or (p1==1 and p2==1 and pp1==3 and pp2==2):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx           

               if (p1==3 and p2==0 and pp1==1 and pp2==3) or (p1==3 and p2==1 and pp1==0 and pp2==3) or (p1==3 and p2==2 and pp1==0 and pp2==0) or (p1==0 and p2==2 and pp1==2 and pp2==1) or (p1==1 and p2==1 and pp1==2 and pp2==3) or (p1==1 and p2==2 and pp1==2 and pp2==0):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p1==3 and p2==2 and pp1==1 and pp2==1) or (p1==0 and p2==0 and pp1==2 and pp2==3):
                if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx             
              # t2 45
               if (p4==0 and p5==3 and pp4==3 and pp5==1) or (p4==1 and p5==3 and pp4==3 and pp5==0) or (p4==2 and p5==3 and pp4==1 and pp5==1) or (p4==0 and p5==0 and pp4==3 and pp5==2) or (p4==2 and p5==0 and pp4==1 and pp5==2) or (p4==2 and p5==1 and pp4==0 and pp5==2):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p4==2 and p5==3 and pp4==0 and pp5==0) or (p4==1 and p5==1 and pp4==3 and pp5==2):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx           

               if (p4==3 and p5==0 and pp4==1 and pp5==3) or (p4==3 and p5==1 and pp4==0 and pp5==3) or (p4==3 and p5==2 and pp4==0 and pp5==0) or (p4==0 and p5==2 and pp4==2 and pp5==1) or (p4==1 and p5==1 and pp4==2 and pp5==3) or (p4==1 and p5==2 and pp4==2 and pp5==0):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                 MP[N1][N2]=MP[N1][N2]+t2*tx
               if (p4==3 and p5==2 and pp4==1 and pp5==1) or (p4==0 and p5==0 and pp4==2 and pp5==3):
                if abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 MP[N1][N2]=MP[N1][N2]-t2*tx 
              
#Magnetic
            # LINK 12 and LINK 45
            # x
               if p1+pp1==1 and p2+pp2==1 and p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+J2+J1

               if p4+pp4==1 and p5+pp5==1 and p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+J2+J1

            # z
               if p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p1+p2)*J2+(-1)**(p1+p2)*J1
                         
               if p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p4+p5)*J2+(-1)**(p4+p5)*J1
            
            # y
               if p1+pp1==1 and p2+pp2==1 and p1<2 and pp1<2 and p2<2 and pp2<2 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if p1+p2==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                 
                if p1+p2==0 or p1+p2==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
 
               if p5+pp5==1 and p4+pp4==1 and p4<2 and pp4<2 and p5<2 and pp5<2 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                if p5+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                if p5+p4==0 or p5+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1


              
                          
            # LINK 34 and LINK 61
            # z
               if p3<2 and pp3<2 and p4<2 and pp4<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+(-1)**(p3+p4)*J2+(-1)**(p3+p4)*J1 
               if p6<2 and pp6<2 and p1<2 and pp1<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+(-1)**(p6+p1)*J2+(-1)**(p6+p1)*J1
            # x
               if p3+pp3==1 and p4+pp4==1 and p3<2 and pp3<2 and p4<2 and pp4<2 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
               if p6+pp6==1 and p1+pp1==1 and p6<2 and pp6<2 and p1<2 and pp1<2 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1

            # y
               if p3<2 and pp3<2 and p4<2 and pp4<2 and p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                if p3+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                if p3+p4==0 or p3+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
               if p6<2 and pp6<2 and p1<2 and pp1<2 and p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
                if p6+p1==1:
                  MP[N1][N2]=MP[N1][N2]-J2+J1
                if p6+p1==0 or p6+p1==2:            
                  MP[N1][N2]=MP[N1][N2]+J2-J1
                         

            # LINK 23 and LINK 56
            # y
               if p2<2 and pp2<2 and p3<2 and pp3<2 and p2+pp2==1 and p3+pp3==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                if p2+p3==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
                if p2+p3==0 or p2+p3==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
               if p5+pp5==1 and p6+pp6==1 and p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                if p5+p6==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
                if p5+p6==0 or p5+p6==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
            # x
               if p2<2 and pp2<2 and p3<2 and pp3<2 and p3+pp3==1 and p2+pp2==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
               if p6+pp6==1 and p5+pp5==1 and p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
                MP[N1][N2]=MP[N1][N2]-J2+J1
            # z
               if p2<2 and pp2<2 and p3<2 and pp3<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p2+p3)*J2+(-1)**(p2+p3)*J1
               if p5<2 and pp5<2 and p6<2 and pp6<2 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-(-1)**(p5+p6)*J2+(-1)**(p5+p6)*J1


 VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
 VAL,VEC=VAL.real,VEC


 idx = VAL.argsort()   
 VAL = VAL[idx]
 VEC = VEC[:,idx]
 print NS
 print NSS
 print VAL[0]
 print VAL[1]
 print VAL[2]
 print VAL[3]
 #ff1.write(str(VAL[0])+'\t')
 #ff1.write(str(VAL[1])+'\t')
 #ff1.write(str(VAL[2])+'\t')
 #ff1.write(str(VAL[3])+'\n')
 V0=VEC[:,0]
 V1=VEC[:,1]
 V2=VEC[:,2]




 for i in range(0,495):
  ff.write(str(VAL[i])+'\t')
 for i in range(0,4096):
  ff3.write(str(V0[i])+'\t')

