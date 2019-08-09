from numpy import *
from pylab import *
from math import *
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from numpy import linalg as LA
from math import exp

S=0
for N1 in range(0,8192):
              p1=N1%2
              NR=p1
              p2=(N1%4-p1)/2
              NR=NR+2*p2 
              p3=(N1%8-NR)/4
              NR=NR+4*p3
              p4=(N1%16-NR)/8
              NR=NR+8*p4
              p5=(N1%32-NR)/16
              NR=NR+16*p5
              p6=(N1%64-NR)/32
              NR=NR+32*p6
              p7=(N1%128-NR)/64
              NR=NR+64*p7
              p8=(N1%256-NR)/128
              NR=NR+128*p8
              p9=(N1%512-NR)/256
              NR=NR+256*p9
              p10=(N1%1024-NR)/512
              NR=NR+512*p10
              p11=(N1%2048-NR)/1024
              NR=NR+1024*p11
              p12=(N1%4096-NR)/2048
              NR=NR+2048*p12
              p13=(N1-NR)/4096
              for N2 in range(0,8192):
                           pp1=N2%2
                           NRR=pp1
                           pp2=(N2%4-pp1)/2
                           NRR=NRR+2*pp2 
                           pp3=(N2%8-NRR)/4
                           NRR=NRR+4*pp3
                           pp4=(N2%16-NRR)/8
                           NRR=NRR+8*pp4
                           pp5=(N2%32-NRR)/16
                           NRR=NRR+16*pp5
                           pp6=(N2%64-NRR)/32
                           NRR=NRR+32*pp6
                           pp7=(N2%128-NRR)/64
                           NRR=NRR+64*pp7
                           pp8=(N2%256-NRR)/128
                           NRR=NRR+128*pp8
                           pp9=(N2%512-NRR)/256
                           NRR=NRR+256*pp9
                           pp10=(N2%1024-NRR)/512
                           NRR=NRR+512*pp10
                           pp11=(N2%2048-NRR)/1024
                           NRR=NRR+1024*pp11
                           pp12=(N2%4096-NRR)/2048
                           NRR=NRR+2048*pp12
                           pp13=(N2-NRR)/4096
