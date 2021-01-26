import matplotlib.pyplot as plt
import numpy as np
import os

#file = open("data_thickness.txt")
#lines = file.readlines()
#lines[0] = []


os.chdir('C:/Users/JaianthV/Documents/Globus/Co_4A2_150321/data/')

#files=['Room_temperature_plot.txt','100_degrees_plot.txt','200_degrees_plot.txt','300deg_new_plot.txt','450_degrees_plot.txt']
#files=['0L_new_plot.txt','1atm_new_plot.txt','100d_HO_plot.txt','200_deg_plot.txt','450_deg_plot.txt']
files=['0L_new_plot.txt','Co_C_capped_plot.txt']
names =[]
xas =[]
Energy =[]
for i in range(0,len(files)):
    X=[]
    Y=[]
    
    f = open(files[i], "r")
    
    for line in f:
        
        split = line.split(",");
        X.append(float(split[0]));
        Y.append(float(split[1].replace("\n"," ")));
        #X= np.array(X)
        #Y= np.array(Y)
        print (X)
        
       # print (len(split))
        #if (len(split)) == 2:
         #  if split[0] != "\n":
          #    X.append(float(split[0]));
           #   split[1].replace("\n"," ")
            #  Y.append(float(split[1]));
    Energy.append(X)
    xas.append(Y)
    
    #np.append(Energy,X)
    #np.append(xas,Y)
    X=[]
    Y=[]
   
    #Energy = X;
    
#print ((Energy))
Energy[0] = np.array(Energy[0], dtype=np.float32)-1.45
Energy[1] = np.array(Energy[1], dtype=np.float32)
#Energy[2] = np.array(Energy[2], dtype=np.float32)
#Energy[3] = np.array(Energy[3], dtype=np.float32)
#Energy[4] = np.array(Energy[4], dtype=np.float32)


xas[0] = np.array(xas[0],dtype=np.float32)
xas[1] = np.array(xas[1],dtype=np.float32)
#xas[2] = np.array(xas[2],dtype=np.float32)+4
#xas[3] = np.array(xas[3],dtype=np.float32)+6
#xas[4] = np.array(xas[4],dtype=np.float32)+8
#print (xas[3])
plt.plot(Energy[0],xas[0],Energy[1],xas[1])#,Energy[2],xas[2],Energy[3],xas[3],Energy[4],xas[4])
#plt.legend(["RT","100","200","300","450"], loc='upper left')
#plt.plot(Energy[3],xas[3]-6)
plt.xlabel("Energy (e.V)", fontsize = 15)
plt.ylabel("XA (a.u.)", fontsize = 15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.xlim(775,788)
#plt.title("Reduction process", fontsize = 15)
#plt.grid()
plt.show()
#np.resize


