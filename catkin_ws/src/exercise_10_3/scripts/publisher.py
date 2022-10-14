#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node("topic_publisher")
publisher = rospy.Publisher("/counter", Int32, queue_size=1)

msg = Int32()

init_value = 0
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    msg.data = init_value
    publisher.publish(msg)
    init_value += 1
    rate.sleep()



