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

for p in range(0,N):
 J1=p*1.0/N
 J2=1-J1
 J3=sqrt(J1*J2)
 ff.write(str(J1)+'\t')
 ff.write(str(J2)+'\t')


 MP=zeros([64,64],'complex')
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
            #DMX 12          
	     if pp1+pp2==1 and abs(p1-pp1)+abs(p1-p2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-1J*J3
          
	     if pp1+pp2==1 and abs(p2-pp2)+abs(p1-p2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+1J*J3
             if p1+p2==1 and abs(p1-pp1)+abs(pp1-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                MP[N1][N2]=MP[N1][N2]+1J*J3
             if p1+p2==1 and abs(p2-pp2)+abs(pp1-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0: 
                MP[N1][N2]=MP[N1][N2]-1J*J3
            #DMX 45          
	     if pp4+pp5==1 and abs(p4-pp4)+abs(p4-p5)+abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]-1J*J3
          
	     if pp4+pp5==1 and abs(p5-pp5)+abs(p4-p5)+abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                MP[N1][N2]=MP[N1][N2]+1J*J3
             if p4+p5==1 and abs(p4-pp4)+abs(pp4-pp5)+abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                MP[N1][N2]=MP[N1][N2]+1J*J3
             if p4+p5==1 and abs(p5-pp5)+abs(pp4-pp5)+abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0: 
                MP[N1][N2]=MP[N1][N2]-1J*J3
              
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
            # DMZ 34
             if p3+pp3==1 and p4+pp4==1 and p3+p4==1 and abs(p1-pp1)+abs(p5-pp5)+abs(p6-pp6)+abs(p2-pp2)==0:
                if p3==0: MP[N1][N2]=MP[N1][N2]-2J*J3
                if p3==1: MP[N1][N2]=MP[N1][N2]+2J*J3

            # DMZ 61
             if p6+pp6==1 and p1+pp1==1 and p6+p1==1 and abs(p3-pp3)+abs(p5-pp5)+abs(p4-pp4)+abs(p2-pp2)==0:
                if p6==0: MP[N1][N2]=MP[N1][N2]-2J*J3
                if p6==1: MP[N1][N2]=MP[N1][N2]+2J*J3

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
            # DMY 23
             if pp2+pp3==1 and abs(p2-p3)+abs(p1-pp1)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if pp2==0:  MP[N1][N2]=MP[N1][N2]+J3
                if pp2==1:  MP[N1][N2]=MP[N1][N2]-J3 
             if p2+p3==1 and abs(pp2-pp3)+abs(p1-pp1)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if p2==0: MP[N1][N2]=MP[N1][N2]+J3
                if p2==1: MP[N1][N2]=MP[N1][N2]-J3
            # DMY 56
             if pp5+pp6==1 and abs(p5-p6)+abs(p1-pp1)+abs(p4-pp4)+abs(p3-pp3)+abs(p2-pp2)==0:
                if pp5==0:  MP[N1][N2]=MP[N1][N2]+J3
                if pp5==1:  MP[N1][N2]=MP[N1][N2]-J3 
             if p5+p6==1 and abs(pp5-pp6)+abs(p1-pp1)+abs(p4-pp4)+abs(p3-pp3)+abs(p2-pp2)==0:
                if p5==0: MP[N1][N2]=MP[N1][N2]+J3
                if p5==1: MP[N1][N2]=MP[N1][N2]-J3


 VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
 VAL=VAL.real


 idx = VAL.argsort()   
 VAL = VAL[idx]
 VEC = VEC[:,idx]

 VV=VEC[:,0]
 VV=VV/LA.norm(VV)

 M_ENT1=zeros([4,4],'complex')
 for p1 in range(0,2):  
  for p4 in range(0,2):
   for p5 in range(0,2):
    for p6 in range(0,2):
     for p2 in range(0,2):
      for p3 in range(0,2):
       N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6
       C1=p1+2*p2

       for pp1 in range(0,2):
        for pp2 in range(0,2):
         N2=pp1+2*pp2+4*p3+8*p4+16*p5+32*p6
         C2=pp1+2*pp2
         M_ENT1[C1][C2]=M_ENT1[C1][C2]+VV[N1].conjugate()*VV[N2]
 VAL_ENT1,VEC_ENT1=LA.eig(M_ENT1)
 iidx = VAL_ENT1.argsort()   
 VAL_ENT1 = VAL_ENT1[iidx].real
 VEC_ENT1 = VEC_ENT1[:,iidx].real
 print 'X'
 print VAL_ENT1
 print VEC_ENT1[:,3]
 for i in range(0,4):
  ff.write(str(VAL_ENT1[i])+'\t')
 for i in range(0,4):
  ff.write(str(VEC_ENT1[i,3])+'\t')


 M_ENT1=zeros([4,4],'complex')
 for p1 in range(0,2):  
  for p4 in range(0,2):
   for p5 in range(0,2):
    for p6 in range(0,2):
     for p2 in range(0,2):
      for p3 in range(0,2):
       N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6
       C1=p2+2*p3

       for pp2 in range(0,2):
        for pp3 in range(0,2):
         N2=p1+2*pp2+4*pp3+8*p4+16*p5+32*p6
         C2=pp2+2*pp3
         M_ENT1[C1][C2]=M_ENT1[C1][C2]+VV[N1].conjugate()*VV[N2]
 VAL_ENT1,VEC_ENT1=LA.eig(M_ENT1)
 iidx = VAL_ENT1.argsort()   
 VAL_ENT1 = VAL_ENT1[iidx].real
 VEC_ENT1 = VEC_ENT1[:,iidx].real

 print 'Y'
 print VAL_ENT1
 print VEC_ENT1[:,3]
 sgn=VEC_ENT1[0,3]/abs(VEC_ENT1[0,3])
 VEC_ENT1[:,3]=sgn*VEC_ENT1[:,3]
 for i in range(0,4):
  ff.write(str(VAL_ENT1[i])+'\t')
 for i in range(0,4):
  ff.write(str(VEC_ENT1[i,3])+'\t')


 M_ENT1=zeros([4,4],'complex')
 for p1 in range(0,2):  
  for p2 in range(0,2):
   for p5 in range(0,2):
    for p6 in range(0,2):
     for p3 in range(0,2):
      for p4 in range(0,2):
       N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6
       C1=p3+2*p4

       for pp3 in range(0,2):
        for pp4 in range(0,2):
         N2=p1+2*p2+4*pp3+8*pp4+16*p5+32*p6
         C2=pp3+2*pp4
         M_ENT1[C1][C2]=M_ENT1[C1][C2]+VV[N1].conjugate()*VV[N2]
 VAL_ENT1,VEC_ENT1=LA.eig(M_ENT1)
 iidx = VAL_ENT1.argsort()   
 VAL_ENT1 = VAL_ENT1[iidx].real
 VEC_ENT1 = VEC_ENT1[:,iidx].real
 print 'Z'
 print VAL_ENT1
 print VEC_ENT1[:,3]
 sgn=VEC_ENT1[1,3]/abs(VEC_ENT1[1,3])
 VEC_ENT1[:,3]=sgn*VEC_ENT1[:,3]
 for i in range(0,4):
  ff.write(str(VAL_ENT1[i])+'\t')
 for i in range(0,4):
  ff.write(str(VEC_ENT1[i,3])+'\t')

 ff.write(str(VAL[0])+'\t')
 ff.write(str(VAL[1])+'\t')
 ff.write(str(VAL[2])+'\t')
 ff.write(str(VAL[3])+'\t')
 ff.write(str(VAL[4])+'\n')
# print VAL
