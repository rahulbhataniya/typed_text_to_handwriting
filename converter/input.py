 
#for small later in first uploaded file there will be exact 13 character a-m
#for next upload file there will be exact 13 character n-z

#same foe capital laters

#the upload digits 0-9 in a single line

#all the upload file will be exactly one line 
#and characters and digits in a sequence

from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import os
import cv2
#cv2.imshow('first',image)
#print(image.shape)
def recognize(path_to_read,user_name,start,case):
	image = cv2.imread(path_to_read)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)
	thresh1 = cv2.threshold(blurred,150,255, cv2.THRESH_BINARY)[1]#This operation takes any 
	# pixel value p >= 150 and sets it to 255 (white). Pixel values < 200 are set to 0 (black)

	#resize the image

	scale_percent = 30 # percent of original size
	width = int(thresh1.shape[1] * (scale_percent) / 100)
	height = int(thresh1.shape[0] * (scale_percent) / 100)

	dim = (1395, 261)
	# resize image
	print(dim)
	thresh1 = cv2.resize(thresh1, dim)
	#cv2.imshow('risize',thresh1)
	#thresh1=cv2.resize(thresh1,(1080,660)) 

	#cv2.imshow('thresh1',thresh1)
	thresh= ~thresh1  
	#convert black to white and white to black
	# perform a series of erosions and dilations to remove
	# any small blobs of noise from the thresholded image
	#thresh = cv2.erode(thresh, None, iterations=3)
	kernel=np.ones((5,5),np.uint8)
	thresh = cv2.dilate(thresh,kernel, iterations=5)

	# perform a connected component analysis on the thresholded
	# image, then initialize a mask to store only the "large"
	# components
	labels = measure.label(thresh, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")
	print(mask)
	# loop over the unique components
	for label in np.unique(labels):
		# if this is the background label, ignore it
		if label == 0:
			continue
		# otherwise, construct the label mask and count the
		# number of pixels 
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255  #convert that lable to white
		numPixels = cv2.countNonZero(labelMask)

		# if the number of pixels in the component is sufficiently
		# large, then add it to our mask of "large blobs"
		if numPixels > 100:
			mask = cv2.add(mask, labelMask)
		
	# find the contours in the mask, then sort them from left to
	# right
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = contours.sort_contours(cnts)[0]
	# loop over the contours
	for (i, c) in enumerate(cnts):
		# draw the bright spot on the image
		(x, y, w, h) = cv2.boundingRect(c)
		((cX, cY), radius) = cv2.minEnclosingCircle(c)
		#cv2.rectangle(thresh1,(x-2,y-2),(x+w+2,y+h+2),(0 ,0,255),3)
		#cv2.imshow("rec",thresh1)
		cv2.waitKey(50)
		cropped=thresh1[y-2:y+h+2,x-2:x+w+2]
		#print(cropped.shape)
		if cropped.shape[0]>=4 and cropped.shape[0]<=400 and cropped.shape[1]>=2 and cropped.shape[1]<=400 and cropped.shape[1]*cropped.shape[0]>1000:
			output=cv2.resize(cropped,(50,113))
			#cv2.imshow("cropped",output)
			#print('we are going to save image {}'.format(i))
			path_to_write=os.path.join("/text_to_hand/media/res",user_name)
			if not os.path.exists(path_to_write):
				os.makedirs(path_to_write)

			#cv2.imwrite(path_to_write,output)
			path_to_image=f"{start}_{case}"+".png"
			path_to_write_image=os.path.join(path_to_write,path_to_image)
			cv2.imwrite(path_to_write_image,output)
			#cv2.imwrite("E:\\txttohandwritting-master\\train\%d.png"%i,output)
			#cv2.circle(image, (int(cX), int(cY)), int(radius),(0, 0, 255), 3)
			cv2.putText(thresh1, "#{}".format(start), (x, y - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
			#cv2.imshow("rec",thresh1)
			cv2.waitKey(100)
			start=chr(ord(start) + 1)
	# show the output image 
	#cv2.imshow("Image", thresh1)
def genrate_char(list_of_path,username="rahul"):
	print(list_of_path)
	recognize(list_of_path[0],username,'0','digit')
	recognize(list_of_path[1],username,'a','small')
	recognize(list_of_path[2],username,'o','small')
	recognize(list_of_path[3],username,'A','upper')
	recognize(list_of_path[4],username,'N','upper')
	
	return (os.path.join("/text_to_hand/media/res",username))
if __name__ == "__main__":
	list_of_path=[]
	list_of_path.append("/text_to_hand/converter/static/upload/traine_model/0_9.jpg")
	list_of_path.append("/text_to_hand/converter/static/upload/traine_model/a_n.jpg")
	list_of_path.append("/text_to_hand/converter/static/upload/traine_model/o_z.jpg")
	list_of_path.append("/text_to_hand/converter/static/upload/traine_model/A_M.jpg")
	list_of_path.append("/text_to_hand/converter/static/upload/traine_model/N_Z.jpg")
	username='rahul'
	genrate_char(list_of_path,username)


 








