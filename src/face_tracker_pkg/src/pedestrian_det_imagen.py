# importamos los paquetes necesarios
import rospy
from std_msgs.msg import String
#from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# se inicializa el descriptor centenido en opencv
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


#quitar comentarios para buscar peatones en imagenes
im_path = "/home/bebop/ros_bebop_ws/src/face_tracker_pkg/src/pedestrian.jpeg"
imagePath = im_path
image = cv2.imread(imagePath)
image = imutils.resize(image, width=min(400, image.shape[1]))



def publisher_():
	rospy.init_node('ped_node', anonymous = False)
	pub = rospy.Publisher('publish_ped', String, queue_size=10)
	rate = rospy.Rate(10);
	# detecta personas
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
	padding=(8, 8), scale=1.05)

	#enmarca personas detectadas
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# dibuja cuadros finales, suprimiendo dobles cuadros
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
	string_ = str(len(rects))
	pub.publish(string_)
	rate.sleep()

	# informacion extra
	filename = imagePath[imagePath.rfind("/") + 1:]
	print("[INFO] {}: {} original boxes, {} after suppression".format(
		filename, len(rects), len(pick)))

	# muestra las imagenes
	cv2.imshow("After NMS", image)
	cv2.waitKey(0)
	

if __name__ == '__main__':
	publisher_()
