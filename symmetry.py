from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VV=loadtxt("Holes_plaquette1.txt", dtype=complex)
VV0=loadtxt("Holes_plaquette0.txt", dtype=complex)


C12=0
C16=0
NOP=4
NOP0=6
NNN=1
for ln in range(0,NNN):
 C12uu=0
 C12dd=0
 C12ud=0
 C12du=0
 C16uu=0
 C16dd=0
 C16ud=0
 C16du=0
 print ln*1.0/NNN
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
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6
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
              if NPP==NOP0:
               N2=pp1+4*pp2+16*pp3+64*pp4+256*pp5+1024*pp6
               if abs(p2-pp2)+abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)==0:
                if (p1==2 and p6==2 and pp1==0 and pp6==0) or (p1==1 and p6==2 and pp1==3 and pp6==0) : 
                  C16uu=C16uu+VV[N1].conjugate()*VV0[N2]
                if  (p1==2 and p6==1 and pp1==0 and pp6==3) or (p1==1 and p6==1 and pp1==3 and pp6==3):               
                  C16uu=C16uu-VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p6==2 and pp1==1 and pp6==1) or (p1==2 and p6==0 and pp1==1 and pp6==3):               
                  C16dd=C16dd+VV[N1].conjugate()*VV0[N2]
                if (p1==0 and p6==0 and pp1==3 and pp6==3) or (p1==0 and p6==2 and pp1==3 and pp6==1):               
                  C16dd=C16dd-VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p6==2 and pp1==0 and pp6==1) or (p1==2 and p6==0 and pp1==0 and pp6==3) or (p1==1 and p6==0 and pp1==3 and pp6==3) or (p1==1 and p6==2 and pp1==3 and pp6==1): 
                 C16ud=C16ud+VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p6==2 and pp1==1 and pp6==0) or  (p1==0 and p6==1 and pp1==3 and pp6==3): 
                  C16du=C16du+VV[N1].conjugate()*VV0[N2]
                if (p1==2 and p6==1 and pp1==1 and pp6==3) or  (p1==0 and p6==2 and pp1==3 and pp6==0):
                  C16du=C16du-VV[N1].conjugate()*VV0[N2]

               if abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                if (p1==2 and p2==2 and pp1==0 and pp2==0) or (p1==2 and p2==1 and pp1==0 and pp2==3): 
                  C12uu=C12uu+VV[N1].conjugate()*VV0[N2]
                if (p1==1 and p2==2 and pp1==3 and pp2==0) or (p1==1 and p2==1 and pp1==3 and pp2==3):               
                  C12uu=C12uu-VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p2==2 and pp1==1 and pp2==1) or (p1==0 and p2==2 and pp1==3 and pp2==1):               
                  C12dd=C12dd+VV[N1].conjugate()*VV0[N2]
                if (p1==2 and p2==0 and pp1==1 and pp2==3) or (p1==0 and p2==0 and pp1==3 and pp2==3):               
                  C12dd=C12dd-VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p2==2 and pp1==0 and pp2==1) or (p1==1 and p2==0 and pp1==3 and pp2==3): 
                  C12ud=C12ud+VV[N1].conjugate()*VV0[N2]
                if (p1==2 and p2==0 and pp1==0 and pp2==3) or (p1==1 and p2==2 and pp1==3 and pp2==1):               
                  C12ud=C12ud-VV[N1].conjugate()*VV0[N2]

                if (p1==2 and p2==2 and pp1==1 and pp2==0) or (p1==2 and p2==1 and pp1==1 and pp2==3) or (p1==0 and p2==2 and pp1==3 and pp2==0) or (p1==0 and p2==1 and pp1==3 and pp2==3): 
                  C12du=C12du+VV[N1].conjugate()*VV0[N2]


 print (C12ud-C12du)/(C16ud-C16du)
 print abs(C12uu-C12dd)
 print abs(C16ud+C16du)
 print abs(C12ud-C12du)
 print abs(C16ud-C16du)





