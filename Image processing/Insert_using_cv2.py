import numpy as np
import int_to_bin 
import bin_to_int
import cv2
def red_pixel(l,m,n):
    red_pxl_of_img = img[l,m,n]

    #print(red_pxl_of_img)
    bin_pxl=int_to_bin.method(red_pxl_of_img) # convert the integer into binary so that we can change last bit of binary value according to data 
    bin_pxl[7]=1 # inserting data in last bit of binary value 
    int_pxl=bin_to_int.method(bin_pxl) # converting the binary value in to corresponding integer 
    #print(int_pxl)
    img[l,m,n]=int_pxl


def green_pixel(l,m,n):
    '''img_shape = img.shape
    for l in range (0,img_shape[0]):
        for m in range(0,img_shape[1]):
            for n in range(1,2):
                green_pxl_of_img = img[l,m,n]
                #print(green_pxl_of_img)
                break
            break
        break
    '''
    green_pxl_of_img = img[l,m,n]
    #print(green_pxl_of_img)
    bin_pxl=int_to_bin.method(green_pxl_of_img) # convert the integer into binary so that we can change last bit of binary value according to data 
    bin_pxl[7]=1 # inserting data in last bit of binary value 
    int_pxl=bin_to_int.method(bin_pxl) # converting the binary value in to corresponding integer 
    #print(int_pxl)
    img[l,m,n]=int_pxl


msg="I am a student"
int_value_of_msg = list()
bin_value_of_msg = list()
for i in msg:
    int_value_of_msg.append(ord(i))
print(int_value_of_msg)
print("___________________ convert the message's ascii value into binary ______________________________________________")
for i in int_value_of_msg:
    temp = int_to_bin.method(i)
    bin_value_of_msg.append(temp)
for i in bin_value_of_msg:
    print(i)

print("________________________ insert the all bit into pixel _________________________")
print(len (bin_value_of_msg) )
print(type(bin_value_of_msg))


print("_________________________Main function ____________________________________")

path1 = "H:\Shaap\Image processing\stinkbug.png" # image path
img = cv2.imread(path1,1) # Reding image in RGB mode 
print("____________________ original image _________________________")
#print(img)
'''
cv2.imshow("Orginal Image",img) # Showing original image 
cv2.waitKey(0)
'''
print("________________________________________________ red pixel of img ____________________________________________________________________")
img_shape = img.shape
for l in range (0,img_shape[0]):
    for m in range(0,10): #img_shape[1]
        for n in range(0,1): # picking red pixel of image 
            #value = bin_value_of_msg[]
            red_pxl_of_img = img[l,m,n]
            bin_of_red_pxl=int_to_bin.method(red_pxl_of_img)
            if (bin_of_red_pxl[7]==0):
                green_pixel(l,m,n+1)
            elif (bin_of_red_pxl[7]==1):
                red_pixel(l,m,n+2)
            
        
    break

#print(img)
'''cv2.imshow("Stego Image",img)
cv2.waitKey(0)
#cv2.destroyAllWindows()''' 
