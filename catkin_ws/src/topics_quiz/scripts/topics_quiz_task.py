#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32

rospy.init_node("topics_quiz_node")

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

vel = Twist()
linear_vel = 0.5
angular_vel = 0.5


def callback(message):
    ranges = message.ranges
    distance_in_front = ranges[360]
    distance_on_left = ranges[719]
    distance_on_right = ranges[0]
    print("Distance In Front", distance_in_front)
    print("Distance On Left", distance_on_left)
    print("Distance On Right", distance_on_right)
    if distance_in_front < 1:
        turn_left()
        return
    if distance_on_right < 1:
        turn_left()
        return
    if distance_on_left < 1:
        turn_right()
        return
    move_straight()


sub1 = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback=callback)


rate = rospy.Rate(1)
def turn_left():
    print("Turn Left")
    vel.linear.x = 0
    vel.angular.z = angular_vel
    pub.publish(vel)


def turn_right():
    print("Turn Right")
    vel.linear.x = 0
    vel.angular.z = -angular_vel
    pub.publish(vel)


def move_straight():
    print("Move Straight")
    vel.angular.z = 0
    vel.linear.x = linear_vel
    pub.publish(vel)


rospy.spin()
