#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node("custom_bb8_server_caller")

custom_movement_service = rospy.ServiceProxy("/move_bb8_in_circle_custom", MyCustomServiceMessage)

request = MyCustomServiceMessageRequest()
request.duration = 5

custom_movement_service(request)