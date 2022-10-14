#! /usr/bin/env python

import rospy

rospy.init_node('ObiWan')
print("Help me Obi-Wan Kenobi")

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    print("Help me Obi-Wan kenobi, you're my only hope")
    rate.sleep()