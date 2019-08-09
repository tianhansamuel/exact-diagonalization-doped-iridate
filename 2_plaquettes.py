from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp




NS=0
NOP=30
ff=open('matrix_plaquette_2.txt','w')
ff1=open('ground_state.txt','w')
#ff.write('J1'+'\t')
#ff.write('J2'+'\t')
#ff.write('X'+'\t'+'\t')
#ff.write('Y'+'\t'+'\t')
#ff.write('Z'+'\t'+'\t'+'\n')
J1=0.1
J2=0.9
 

MP=zeros([1024,1024])
print J1
print J2
for N1 in range(0,1024):
  p1=N1-N1/2*2
  NR=p1
  p2=(N1-N1/4*4-p1)/2
  NR=NR+2*p2 
  p3=(N1-N1/8*8-NR)/4
  NR=NR+4*p3
  p4=(N1-N1/16*16-NR)/8
  NR=NR+8*p4
  p5=(N1-N1/32*32-NR)/16
  NR=NR+16*p5
  p6=(N1-N1/64*64-NR)/32
  NR=NR+32*p6
  p7=(N1-N1/128*128-NR)/64
  NR=NR+64*p7
  p8=(N1-N1/256*256-NR)/128
  NR=NR+128*p8
  p9=(N1-N1/512*512-NR)/256
  NR=NR+256*p9
  p10=(N1-NR)/512
  print N1
  for N2 in range(0,1024):
    pp1=N2%2
    NRR=pp1
    pp2=(N2-N2/4*4-pp1)/2
    NRR=NRR+2*pp2 
    pp3=(N2-N2/8*8-NRR)/4
    NRR=NRR+4*pp3
    pp4=(N2-N2/16*16-NRR)/8
    NRR=NRR+8*pp4
    pp5=(N2-N2/32*32-NRR)/16
    NRR=NRR+16*pp5
    pp6=(N2-N2/64*64-NRR)/32
    NRR=NRR+32*pp6
    pp7=(N2-N2/128*128-NRR)/64
    NRR=NRR+64*pp7
    pp8=(N2-N2/256*256-NRR)/128
    NRR=NRR+128*pp8
    pp9=(N2-N2/512*512-NRR)/256
    NRR=NRR+256*pp9
    pp10=(N2-NRR)/512
    # LINK 12 and LINK 45 and LINK 37 and LINK 9 10 and LINK 11 12
    # x
    if p1+pp1==1 and p2+pp2==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+J2+J1

    if p4+pp4==1 and p5+pp5==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+J2+J1

    if p3+pp3==1 and p7+pp7==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+J2+J1

    if p9+pp9==1 and p10+pp10==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)==0:
       MP[N1][N2]=MP[N1][N2]+J2+J1



     # z
    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p1+p2)%2)*J2+(-1)**((p1+p2)%2)*J1
                         
    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p4+p5)%2)*J2+(-1)**((p4+p5)%2)*J1

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p3+p7)%2)*J2+(-1)**((p3+p7)%2)*J1
                         
    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p9+p10)%2)*J2+(-1)**((p9+p10)%2)*J1

                         
    # y
    if p1+pp1==1 and p2+pp2==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p1+p2==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
                 
       if p1+p2==0 or p1+p2==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1
 
    if p5+pp5==1 and p4+pp4==1 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p5+p4==1:
         MP[N1][N2]=MP[N1][N2]-J2+J1
       if p5+p4==0 or p5+p4==2:            
         MP[N1][N2]=MP[N1][N2]+J2-J1

    if p3+pp3==1 and p7+pp7==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p3+p7==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
                 
       if p3+p7==0 or p3+p7==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1

    if p9+pp9==1 and p10+pp10==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p1-pp1)+abs(p2-pp2)==0:
       if p9+p10==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
                 
       if p9+p10==0 or p9+p10==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1


            
     # LINK 34 and LINK 61
     # z
    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+(-1)**((p3+p4)%2)*J2+(-1)**((p3+p4)%2)*J1 

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+(-1)**((p6+p1)%2)*J2+(-1)**((p6+p1)%2)*J1

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]+(-1)**((p8+p9)%2)*J2+(-1)**((p8+p9)%2)*J1 



    # x
    if p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1

    if p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1

    if p8+pp8==1 and p9+pp9==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)+abs(p7-pp7)+abs(p1-pp1)+abs(p6-pp6)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1



    # y
    if p3+pp3==1 and p4+pp4==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p3+p4==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
       if p3+p4==0 or p3+p4==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1

    if p6+pp6==1 and p1+pp1==1 and abs(p5-pp5)+abs(p3-pp3)+abs(p2-pp2)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p6+p1==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
       if p6+p1==0 or p6+p1==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1

    if p8+pp8==1 and p9+pp9==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)+abs(p7-pp7)+abs(p3-pp3)+abs(p4-pp4)+abs(p10-pp10)==0:
       if p8+p9==1:
          MP[N1][N2]=MP[N1][N2]-J2+J1
       if p8+p9==0 or p8+p9==2:            
          MP[N1][N2]=MP[N1][N2]+J2-J1



     # LINK 23 and LINK 56 and LINK 78 and LINK 4 10 and LINK 12 13
     # y
    if p2+pp2==1 and p3+pp3==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p2+p3==1:
          MP[N1][N2]=MP[N1][N2]+J2+J1
       if p2+p3==0 or p2+p3==2:            
          MP[N1][N2]=MP[N1][N2]-J2-J1

    if p5+pp5==1 and p6+pp6==1 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p5+p6==1:
          MP[N1][N2]=MP[N1][N2]+J2+J1
       if p5+p6==0 or p5+p6==2:            
          MP[N1][N2]=MP[N1][N2]-J2-J1

    if p7+pp7==1 and p8+pp8==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)+abs(p2-pp2)+abs(p3-pp3)+abs(p9-pp9)+abs(p10-pp10)==0:
       if p7+p8==1:
          MP[N1][N2]=MP[N1][N2]+J2+J1
       if p7+p8==0 or p7+p8==2:            
          MP[N1][N2]=MP[N1][N2]-J2-J1

    if p4+pp4==1 and p10+pp10==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p2-pp2)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p3-pp3)==0:
       if p4+p10==1:
          MP[N1][N2]=MP[N1][N2]+J2+J1
       if p4+p10==0 or p4+p10==2:            
          MP[N1][N2]=MP[N1][N2]-J2-J1


    # x
    if p3+pp3==1 and p2+pp2==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1

    if p6+pp6==1 and p5+pp5==1 and abs(p2-pp2)+abs(p1-pp1)+abs(p3-pp3)+abs(p4-pp4)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1

    if p7+pp7==1 and p8+pp8==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p4-pp4)+abs(p2-pp2)+abs(p3-pp3)+abs(p9-pp9)+abs(p10-pp10)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1

    if p4+pp4==1 and p10+pp10==1 and abs(p5-pp5)+abs(p1-pp1)+abs(p6-pp6)+abs(p2-pp2)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p3-pp3)==0:
       MP[N1][N2]=MP[N1][N2]-J2+J1




     # z
    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
        MP[N1][N2]=MP[N1][N2]-(-1)**((p2+p3)%2)*J2+(-1)**((p2+p3)%2)*J1

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
        MP[N1][N2]=MP[N1][N2]-(-1)**((p5+p6)%2)*J2+(-1)**((p5+p6)%2)*J1

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
        MP[N1][N2]=MP[N1][N2]-(-1)**((p7+p8)%2)*J2+(-1)**((p7+p8)%2)*J1

    if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0:
        MP[N1][N2]=MP[N1][N2]-(-1)**((p4+p10)%2)*J2+(-1)**((p4+p10)%2)*J1


VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
VAL,VEC=VAL.real,VEC.real


idx = VAL.argsort()   
VAL = VAL[idx]
VEC = VEC[:,idx]

VV=VEC[:,0]
VV1=VEC[:,1]
VV2=VEC[:,2]
VV=VV/LA.norm(VV)
VV1=VV1/LA.norm(VV)
VV2=VV2/LA.norm(VV)
print VAL[0]
print VAL[1]
print VAL[2]

M_ENT=zeros([4,4])


for p1 in range(0,2):  
  for p2 in range(0,2):
   for p3 in range(0,2):
    for p4 in range(0,2):
     for p5 in range(0,2):
      for p6 in range(0,2):
       for p7 in range(0,2):
        for p8 in range(0,2):
         for p9 in range(0,2):
          for p10 in range(0,2):
           N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6+64*p7+128*p8+256*p9+512*p10
           C1=p9+2*p10
           for pp1 in range(0,2):
            for pp2 in range(0,2):
             N2=p1+2*p2+4*p3+8*p4+16*p5+32*p6+64*p7+128*p8+256*pp9+512*pp10
             C2=pp9+2*pp10
             M_ENT[C1][C2]=M_ENT[C1][C2]+VV[N1]*VV[N2]
VAL_ENT,VEC_ENT=LA.eig(M_ENT)
iidx = VAL_ENT.argsort()   
VAL_ENT = VAL_ENT[iidx]
VEC_ENT = VEC_ENT[:,iidx]

print 'X'
print VAL_ENT
print VEC_ENT[:,3]
sgn=VEC_ENT[0,3]/abs(VEC_ENT[0,3])
VEC_ENT[:,3]=sgn*VEC_ENT[:,3]




