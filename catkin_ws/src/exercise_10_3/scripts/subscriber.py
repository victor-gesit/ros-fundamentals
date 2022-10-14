#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data)

rospy.init_node("topic_subscriber")
subscriber = rospy.Subscriber("/counter", Int32, callback)

rospy.spin()