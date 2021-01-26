
import numpy as np
import matplotlib.pyplot as plt
import sys as os



path= "C:/Users/JaianthV/Documents/Globus/160606_Co_Nanoparticles/PEEM/";
Nameoffile1=path+"s160606_018.dat";

X1= [];
Y1 =[];

f = open(Nameoffile1, "r")
for line in f:
    
    #split = f.split(",");
    split = line.split("\t");
    #for s in split:
    X1.append((split[0]));

del(X1[0])
for i in range(len(X1)):
    X1[i] = float(X1[i])

    print (round(X1[i],1))
