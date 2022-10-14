#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
cmd_vel = Twist()
cmd_vel.linear.x = 1
cmd_vel.angular.z = 0.5

while not rospy.is_shutdown():
    pub.publish(cmd_vel)
    rate.sleep()

print("Shutting down...")
cmd_vel.linear.x = 0
cmd_vel.angular.z = 0
pub.publish(cmd_vel)