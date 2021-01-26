import matplotlib.pyplot as plt
import numpy as np
import os

#file = open("data_thickness.txt")
#lines = file.readlines()
#lines[0] = []


os.chdir('C:/Users/JaianthV/Documents/Globus/Data_analysis/')

#files=['Room_temperature_plot.txt','100_degrees_plot.txt','200_degrees_plot.txt','450_degrees_plot.txt']
files=['300_deg_origin_new.txt']
#,'1atm_plot.txt']


for i in range(0,len(files)):
    X=[]
    Y=[]
    
    f = open(files[i], "r")
    
    for line in f:
        
        split = line.split("\t");
        print ((split))
        if (len(split)) == 2:
           if split[0] != "\n":
              X.append(float(split[0]));
              #split[1].replace("\n"," ")
              Y.append(float(split[1]));
    print (min(Y))
    Y= np.array(Y,dtype=np.float32)
    Y = (Y - min(Y))/(max(Y)-min(Y))
    filename_area = open("300deg_new_plot.txt","a")
    for i in range(0,len(Y)):
        filename_area.write("%f,%f\n"%(X[i],Y[i]))
    filename_area.close()
