import numpy as np
import matplotlib.pyplot as plt
import sys as os

#Energy
No = 11
path= "C:/Users/JaianthV/Documents/Globus/XLD_HD/Lin0/";
Nameoffile=path+"Energy.txt";

Energy =[];

#f = open(Nameoffile, "r")



with open(Nameoffile) as f:
     lines = f.readlines()
        
for line in lines:
    Energy.append(float(line.replace("\t"," ")));



#Lin 0
path= "C:/Users/JaianthV/Documents/Globus/XLD_HD/Lin0/";
Nameoffile=path+"P"+str(No)+".csv";
Nameofback=path+"P"+str(No)+"_back.csv";

Y = [];
back = [];
Lin_zero = [];

with open(Nameoffile) as f:
     lines = f.readlines()
     del(lines[0])
for line in lines:
    split = line.split(",");
    Y.append(float(split[1].replace("\n"," ")));

with open(Nameofback) as f:
     lines = f.readlines()
     del(lines[0])
for line in lines:
    split = line.split(",");
    back.append(float(split[1].replace("\n"," ")));

Lin_zero = np.divide(Y,back)
Lin_zero = list(np.subtract(Lin_zero,Lin_zero[0]))


#Lin 90
path= "C:/Users/JaianthV/Documents/Globus/XLD_HD/Lin90/";
Nameoffile=path+"P"+str(No)+".csv";
Nameofback=path+"P"+str(No)+"_back.csv";

Y = [];
back = [];
Lin_90 = [];

with open(Nameoffile) as f:
     lines = f.readlines()
     del(lines[0])
for line in lines:
    split = line.split(",");
    Y.append(float(split[1].replace("\n"," ")));

with open(Nameofback) as f:
     lines = f.readlines()
     del(lines[0])
for line in lines:
    split = line.split(",");
    back.append(float(split[1].replace("\n"," ")));

Lin_90 = np.divide(Y,back)
Lin_90 = list(np.subtract(Lin_90,Lin_90[0]))
print (Lin_zero)


filename_area = open("P_new"+str(No)+"processed.txt","a")
filename_area.write("Energy,Lin_0,Lin90\n")
for i in range(0,len(Energy)):
    filename_area.write("%f,%f,%f\n"%(Energy[i],Lin_zero[i],Lin_90[i]))
filename_area.close()


'''

plt.figure(1)
#plt.subplot(211)
plt.plot(Energy,Lin_zero,'r',Energy,Lin_90,'b', linewidth = 4) 
plt.ylabel('XAS (a.u.)',fontsize = 10)
plt.xlabel('Energy (eV)', fontsize = 10)
plt.legend(["0_deg","90_deg"], loc='upper left')
plt.title("Particle"+str(No), fontsize = 15)
#plt.ylim(-0.05,0.05)
plt.tick_params(labelsize=10)
#ax.xaxis.set_tick_params(labelsize=20)

#plt.subplot(212)
#plt.plot(X1,Y1) 
#plt.ylabel('XMCD')
#plt.xlabel('Distance (um)')
plt.show();

'''
