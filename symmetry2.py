from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VVD=loadtxt("Holes_plaquette1.txt", dtype=complex)
VVH=loadtxt("Holes_plaquette0.txt", dtype=complex)
C12=0
C16=0
NOP=4
NOP0=6
NNN=9


for ll in range(0,NNN+1):
 print ll*1.0/NNN
 VV=[0]*4096
 VV1=[0]*4096
 for i in range(0,4096):
  VV[i]=VVD[ll*4096+i]
 M_ENT1=zeros([16,16],'complex')
 for p1 in range(0,4):  
   for p2 in range(0,4):
    for p3 in range(0,4):
     for p4 in range(0,4):
      for p5 in range(0,4):
       for p6 in range(0,4):
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
        C1=p1+4*p2
        for pp1 in range(0,4):
         for pp2 in range(0,4):
          N2=pp1+4*pp2+16*p3+64*p4+256*p5+1024*p6
          C2=pp1+4*pp2
          M_ENT1[C1][C2]=M_ENT1[C1][C2]+VV[N1].conjugate()*VV[N2]+VV1[N1].conjugate()*VV1[N2]
 VAL_ENT,VEC_ENT=LA.eig(M_ENT1)
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]
 C12=0
 for i in range(0,16):
  C12=C12+VAL_ENT[i]*VEC_ENT[10,i]
 print C12


 M_ENT=zeros([16,16],'complex')


 for p1 in range(0,4):  
  for p2 in range(0,4):
   for p3 in range(0,4):
    for p4 in range(0,4):
     for p5 in range(0,4):
      for p6 in range(0,4):
       N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
       C1=p2+4*p3
       for pp2 in range(0,4):
        for pp3 in range(0,4):
         N2=p1+4*pp2+16*pp3+64*p4+256*p5+1024*p6
         C2=pp2+4*pp3
         M_ENT[C1][C2]=M_ENT[C1][C2]+VV[N1].conjugate()*VV[N2]+VV1[N1].conjugate()*VV1[N2]
 VAL_ENT,VEC_ENT=LA.eig(M_ENT)
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]

 C23=0
 for i in range(0,16):
  C23=C23+VAL_ENT[i]*VEC_ENT[10,i]
 print C23



 M_ENT=zeros([16,16],'complex')


 for p1 in range(0,4):  
  for p2 in range(0,4):
   for p3 in range(0,4):
    for p4 in range(0,4):
     for p5 in range(0,4):
      for p6 in range(0,4):
       N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
       C1=p3+4*p4
       for pp3 in range(0,4):
        for pp4 in range(0,4):
         N2=p1+4*p2+16*pp3+64*pp4+256*p5+1024*p6
         C2=pp3+4*pp4
         M_ENT[C1][C2]=M_ENT[C1][C2]+VV[N1].conjugate()*VV[N2]+VV1[N1].conjugate()*VV1[N2]
 VAL_ENT,VEC_ENT=LA.eig(M_ENT)
 iidx = VAL_ENT.argsort()   
 VAL_ENT = VAL_ENT[iidx]
 VEC_ENT = VEC_ENT[:,iidx]

 C34=0
 for i in range(0,16):
  C34=C34+VAL_ENT[i]*VEC_ENT[10,i]
 print C34
 print '*******************************************'


