import cv2
import numpy as np
import glob

name="*.png"
print(name)
#imgs = glob.glob("./result/original_seg.png")
#imgs = glob.glob("/media/sangbin/D/ade20k/ADEChallengeData2016/annotations/training/*.png")
imgs = glob.glob("/media/sangbin/D/2hae_dataset/annotations/training_r/" + name)
numfiles = len(imgs)
print(imgs)
#print(imgs[0])
#img = cv2.imread("/home/yun/data/yun/training/ADE_train_00000012.png",0)
#img = cv2.imread("/home/yun/data/yun/training/ADE_train_00000001.png")

#/home/yun/data/yun/training
#cv2.imshow("test",img)

#img = cv2.imread(imgs[0],0)
#cv2.imshow("test",img)
#fn = imgs[0].split("/")
#result = cv2.imwrite("/home/yun/data/trainingresult/"+fn[6],img)
#print(result)
#cv2.waitKey(0)
#images = []
for fname in imgs:
	img = cv2.imread(fname,0)

	fn = fname.split("/")
	print(fn)


## dataset setup

#0 background
#1 wall
#2 space 2-> 7
#3 space 3-> 1
#4 floor 4-> 2
#5 space 5-> 3
#6 ceiling 6-> 4
# 7 >= -> 0

##origin data 7class
#0 background
#1 wall
#2 table_top
#3 film
#4 floor
#5 window
#6 ceiling

#0~7 5class
#0 background
#1 wall
#2 floor
#3 window
#4 ceiling

	img = np.where(img==2,7,img)
	img = np.where(img==3,1,img)
	img = np.where(img==4,2,img)
	img = np.where(img==5,3,img)
	img = np.where(img==6,4,img)
	img = np.where(img>=7,0,img)
	
	#img = np.where(img>3,4,img)


#	img=np.where(img==58,255,img)
#	img=np.where(img==120,0,img)
#	img=np.where(img==137,0,img)
#	img=np.where(img==163,0,img)
#	cv2.imshow("test",img)
#	cv2.waitKey(0)
	#images.append(img):
	
#	print("/home/semantic-segmentation-pytorch/data/trainingresult/"+fn[6])
	#result = cv2.imwrite("./data/validation/"+fn[4],img)
	result = cv2.imwrite("./result/"+fn[7],img)
	print(result)
	#cv2.imshow("test",img)
	#cv2.waitKey(0)



#cv2.imshow("test1",img)
####
#cv2.waitKey(0)
#cv2.destroyAllWindows()
