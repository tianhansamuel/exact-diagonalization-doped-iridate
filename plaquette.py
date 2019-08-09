from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp



MP=zeros([64,64])
PSN=[0]*64
N=100
NS=0
NOP=30
ff=open('matrix_plaquette.dat','w')

#ff.write('J1'+'\t')
#ff.write('J2'+'\t')
#ff.write('X'+'\t'+'\t')
#ff.write('Y'+'\t'+'\t')
#ff.write('Z'+'\t'+'\t'+'\n')
for p in range(0,N+1):
 J1=p*1.0/N
 J2=1-J1
 ff.write(str(J1)+'\t')
 #ff.write(str(J2)+'\t')
 MP=zeros([64,64])
 print J1
 for p1 in range(0,2): 
  for p2 in range(0,2):
   for p3 in range(0,2):
    for p4 in range(0,2):
     for p5 in range(0,2):
      for p6 in range(0,2):
       N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6
       for pp1 in range(0,2):
        for pp2 in range(0,2):
         for pp3 in range(0,2):
          for pp4 in range(0,2):
           for pp5 in range(0,2):
            for pp6 in range(0,2):
             N2=pp1+2*pp2+4*pp3+8*pp4+16*pp5+32*pp6
            # LINK 12 and LINK 45
            # x
             if p1+pp1==1 and p2+pp2==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]+J2+J1

             if p4+pp4==1 and p5+pp5==1 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]+J2+J1

            # z
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]-(-1)**(p1+p2)*J2+(-1)**(p1+p2)*J1
                         
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]-(-1)**(p4+p5)*J2+(-1)**(p4+p5)*J1
            
            # y
             if p1+pp1==1 and p2+pp2==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               if p1+p2==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
                 
               if p1+p2==0 or p1+p2==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
 
             if p5+pp5==1 and p4+pp4==1 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
               if p5+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
               if p5+p4==0 or p5+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
            
            # LINK 34 and LINK 61
            # z
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]+(-1)**(p3+p4)*J2+(-1)**(p3+p4)*J1 
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]+(-1)**(p6+p1)*J2+(-1)**(p6+p1)*J1
            # x
             if p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]-J2+J1
             if p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
               MP[N1][N2]=MP[N1][N2]-J2+J1

            # y
             if p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
               if p3+p4==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
               if p3+p4==0 or p3+p4==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1
             if p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)==0:
               if p6+p1==1:
                 MP[N1][N2]=MP[N1][N2]-J2+J1
               if p6+p1==0 or p6+p1==2:            
                 MP[N1][N2]=MP[N1][N2]+J2-J1

            # LINK 23 and LINK 56
            # y
             if p2+pp2==1 and p3+pp3==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
               if p2+p3==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
               if p2+p3==0 or p2+p3==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
             if p5+pp5==1 and p6+pp6==1 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
               if p5+p6==1:
                 MP[N1][N2]=MP[N1][N2]+J2+J1
               if p5+p6==0 or p5+p6==2:            
                 MP[N1][N2]=MP[N1][N2]-J2-J1
            # x
             if p3+pp3==1 and p2+pp2==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)==0:
               MP[N1][N2]=MP[N1][N2]-J2+J1
             if p6+pp6==1 and p5+pp5==1 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)==0:
               MP[N1][N2]=MP[N1][N2]-J2+J1
            # z
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]-(-1)**(p2+p3)*J2+(-1)**(p2+p3)*J1
             if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
               MP[N1][N2]=MP[N1][N2]-(-1)**(p5+p6)*J2+(-1)**(p5+p6)*J1

 VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
 VAL,VEC=VAL.real,VEC.real

 iidx = VAL.argsort()
 VAL = VAL[iidx]
 VEC = VEC[:,iidx]


 VV=VEC[:,0]
 VV1=VEC[:,1]
 VV2=VEC[:,2]
 VV=VV/LA.norm(VV)
 VV1=VV1/LA.norm(VV)
 VV2=VV2/LA.norm(VV)

 M_ENT=zeros([4,4])
 for p1 in range(0,2):  
  for p2 in range(0,2):
   for p3 in range(0,2):
    for p4 in range(0,2):
     for p5 in range(0,2):
      for p6 in range(0,2):
       N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6
       C1=p1+2*p2
       for pp1 in range(0,2):
        for pp2 in range(0,2):
         N2=pp1+2*pp2+4*p3+8*p4+16*p5+32*p6
         C2=pp1+2*pp2
         M_ENT[C1][C2]=M_ENT[C1][C2]+VV[N1]*VV[N2]
 VAL_ENT,VEC_ENT=LA.eig(M_ENT)
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]


 for i in range(0,4):
  ff.write(str(VAL_ENT[i])+'\t')
 ff.write('\n') 











