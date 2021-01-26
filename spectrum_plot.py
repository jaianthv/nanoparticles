import matplotlib.pyplot as plt
import numpy as np
import os

#file = open("data_thickness.txt")
#lines = file.readlines()
#lines[0] = []


os.chdir('C:/Users/JaianthV/Documents/Globus/Co_4A2_150321/data/')
         
with open('Co_C_capped.txt') as f:
    lines = f.readlines()
    
    split = lines[0].split("\t")
    #split = lines[0].split(" ")
    print ((split))
    print (len(split))
    #print (lines)
    del(lines[0]);
    sum_array = np.zeros(70);
    for i in range(1,len(split)-2,2):
        Energy = [line.split("\t")[0] for line in lines]
        Energy = np.array(Energy, dtype=np.float32)
        #print (Energy)
        x = [line.split("\t")[i] for line in lines]
        y = [line.split("\t")[i+1] for line in lines]
        for ii in range(len(y)):
            has_n ="\n" in y[ii]
            if has_n == True:
                y[ii].replace('\n',' ')
                
                y[ii] = float(y[ii])
            else:
                
                y[ii] = float(y[ii])
            has_n ="\n" in x[ii]
            if has_n == True:
                x[ii].replace('\n',' ')
                
                x[ii] = float(x[ii])
            else:
                
                x[ii] = float(x[ii])
        #plt.plot(Energy,np.divide(x,y))
        #plt.ylim(0.9,1.1)
        #plt.show()
            
        
        sum_array = sum_array + np.divide(x,y)
        #plt.plot(Energy,sum_array)
        #plt.ylim(0.9,1.1)
        #plt.show()
    
    sum_array = sum_array/((len(split)-1)/2)
    sum_array = (sum_array - min(sum_array))/(max(sum_array)-min(sum_array))
    
    filename_area = open("Co_C_capped_plot.txt","a")
    for i in range(0,len(Energy)):
        filename_area.write("%f,%f\n"%(Energy[i],sum_array[i]))
    filename_area.close()
    
    plt.plot(Energy,sum_array)
    plt.xlabel("Energy (e.V)", fontsize = 15)
    plt.ylabel("XA (a.u.)", fontsize = 15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0,1.09)
    #plt.xlim(775,788)
    #text = 'Average ='+str(round(average,1)) + ' $\pm$ 0.9 ($\mu$m) '
    #plt.text(0, 32, text , fontsize=15)
    #plt.yscale("linear")
    #plt.xscale("log")
    plt.title("Carbon capped", fontsize = 15)
    plt.show()

