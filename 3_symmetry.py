from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VV=loadtxt("ground_state.txt", dtype=complex)

M_ENT=zeros([4,4],'complex')
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
           for p11 in range(0,2):
            for p12 in range(0,2):
             for p13 in range(0,2):
              N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6+64*p7+128*p8+256*p9+512*p10+1024*p11+2048*p12+4096*p13
              C1=p1+2*p2
              for pp1 in range(0,2):
               for pp2 in range(0,2):
                N2=pp1+2*pp2+4*p3+8*p4+16*p5+32*p6+64*p7+128*p8+256*p9+512*p10+1024*p11+2048*p12+4096*p13
                C2=pp1+2*pp2
                M_ENT[C1][C2]=M_ENT[C1][C2]+VV[N1]*VV[N2]
VAL_ENT,VEC_ENT=LA.eig(M_ENT)
iidx = VAL_ENT.argsort()   
VAL_ENT = VAL_ENT[iidx]
VEC_ENT = VEC_ENT[:,iidx]

print 'y'
print VAL_ENT
print VEC_ENT[:,3]

M_ENT1=zeros([4,4],'complex')
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
           for p11 in range(0,2):
            for p12 in range(0,2):
             for p13 in range(0,2):
              N1=p1+2*p2+4*p3+8*p4+16*p5+32*p6+64*p7+128*p8+256*p9+512*p10+1024*p11+2048*p12+4096*p13
              C1=p4+2*p5
              for pp4 in range(0,2):
               for pp5 in range(0,2):
                N2=p1+2*p2+4*p3+8*pp4+16*pp5+32*p6+64*p7+128*p8+256*p9+512*p10+1024*p11+2048*p12+4096*p13
                C2=pp4+2*pp5
                M_ENT1[C1][C2]=M_ENT1[C1][C2]+VV[N1]*VV[N2]
VAL_ENT1,VEC_ENT1=LA.eig(M_ENT1)
iidx = VAL_ENT1.argsort()   
VAL_ENT1 = VAL_ENT1[iidx]
VEC_ENT1 = VEC_ENT1[:,iidx]

print 'y'
print VAL_ENT1
print VEC_ENT1[:,3]
