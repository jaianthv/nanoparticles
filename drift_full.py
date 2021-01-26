import os
import sys
import cv2 as cv
import numpy as np
from PIL import Image
from scipy.ndimage import shift
import hyperspy.api as hs
import matplotlib.pyplot as plt

folder_defocus = "C:/Users/JaianthV/Desktop/XLD/"
#defocus_image = "i160601_055.tif"
#file_name = folder_defocus+defocus_image;
#defocus = Image.open(file_name)
#defocus = np.array(defocus, dtype = np.uint32)


folder = "C:/Users/JaianthV/Documents/Globus/s170909_019/Back_sub/Drift/"
os.chdir(folder)

'''
temp = cv.imread("i160606_Copy.tif",-1)
temp = Image.open("i160606_Copy.tif")
base_img = np.array(temp, dtype =np.uint32)
print(type(base_img))
cv.imshow('dsa',temp)
cv.waitKey(0)
cv.destroyAllWindows()
'''

'''
def center(x1,y1,x2,y2):
    x = x1+(x2/2)
    y = y1+(y2/2)
    c = [x,y]
    return c

List_of_files = os.listdir()
List_of_tiff_files=[];
for i in range(len(List_of_files)):
    Is_it_tiff=".tif" in List_of_files[i]
   
    if Is_it_tiff==True:
       List_of_tiff_files.append(List_of_files[i])

image = cv.imread(List_of_files[0],-1)
th, im_th = cv.threshold(image, 1.65, 1.7, cv.THRESH_BINARY)
r = cv.selectROI('video',im_th, fromCenter = False)
cv.destroyAllWindows()
    #takes the ceter of defined ROI
initial = center(int(r[0]),int(r[1]),int(r[2]),int(r[3]))
print (initial)

#if key == 27:
#   cv.destroyAllWindows()
'''

List_of_files = os.listdir()
List_of_nxs_files=[];
images = [];

for i in range(len(List_of_files)):
    Is_it_tiff=".tif" in List_of_files[i]
   
    if Is_it_tiff==True:
        #List_of_tiff_files.append(List_of_files[i])
        #temp = cv.imread(List_of_files[i],-1)
        
        temp = Image.open(List_of_files[i])
        temp = np.array(temp, dtype=np.float32)
        #temp = temp
        #temp = np.array(temp, dtype=np.uint32)
        #plt.matshow(temp)
        #plt.show()
        images.append(temp)
        

s = hs.signals.Signal2D(images)
shift = s.estimate_shift2D(reference='current',dtype='float',sub_pixel_factor=500)#(reference='current',
#print (shift)
#s.align2D(shifts=shift)
#split = folder.split('/')
#save_files = split[len(split)-1]
#s.save("test.tiff")

folder = "C:/Users/JaianthV/Documents/Globus/s170909_019/Back_sub/"
os.chdir(folder)
List_of_files = os.listdir()
List_of_nxs_files=[];
images = [];

for i in range(len(List_of_files)):
    Is_it_tiff=".tif" in List_of_files[i]
   
    if Is_it_tiff==True:
        #List_of_tiff_files.append(List_of_files[i])
        #temp = cv.imread(List_of_files[i],-1)
        
        temp = Image.open(List_of_files[i])
        temp = np.array(temp, dtype=np.float32)
        #temp = temp
        #temp = np.array(temp, dtype=np.uint32)
        #plt.matshow(temp)
        #plt.show()
        images.append(temp)
        
s = hs.signals.Signal2D(images)
s.align2D(shifts=shift)
split = folder.split('/')
save_files = split[len(split)-1]
s.save("test.tiff")

print ((images))

    


