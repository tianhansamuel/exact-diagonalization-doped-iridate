from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VV=loadtxt('Holes_plaquette.txt',dtype=complex)


NOP=4
NNN=4
for ln in range(0,NNN):
 NOO=ln*4096
 M_ENT12=zeros([16,16],'complex')

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
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6+NOO
        C1=p1+4*p2
        for pp1 in range(0,4):
         for pp2 in range(0,4):
             NPP=0
             if pp1==0 or pp1==1:
              NPP=NPP+1
             if pp1==3:
              NPP=NPP+2 
             if pp2==0 or pp2==1:
              NPP=NPP+1
             if pp2==3:
              NPP=NPP+2
             if p3==0 or p3==1:
              NPP=NPP+1
             if p3==3:
              NPP=NPP+2
             if p4==0 or p4==1:
              NPP=NPP+1
             if p4==3:
              NPP=NPP+2
             if p5==0 or p5==1:
              NPP=NPP+1
             if p5==3:
              NPP=NPP+2
             if p6==0 or p6==1:
              NPP=NPP+1
             if p6==3:
              NPP=NPP+2
             if NPP==NOP:
              N2=pp1+4*pp2+16*p3+64*p4+256*p5+1024*p6+NOO
              C2=pp1+4*pp2
              M_ENT12[C1][C2]=M_ENT12[C1][C2]+VV[N1].conjugate()*VV[N2]

 VAL_ENT,VEC_ENT=LA.eig(M_ENT12)
 VAL_ENT=VAL_ENT.real
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]
 G12=0
 for j in range(0,16):
  G12=G12+VEC_ENT[10,j]*VAL_ENT[j]
 print G12
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
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6+NOO
        C1=p1+4*p6
        for pp1 in range(0,4):
         for pp6 in range(0,4):
             NPP=0
             if pp1==0 or pp1==1:
              NPP=NPP+1
             if pp1==3:
              NPP=NPP+2 
             if p2==0 or p2==1:
              NPP=NPP+1
             if p2==3:
              NPP=NPP+2
             if p3==0 or p3==1:
              NPP=NPP+1
             if p3==3:
              NPP=NPP+2
             if p4==0 or p4==1:
              NPP=NPP+1
             if p4==3:
              NPP=NPP+2
             if p5==0 or p5==1:
              NPP=NPP+1
             if p5==3:
              NPP=NPP+2
             if pp6==0 or pp6==1:
              NPP=NPP+1
             if pp6==3:
              NPP=NPP+2
             if NPP==NOP:
              N2=pp1+4*pp2+16*p3+64*p4+256*p5+1024*p6+NOO
              C2=pp1+4*pp2
              M_ENT12[C1][C2]=M_ENT12[C1][C2]+VV[N1].conjugate()*VV[N2]

 VAL_ENT,VEC_ENT=LA.eig(M_ENT12)
 VAL_ENT=VAL_ENT.real
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]
 G16=0
 for j in range(0,16):
  G16=G16+VEC_ENT[10,j]*VAL_ENT[j]
 print G16


