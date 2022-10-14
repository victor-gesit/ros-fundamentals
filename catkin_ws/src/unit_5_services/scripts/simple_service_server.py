#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

rospy.init_node('bb8_circle_service')

def callback(request):
    print("Req: ", request)
    turn_around()
    return EmptyResponse()

def turn_around():
    data.linear.x = 0.2
    data.angular.z = 0.2
    publisher.publish(data)

data = Twist()
my_service = rospy.Service('/move_bb8_in_circle', Empty, callback)
publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()