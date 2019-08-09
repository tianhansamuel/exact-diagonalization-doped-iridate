from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp


VVD=loadtxt("Holes_plaquette2.txt", dtype=complex)
VVH=loadtxt("Holes_plaquette0.txt", dtype=complex)
ff1=open('Hole_order.dat','w')
ff2=open('Angles.dat','w')
ff3=open('Parametre_order.dat','w')
NOP=4
NOP0=6
NNN=100
print VVD.shape[0]
print VVH.shape[0]

for ln in range(0,NNN):
 p=ln*1.0/NNN
 ff3.write(str(p)+'\t')
 C12X=C23Y=C34Z=0
 C12=C23=C34=0
 C12_2=C23_2=C34_2=0
 C12X_2=C23Y_2=C34Z_2=0
 PPX00=PPX01=PPX10=PPX11=0
 PPY00=PPY01=PPY10=PPY11=0
 PPZ00=PPZ01=PPZ10=PPZ11=0


 C45X=C56Y=C61Z=0
 C45=C56=C61=0
 C45_2=C56_2=C61_2=0
 C45X_2=C56Y_2=C61Z_2=0
 ff1.write(str(ln*1.0/NNN)+'\t')
 ff2.write(str(ln*1.0/NNN)+'\t')
 NOO=ln*4096
 for p1 in range(0,4):
  for p2 in range(0,4):
   for p3 in range(0,4):
    for p4 in range(0,4):
     for p5 in range(0,4):   
      for p6 in range(0,4):
        N1=p1+4*p2+16*p3+64*p4+256*p5+1024*p6+NOO
        for pp1 in range(0,4):
         for pp2 in range(0,4):
          for pp3 in range(0,4):
           for pp4 in range(0,4):
            for pp5 in range(0,4):   
             for pp6 in range(0,4):
               N2=pp1+4*pp2+16*pp3+64*pp4+256*pp5+1024*pp6+NOO
               if p1==2 and p2==2 and abs(p3-pp3)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 if pp1==0 and pp2==0:
                   C12X=C12X+VVD[N1].conjugate()*VVH[N2]
                   #C12X_2=C12X_2+VVD1[N1].conjugate()*VVH[N2]
                   PPX00=PPX00+VVD[N1].conjugate()*VVH[N2]
                 if pp1==1 and pp2==1:
                   C12X=C12X-VVD[N1].conjugate()*VVH[N2]
                   #C12X_2=C12X_2-VVD1[N1].conjugate()*VVH[N2]
                   PPX11=PPX11+VVD[N1].conjugate()*VVH[N2]
                 if pp1==0 and pp2==1:
                   C12=C12+VVD[N1].conjugate()*VVH[N2]
                   #C12_2=C12_2+VVD1[N1].conjugate()*VVH[N2]
                   PPX01=PPX01+VVD[N1].conjugate()*VVH[N2]
                 if pp1==1 and pp2==0:
                   C12=C12-VVD[N1].conjugate()*VVH[N2]
                   #C12_2=C12_2-VVD1[N1].conjugate()*VVH[N2]
                   PPX10=PPX10+VVD[N1].conjugate()*VVH[N2]
               if p2==2 and p3==2 and abs(p1-pp1)+abs(p4-pp4)+abs(p5-pp5)+abs(p6-pp6)==0:
                 if (pp2==0 and pp3==0):
                   C23Y=C23Y-1j*VVD[N1].conjugate()*VVH[N2]
                   PPY00=PPY00+VVD[N1].conjugate()*VVH[N2]
                 if (pp2==1 and pp3==1):
                   #C23Y_2=C23Y_2-1j*VVD1[N1].conjugate()*VVH[N2]
                   PPY11=PPY11+VVD[N1].conjugate()*VVH[N2]
                 if pp2==0 and pp3==1:
                   C23=C23+VVD[N1].conjugate()*VVH[N2]
                   #C23_2=C23_2+VVD1[N1].conjugate()*VVH[N2]
                   PPY01=PPY01+VVD[N1].conjugate()*VVH[N2]
                 if pp2==1 and pp3==0:
                   C23=C23-VVD[N1].conjugate()*VVH[N2]
                   #C23_2=C23_2-VVD1[N1].conjugate()*VVH[N2]
                   PPY10=PPY10+VVD[N1].conjugate()*VVH[N2]
               if p3==2 and p4==2 and abs(p1-pp1)+abs(p2-pp2)+abs(p5-pp5)+abs(p6-pp6)==0:
                 if pp3==0 and pp4==1:
                   C34=C34+VVD[N1].conjugate()*VVH[N2]
                   C34Z=C34Z-VVD[N1].conjugate()*VVH[N2]
                   #C34_2=C34_2+VVD1[N1].conjugate()*VVH[N2]
                   #C34Z_2=C34Z_2-VVD1[N1].conjugate()*VVH[N2]
                   PPZ01=PPZ01+VVD[N1].conjugate()*VVH[N2]

                 if pp3==1 and pp4==0:
                   C34=C34-VVD[N1].conjugate()*VVH[N2]
                   C34Z=C34Z-VVD[N1].conjugate()*VVH[N2]
                   #C34_2=C34_2-VVD1[N1].conjugate()*VVH[N2]
                  # C34Z_2=C34Z_2-VVD1[N1].conjugate()*VVH[N2]
                   PPZ10=PPZ10+VVD[N1].conjugate()*VVH[N2]
                 if pp3==0 and pp4==0:
                   #C34_2=C34_2-VVD1[N1].conjugate()*VVH[N2]
                  # C34Z_2=C34Z_2-VVD1[N1].conjugate()*VVH[N2]
                   PPZ00=PPZ00+VVD[N1].conjugate()*VVH[N2]
                 if pp3==1 and pp4==1:
                   #C34_2=C34_2-VVD1[N1].conjugate()*VVH[N2]
                  # C34Z_2=C34Z_2-VVD1[N1].conjugate()*VVH[N2]
                   PPZ11=PPZ11+VVD[N1].conjugate()*VVH[N2]
               if p4==2 and p5==2 and abs(p3-pp3)+abs(p1-pp1)+abs(p2-pp2)+abs(p6-pp6)==0:
                 if pp4==0 and pp5==0:
                   C45X=C45X+VVD[N1].conjugate()*VVH[N2]
                  # C45X_2=C45X_2+VVD1[N1].conjugate()*VVH[N2]
                 if pp4==1 and pp5==1:
                   C45X=C45X-VVD[N1].conjugate()*VVH[N2]
                   #C45X_2=C45X_2-VVD1[N1].conjugate()*VVH[N2]
                 if pp4==0 and pp5==1:
                   C45=C45+VVD[N1].conjugate()*VVH[N2]
                   #C45_2=C45_2+VVD1[N1].conjugate()*VVH[N2]
                 if pp4==1 and pp5==0:
                   C45=C45-VVD[N1].conjugate()*VVH[N2]
                   #C45_2=C45_2-VVD1[N1].conjugate()*VVH[N2]
               if p5==2 and p6==2 and abs(p1-pp1)+abs(p4-pp4)+abs(p2-pp2)+abs(p3-pp3)==0:
                 if (pp5==0 and pp6==0) or (pp5==1 and pp6==1):
                   C56Y=C56Y-1j*VVD[N1].conjugate()*VVH[N2]
                   #C56Y_2=C56Y_2-1j*VVD1[N1].conjugate()*VVH[N2]
                 if pp5==0 and pp6==1:
                   C56=C56+VVD[N1].conjugate()*VVH[N2]
                   #C56_2=C56_2+VVD1[N1].conjugate()*VVH[N2]
                 if pp5==1 and pp6==0:
                   C56=C56-VVD[N1].conjugate()*VVH[N2]
                   #C56_2=C56_2-VVD1[N1].conjugate()*VVH[N2]
               if p6==2 and p1==2 and abs(p3-pp3)+abs(p2-pp2)+abs(p5-pp5)+abs(p4-pp4)==0:
                 if pp6==0 and pp1==1:
                   C61=C61+VVD[N1].conjugate()*VVH[N2]
                   C61Z=C61Z+VVD[N1].conjugate()*VVH[N2]
                   #C61_2=C61_2+VVD1[N1].conjugate()*VVH[N2]
                   #C61Z_2=C61Z_2+VVD1[N1].conjugate()*VVH[N2]

                 if pp6==1 and pp1==0:
                   C61=C61-VVD[N1].conjugate()*VVH[N2]
                   C61Z=C61Z+VVD[N1].conjugate()*VVH[N2]
                   #C61_2=C61_2-VVD1[N1].conjugate()*VVH[N2]
                  # C16Z_2=C61Z_2+VVD1[N1].conjugate()*VVH[N2]

 print C12X
 print C45X
 print C12
 print C45
 #ff1.write(str(C12)+'\t')
 #ff1.write(str(C12X)+'\t')
 #ff1.write(str(C23)+'\t')
 #ff1.write(str(C23X)+'\t')
 #ff1.write(str(C34)+'\t')
 #ff1.write(str(C34X)+'\n')

 ff3.write(str(PPX00)+'\t')
 ff3.write(str(PPX01)+'\t')
 ff3.write(str(PPX10)+'\t')
 ff3.write(str(PPX11)+'\n')
 ff3.write(str(PPY00)+'\t')
 ff3.write(str(PPY01)+'\t')
 ff3.write(str(PPY10)+'\t')
 ff3.write(str(PPY11)+'\n')
 ff3.write(str(PPZ00)+'\t')
 ff3.write(str(PPZ01)+'\t')
 ff3.write(str(PPZ10)+'\t')
 ff3.write(str(PPZ11)+'\n')

 #print C12X/C23Y
 #print C23Y/C34Z
 #print C34Z/C45X
 #print C45X/C56Y
 #print C56Y/C61Z
 #print C61Z/C12X

 #r1=C12/C23
 #r2=C12X/C23Y
 #rr1=C12_2/C23_2
 #rr2=C23_2/C34_2
 #print C12/C23
 #print C23/C34
 #print C12_2/C23_2
 #print C23_2/C34_2
 #an1=atan(r1.imag/r1.real)
# if r1.real<0:
 # an1=an1+pi
# an2=atan(r2.imag/r2.real)
 #if r2.real<0:
 # an2=an2+pi

 #ana1=atan(rr1.imag/rr1.real)
# if rr1.real<0:
 # ana1=ana1+pi
# ana2=atan(rr2.imag/rr2.real)
 #if rr2.real<0:
 # ana2=ana2+pi
# ff2.write(str(an1/pi)+'\t')
# ff2.write(str(an2/pi)+'\t')
# ff2.write(str(ana1/pi)+'\t')
# ff2.write(str(ana2/pi)+'\n')
 print '*******************************************'




