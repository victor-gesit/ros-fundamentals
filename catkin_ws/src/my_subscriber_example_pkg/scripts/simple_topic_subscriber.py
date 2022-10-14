#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry


def callback(msg):
    print(msg.header)
    print(msg.child_frame_id)
    print(msg.pose)
    print(msg.twist)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/odom', Odometry, callback)

rospy.spin()