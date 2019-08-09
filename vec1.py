from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VV=loadtxt("Holes_plaquette.txt", dtype=complex)
C12=0
C16=0
NOP=4
NNN=20
for ln in range(0,20):
 C12=0
 C16=0

 NOO=ln*4096
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
        if p1==0 and p2==0:
         C12=C12+VV[N1]
        if p1==0 and p6==0:
         C16=C16+VV[N1]
 if atan(C12.imag/C12.real)/pi-atan(C16.imag/C16.real)/pi>0:
  print atan(C12.imag/C12.real)/pi-atan(C16.imag/C16.real)/pi
 if atan(C12.imag/C12.real)/pi-atan(C16.imag/C16.real)/pi<0:
  print 1+atan(C12.imag/C12.real)/pi-atan(C16.imag/C16.real)/pi
