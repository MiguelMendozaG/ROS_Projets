#! /usr/bin/env python
import rospy
from std_msgs.msg import *
from geometry_msgs.msg import Twist
import cv2

face_detected = 0

def action(dato):
	global face_detected
	face_detected = 1
	print ("action, rotando ",dato)

def callback(data):
	action(data.data)
	rospy.loginfo(rospy.get_caller_id() + " Escuchamos un %s", data.data)

def listener():
	rospy.init_node('listener', anonymous=False)
	msg = rospy.Subscriber('/face_found', String, callback, queue_size = 10)

	# publishers and data to publish
	empty = Empty()
	takeoff = rospy.Publisher('bebop/takeoff', Empty, queue_size=10)
	land = rospy.Publisher('bebop/land', Empty, queue_size=10)
	rate = rospy.Rate(10)
	rospy.init_node('listener', anonymous=False)
	move_cmd = Twist()
	move_cmd.linear.x = 0
	move_cmd.linear.y = 0
	move_cmd.angular.z = 0.8

	# takeoff and land
	takeoff.publish(empty)
	rospy.loginfo("Sleep 1")
	rate.sleep()
	rospy.sleep(1)

	takeoff.publish(empty)
	rospy.loginfo("Sleep 2")
	rate.sleep()
	rospy.sleep(5)
	
	while not rospy.is_shutdown():
		global face_detected
		if face_detected == 1:
			cmd_vel = rospy.Publisher('bebop/cmd_vel', Twist, queue_size = 10 )
			cmd_vel.publish(move_cmd)	
			rospy.sleep(2)		
			rospy.loginfo(" En espera de rostro..." )
			face_detected = 0
		#rospy.loginfo(" En espera de rostro..." )


	rospy.loginfo("Fin")	
	land.publish(empty)
	rospy.spin()


face_detected = 0
listener()

"""
move_cmd = Twist()
move_cmd.linear.x = 1
move_cmd.linear.y = 0
move_cmd.linear.z = 0

move_cmd.angular.x = 0
move_cmd.angular.y = 0
move_cmd.angular.z = 0

rospy.sleep(3)

cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)
rospy.sleep(2)

move_cmd.linear.x = 0
move_cmd.linear.y = 1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)
move_cmd.linear.y = 0
move_cmd.linear.x = -1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)

move_cmd.linear.x = 0
move_cmd.linear.y = -1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)
move_cmd.linear.y = 0
move_cmd.linear.z = 1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)

#move_cmd.linear.x = 0
move_cmd.linear.z = -1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)
move_cmd.linear.z = 0
move_cmd.angular.z = 1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)
move_cmd.angular.z = -1
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

rospy.sleep(2)
move_cmd.angular.z = 0
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 1 )
cmd_vel.publish(move_cmd)

land.publish(empty)

"""
