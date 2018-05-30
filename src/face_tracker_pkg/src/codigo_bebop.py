#! /usr/bin/env python
import rospy
from std_msgs.msg import *
from geometry_msgs.msg import Twist

msg = 0

def callback(data):
	msg = rospy.loginfo(rospy.get_caller_id() + "Escuchamos un %s", data.data)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/face_found', String, callback, queue_size = 1) 

	# publishers and data to publish
	empty = Empty()
	takeoff = rospy.Publisher('bebop/takeoff', Empty, queue_size=10)
	land = rospy.Publisher('bebop/land', Empty, queue_size=10)
	rate = rospy.Rate(10);rospy.init_node('listener', anonymous=True)
	rospy
	# takeoff and land
	takeoff.publish(empty)
	rospy.loginfo("Entra en el if, cambia despegue a valor 1")
	rate.sleep()
	rospy.sleep(1)


	takeoff.publish(empty)
	rospy.loginfo("Entra en el if, cambia despegue a valor 1")
	rate.sleep()
	rospy.sleep(10)
	print ("data: ",msg)

	if msg == 'h':
		land.publish(empty)
	rospy.spin()

if __name__ == '__main__':
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
