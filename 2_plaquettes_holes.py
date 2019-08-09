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
 

MP=zeros([125970,125970],'complex64')
print J1
print J2
for N1 in range(0,1048576):
  p1=N1-N1/4*4
  NR=p1
  p2=(N1-N1/16*16-p1)/4
  NR=NR+4*p2 
  p3=(N1-N1/64*64-NR)/16
  NR=NR+16*p3
  p4=(N1-N1/256*256-NR)/64
  NR=NR+64*p4
  p5=(N1-N1/1024*1024-NR)/256
  NR=NR+256*p5
  p6=(N1-N1/4096*4096-NR)/1024
  NR=NR+1024*p6
  p7=(N1-N1/16384*16384-NR)/4096
  NR=NR+4096*p7
  p8=(N1-N1/65576*65576-NR)/16384
  NR=NR+16384*p8
  p9=(N1-N1/262304*262304-NR)/65576
  NR=NR+65576*p9
  p10=(N1-NR)
  print N1
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
   for N2 in range(0,1048576):
    pp1=N2%4
    NRR=pp1
    pp2=(N2-N2/16*16-pp1)/4
    NRR=NRR+4*pp2 
    pp3=(N2-N2/64*64-NRR)/16
    NRR=NRR+16*pp3
    pp4=(N2-N2/256*256-NRR)/64
    NRR=NRR+64*pp4
    pp5=(N2-N2/1024*1024-NRR)/256
    NRR=NRR+256*pp5
    pp6=(N2-N2/4096*4096-NRR)/1024
    NRR=NRR+1024*pp6
    pp7=(N2-N2/16384*16384-NRR)/4096
    NRR=NRR+4096*pp7
    pp8=(N2-N2/65576*65576-NRR)/16384
    NRR=NRR+16384*pp8
    pp9=(N2-N2/262304*262304-NRR)/65576
    NRR=NRR+65576*pp9
    pp10=(N2-NRR)
    NP=0
    if pp1==0 or pp1==1:
     NP=NP+1
    if pp1==3:
     NP=NP+2 
    if pp2==0 or pp2==1:
     NP=NP+1
    if pp2==3:
     NP=NP+2
    if pp3==0 or pp3==1:
     NP=NP+1
    if pp3==3:
     NP=NP+2
    if pp4==0 or pp4==1:
     NP=NP+1
    if pp4==3:
     NP=NP+2
    if pp5==0 or pp5==1:
     NP=NP+1
    if pp5==3:
     NP=NP+2
    if pp6==0 or pp6==1:
     NP=NP+1
    if pp6==3:
     NP=NP+2
    if NP==NOP:
    # LINK 12 and LINK 45 and LINK 37 and LINK 9 10 and LINK 11 12
    # x
     if p1+pp1==1 and p2+pp2==1 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p1<2 and pp1<2 and p2<2 and pp2<2:
       MP[N1][N2]=MP[N1][N2]+J2+J1

     if p4+pp4==1 and p5+pp5==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p4<2 and pp4<2 and p5<2 and pp2<2:
       MP[N1][N2]=MP[N1][N2]+J2+J1

     if p3+pp3==1 and p7+pp7==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p3<2 and pp3<2 and p7<2 and pp7<2:
       MP[N1][N2]=MP[N1][N2]+J2+J1

     if p9+pp9==1 and p10+pp10==1 and abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)==0 and p9<2 and pp9<2 and p10<2 and pp10<2:
       MP[N1][N2]=MP[N1][N2]+J2+J1



     # z
     if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p1<2 and pp1<2 and p2<2 and pp2<2:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p1+p2)%2)*J2+(-1)**((p1+p2)%2)*J1
                         
     if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p4<2 and pp4<2 and p5<2 and pp5<2:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p4+p5)%2)*J2+(-1)**((p4+p5)%2)*J1

     if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p3<2 and pp7<2 and p3<2 and pp7<2:
       MP[N1][N2]=MP[N1][N2]-(-1)**((p3+p7)%2)*J2+(-1)**((p3+p7)%2)*J1
                         
     if abs(p1-pp1)+abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)+abs(p7-pp7)+abs(p8-pp8)+abs(p9-pp9)+abs(p10-pp10)==0 and p1<2 and pp1<2 and p2<2 and pp2<2:
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
