from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp

MP=zeros([16,16],'complex')
N=100
NS=0
NSS=0
NOP=30
t1=1
t2=1
J1=0
J2=0
t0=-1
tx=-1
ty=-1
tz=-1
NP=0
NOP=1
NS=0
print t0
print ty
for p2 in range(0,4):
 for p3 in range(0,4):
  NP=0
  if p2==0 or p2==1:
   NP=NP+1
  if p2==3:
   NP=NP+2 
  if p3==0 or p3==1:
   NP=NP+1
  if p3==3:
   NP=NP+2
  if NP==NOP:
   N1=p2+4*p3
   NS=NS+1
   NSS=0
   for pp2 in range(0,4):
    for pp3 in range(0,4):
     NPP=0
     if pp2==0 or pp2==1:
      NPP=NPP+1
     if pp2==3:
      NPP=NPP+2 
     if pp3==0 or pp3==1:
      NPP=NPP+1
     if pp3==3:
      NPP=NPP+2
     if NPP==NOP:
      N2=pp2+4*pp3
      NSS=NSS+1

      if p2==pp3 and p3==pp2:
       if (p2==0 and p3==3) or (p2==1 and p3==3) or (p2==3 and p3==0) or (p2==3 and p3==1):
                 MP[N1][N2]=MP[N1][N2]-t1*t0
       if (p2==2 and p3==0) or (p2==2 and p3==1) or (p2==0 and p3==2) or (p2==1 and p3==2): 
                 MP[N1][N2]=MP[N1][N2]+t1*t0
      if (p2==1 and p3==0 and pp2==3 and pp3==2) or (p2==1 and p3==0 and pp2==2 and pp3==3) or (p2==2 and p3==3 and pp2==1 and pp3==0) or (p2==3 and p3==2 and pp2==1 and pp3==0): 
                 MP[N1][N2]=MP[N1][N2]-t1*t0
      if (p2==2 and p3==3 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==2 and pp2==0 and pp3==1) or (p2==0 and p3==1 and pp2==2 and pp3==3):
                 MP[N1][N2]=MP[N1][N2]+t1*t0
      if (p2==0 and p3==3 and pp2==3 and pp3==1) or (p2==2 and p3==3 and pp2==0 and pp3==0) or (p2==2 and p3==3 and pp2==1 and pp3==1) or (p2==0 and p3==0 and pp2==3 and pp3==2) or (p2==2 and p3==0 and pp2==1 and pp3==2) or (p2==1 and p3==1 and pp2==3 and pp3==2) or (p2==3 and p3==0 and pp2==1 and  pp3==3) or (p2==0 and p3==2 and pp2==2 and pp3==1):
                 MP[N1][N2]=MP[N1][N2]+1j*t2*ty
      if (p2==1 and p3==3 and pp2==3 and pp3==0) or  (p2==2 and p3==1 and pp2==0 and pp3==2) or (p2==3 and p3==1 and pp2==0 and  pp3==3) or (p2==3 and p3==2 and pp2==1 and  pp3==1) or (p2==3 and p3==2 and pp2==0 and pp3==0) or (p2==0 and p3==0 and pp2==2 and pp3==3) or (p2==1 and p3==1 and pp2==2 and pp3==3) or (p2==1 and p3==2 and pp2==2 and pp3==0):
                 MP[N1][N2]=MP[N1][N2]-1j*t2*ty
VAL,VEC=LA.eig(MP)   ## diagonalisation Val valeur propre, Vec vecteur propre
VAL,VEC=VAL,VEC


idx = VAL.argsort()   
VAL = VAL[idx]
VEC = VEC[:,idx]

print NS
print NSS

print VAL
print VEC[:,0]

